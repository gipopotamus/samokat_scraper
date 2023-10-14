FROM python:3.10

RUN pip install -r requirements.txt

# Копируем исходный код в контейнер
COPY . /app
WORKDIR /app

# Команда для запуска скрапера
CMD ["python", "main.py"]
