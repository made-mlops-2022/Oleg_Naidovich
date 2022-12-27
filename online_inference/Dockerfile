FROM python:3.8-slim

COPY client.py data_schema.py get_test_data.py main.py test_main.py run.sh requirements.txt ./online_inference/
COPY transformer.pkl models.pkl ./online_inference/

WORKDIR ./online_inference

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PATH_TO_MODEL="models.pkl"
ENV PATH_TO_TRANSFORMER="transformer.pkl"

EXPOSE 5000

CMD ["bash", "run.sh"]
