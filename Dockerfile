FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
