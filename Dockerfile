FROM python:3.11
LABEL authors="Mabarik667f"

RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]

