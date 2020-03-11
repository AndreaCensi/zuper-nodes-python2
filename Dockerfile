FROM python:2.7

WORKDIR /project
COPY requirements.* ./
RUN pip install -r requirements.resolved
RUN pip list

COPY src /project/src
COPY setup.py .
COPY setup.cfg .

RUN pip install -e .




ENTRYPOINT ["python", "-u", "test.py"]
