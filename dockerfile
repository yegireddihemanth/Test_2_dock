FROM python:3.11.5

WORKDIR /APP
COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8006
EXPOSE 8009

CMD ["python", "main.py"]