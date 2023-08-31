FROM python

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/Bookstore_project

WORKDIR /usr/src/Bookstore_project

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000