import pandas as pd
import sys

def data_cleaning(file):

    df = pd.read_json(open(file, encoding='utf-8'), orient='records')
    df['komoditas_clean'] = df['komoditas'].str.lower().str.replace('[^a-zA-Z0-9]', ' ')

    # Replace words
    replacement = {
        "salam": "salem",
        "mujaer": "mujair",
        "majaer": "mujair",
        "mujir": "mujair",
        "muajir": "mujair",
        "ikan": "",
        "ikn": "",
        r"\bdan\b": "",
        "gurami": "gurame",
        "lelw": "lele",
        "ikanlele": "lele",
        "kele": "lele",
        "emas": "mas",
        "kembug": "kembung",
        "parin": "patin",
        "gembung": "kembung",
        "krapu": "kerapu",
        "kerpu": "kerapu",
        "tingkol": "tongkol",
        "tngkol": "tongkol",
        "nilem": "nila",
        r"\bnil\b": "",
        r"\bkepala\b": "",
        r"\bmunkar\b": "mujair",
        r"\bmas\b": "mas",
        r"\bpari\b": "laut",
        r"\bbaracuda\b": "laut",
        r"\betong\b": "laut",
        r"\btenggiri\b": "laut",
        r"\bmerah\b": "",
        r"\bhitam\b": ""
    }

    df['komoditas_clean'] = df['komoditas_clean'].replace(replacement, regex=True)

    # Mark irrelevant
    keywords = [
        "ayam", "soto", "babat", "kikil", "nasi", "uduk", "sotobayam", "sea", "food", "pecel", "bebek",
        "goreng", "dll", "bakar", "sate", "usus"
    ]

    df["possibly_irr"] = df['komoditas_clean'].apply(lambda x: 1 if any(i in x for i in keywords) else 0)

    # Remove possibly irrelevant entries
    df = df[df["possibly_irr"] == 0]

    # Remove berat without number
    df= df[df["berat"].str.contains(r'[0-9]')]

    # Replace comma with space
    df['berat_clean'] = df['berat'].str.lower().str.replace(',', ' ')

    # Mark one word only
    df['one_word'] = df['komoditas_clean'].str.match('^[a-zA-Z0-9_]+$')

    # Process one word
    df_one_word = df[df['one_word'] == True].reset_index()

    df_one_word["berat_final_1"] = df_one_word["berat_clean"].str.extract(pat= r'([0-9](?=\skg))')
    df_one_word["berat_final_2"] = df_one_word["berat_clean"].str.extract(pat= r'([0-9](?=kg))')
    df_one_word["berat_final_3"] = df_one_word["berat_clean"].str.extract(pat= r'([0-9])')

    df_one_word["berat_final"] = None

    for i in range(len(df_one_word["berat_final"])):
        if str(df_one_word["berat_final_1"][i]) != 'nan':
            df_one_word["berat_final"][i] = df_one_word["berat_final_1"][i]
        elif str(df_one_word["berat_final_2"][i]) != 'nan':
            df_one_word["berat_final"][i] = df_one_word["berat_final_2"][i]
        else:
            df_one_word["berat_final"][i] = df_one_word["berat_final_3"][i]

    df_one_word = df_one_word[['komoditas_clean', 'berat_final']]
    df_one_word.columns = ['komoditas', 'berat']

    counts = df_one_word.groupby(['komoditas'], as_index=False).count().sort_values(ascending=False, by='berat').reset_index()

    for i in range(len(counts['komoditas'])):
        print(f"{i+1}. {counts['komoditas'][i]}: {counts['berat'][i]}kg")

if __name__ == '__main__':
    file = str(sys.argv[1])

    data_cleaning(file)