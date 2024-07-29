# Imports
import pyspark
from pyspark.sql import SparkSession
import yaml

# Load configuration
with open('/opt/spark/conf/configuration.yaml', 'r') as file:
    config = yaml.safe_load(file)

spark = SparkSession.builder \
    .appName(config['spark']['app_name']) \
    .getOrCreate()

kafka_topic = config['kafka']['topic']
kafka_servers = config['kafka']['bootstrap_servers']
mysql_url = f"jdbc:mysql://{config['mysql']['host']}:{config['mysql']['port']}/{config['mysql']['database']}"
mysql_properties = {
    "user": config['mysql']['user'],
    "password": config['mysql']['password'],
    "driver": "com.mysql.cj.jdbc.Driver"
}
postgres_url = f"jdbc:postgresql://{config['postgres']['host']}:{config['postgres']['port']}/{config['postgres']['database']}"
postgres_properties = {
    "user": config['postgres']['user'],
    "password": config['postgres']['password'],
    "driver": "org.postgresql.Driver"
}

# Read data from Kafka
df = spark \
    .read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Transform data
df = df.selectExpr("CAST(value AS STRING) as json").select(pyspark.sql.functions.from_json("json", schema).alias("data")).select("data.*")

# Write raw data to MySQL
df.write.jdbc(mysql_url, 'raw_taxi_data', 'append', properties=mysql_properties)

# Perform transformation
transformed_df = df.select('column1', 'column2', 'column3')  # Example transformation

# Write transformed data to Postgres
transformed_df.write.jdbc(postgres_url, 'transformed_taxi_data', 'overwrite', properties=postgres_properties)
