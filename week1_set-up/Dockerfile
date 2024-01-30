FROM python:3.9.1

RUN pip install pandas

WORKDIR /app
COPY nyc_taxi_data_pipeline.py nyc_taxi_data_pipeline.py


ENTRYPOINT [ "python", "nyc_taxi_data_pipeline.py" ]