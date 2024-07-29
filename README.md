# NYC Taxi Data Engineering Project

This project is an end-to-end data engineering pipeline that ingests, processes, stores, and visualizes NYC taxi trip data using a variety of tools and technologies. The stack includes Python, SQL, Apache Airflow, Kafka, Apache Spark (PySpark), MySQL, PostgreSQL, Docker, and Looker Studio for data visualization.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Build and Start Services](#build-and-start-services)
  - [Running the Pipeline](#running-the-pipeline)
- [Data Flow](#data-flow)
- [Visualization](#visualization)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The primary objective of this project is to build a scalable data pipeline that streams NYC taxi data from a public API, processes the data using Apache Spark, stores both raw and transformed data in MySQL and PostgreSQL, and visualizes the data using Looker Studio.

## Architecture

![Architecture Diagram](architecture.png) <!-- Add an architecture diagram image here -->

## Technologies Used

- **Python**: For scripting and data manipulation.
- **SQL**: For database interactions.
- **Apache Airflow**: For workflow orchestration.
- **Kafka**: For real-time data streaming.
- **Apache Spark (PySpark)**: For data processing.
- **MySQL**: For storing raw data.
- **PostgreSQL**: For storing processed data.
- **Docker**: For containerizing services.
- **Looker Studio**: For data visualization.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.8+ installed on your machine.

### Configuration

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/data-engineering-project.git
   cd data-engineering-project
   ```

2. Create a `.env` file in the root directory of the project and add your database credentials:

   ```sh
   # .env
   MYSQL_ROOT_PASSWORD=your_mysql_password_here
   POSTGRES_PASSWORD=your_postgres_password_here
   ```

3. Configure the `configuration.yaml` file with the necessary parameters:

   ```yaml
   api:
     url: "https://data.cityofnewyork.us/resource/t29m-gskq.json"
     batch_size: 1000

   kafka:
     topic: "nyc_taxi_data"
     bootstrap_servers: "kafka:9092"

   mysql:
     host: "mysql"
     port: 3306
     user: "root"
     password: "your_mysql_password_here"
     database: "taxi_data"

   postgres:
     host: "postgres"
     port: 5432
     user: "postgres"
     password: "your_postgres_password_here"
     database: "taxi_data"

   spark:
     master: "local[*]"
     app_name: "TaxiDataProcessor"
   ```

### Build and Start Services

1. Build and start the services using Docker Compose:

   ```sh
   docker-compose up --build
   ```

2. In a new terminal, start the Kafka producer:
   ```sh
   cd kafka
   python producer.py
   ```

### Running the Pipeline

1. Access the Airflow UI at [http://localhost:8080](http://localhost:8080).
2. Trigger the `taxi_data_pipeline` DAG to start the pipeline.

### Data Flow

1. **Data Ingestion**: Data is fetched from the NYC taxi data API using the Kafka producer and streamed to a Kafka topic.
2. **Data Processing**: Apache Spark reads data from the Kafka topic, processes it, and writes raw data to MySQL and transformed data to PostgreSQL.
3. **Workflow Orchestration**: Apache Airflow orchestrates the pipeline, ensuring tasks are executed in the correct order.
4. **Data Visualization**: The processed data in PostgreSQL is visualized using Looker Studio.

### Visualization

1. Go to [Looker Studio](https://lookerstudio.google.com/).
2. Connect to the PostgreSQL database using the Postgres connector.
3. Create charts and dashboards to visualize the data.

### Directory Structure

```plaintext
data-engineering-project/
│
├── airflow/
│   ├── dags/
│   │   └── taxi_data_pipeline.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── kafka/
│   ├── docker-compose.yml
│   └── producer.py
│
├── spark/
│   ├── Dockerfile
│   ├── spark_job.py
│   └── requirements.txt
│
├── sql/
│   ├── mysql_init.sql
│   └── postgres_init.sql
│
├── docker-compose.yml
├── configuration.yaml
├── .env
└── README.md
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.
