FROM python:3.11-alpine3.17

RUN mkdir -p /home/intro-to-api-flask/web-app

COPY . /home/intro-to-api-flask/web-app

WORKDIR /home/intro-to-api-flask/web-app

RUN python -m venv .venv

RUN source ./.venv/bin/activate

RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "/home/intro-to-api-flask/web-app/app.py" ]
# ENTRYPOINT [ "/bin/sh" ]