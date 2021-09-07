FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org requests bs4 lxml

CMD ["python3", "bot.py"]
