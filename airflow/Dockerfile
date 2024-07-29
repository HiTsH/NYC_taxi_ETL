FROM apache/airflow:2.1.0-python3.8

COPY dags/ /opt/airflow/dags/
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt
