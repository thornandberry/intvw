import pendulum
from airflow.utils.task_group import TaskGroup
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator

yesterday = pendulum.today(tz="Asia/Jakarta").add(days=-1)

dag_dir = "/opt/airflow"

default_args = {
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'start_date': yesterday,
        'end_date': None
    }

dag = DAG(  'nomor_1',
            default_args=default_args,
            tags=['nomor_1', 'efishery', 'eka'],
            schedule_interval='0 7 * * *',
            catchup=False,
            concurrency=5)

def bash_op(filename):
    op = BashOperator(
        task_id=filename,
        bash_command=f'python {dag_dir}/queries/run_sql.py {filename}.sql',
        dag=dag
    )

    return op

with TaskGroup(group_id='dimensions', prefix_group_id=False, dag=dag) as dimensions:
    bash_op('dim_date')
    bash_op('dim_customer')

with TaskGroup(group_id='facts', prefix_group_id=False, dag=dag) as facts:
    raw = bash_op('raw')
    fact = bash_op('fact')

    raw >> fact

generate_file = BashOperator(
        task_id="generate_files",
        bash_command=f'python {dag_dir}/plugins/generate_file.py',
        dag=dag
    )

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> dimensions >> facts >> generate_file >> end