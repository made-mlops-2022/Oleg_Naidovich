FROM airflow-base:latest

COPY generate_data.py synthetic_data.csv requirements.txt /

ENTRYPOINT ["python3", "generate_data.py"]