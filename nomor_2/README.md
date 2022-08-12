## Cara Setup dan Running

Run command berikut di CLI dengan folder yang berisi `run.py` dan `soal-2.json`.

```commandline
python -W ignore run.py soal-2.json
```

## Struktur Kode dan Modul

Program dibuat dengan bahasa pemrograman Python dengan module `pandas` untuk pengolahan data dan `sys` untuk CLI command.

## Asumsi
Berikut adalah beberapa asumsi yang digunakan dalam proses data cleaning:

1. Hanya mengambil komoditas dengan satu kata karena keterbatasan waktu.
2. Mengganti beberapa kata yang diasumsikan salah ketik. Berikut daftarnya:
```
{
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
```
3. Mengambil semua berat yang mengandung angka saja.
4. Jika tidak ada satuan kg, maka diasumsikan angka berat adalah dalam kilogram.