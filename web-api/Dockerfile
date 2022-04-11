FROM python:3.7.2-stretch

WORKDIR /app

# This way recognizes the app modules
ADD . /app/web-api

RUN pip install -r web-api/requirements.txt

RUN chmod u+x ./web-api/entrypoint.sh

CMD [ "./web-api/entrypoint.sh" ]

ENV ENV=Production
ENV FLASK_ENV=Production
ENV FLASK_APP=wsgi.pyAAAA