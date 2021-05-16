FROM python:3.6-slim
COPY . /app
WORKDIR /app
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export FLASK_ENV=dev
EXPOSE 8080
CMD python run.py