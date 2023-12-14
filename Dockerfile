FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .
COPY SVM-service.py .
COPY OurModel.pkl .

RUN pip install -r requirements.txt

CMD ["python", "SVM-service.py"]
