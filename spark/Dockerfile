FROM bitnami/spark:3.1.2

COPY spark_job.py /opt/spark/jobs/
COPY requirements.txt /requirements.txt
COPY configuration.yaml /opt/spark/conf/

RUN pip install --no-cache-dir -r /requirements.txt
