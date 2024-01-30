FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY nyc_taxi_data_pipeline.py nyc_taxi_data_pipeline.py


ENTRYPOINT [ "python", "nyc_taxi_data_pipeline.py" ]