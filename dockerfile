FROM python:3.11.4

WORKDIR /APP
COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8006

CMD ["python", "main.py"]