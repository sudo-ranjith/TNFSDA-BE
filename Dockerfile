FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 8080
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN apt-get install -y python3-setuptools
RUN pip install -r requirements.txt --ignore-installed
CMD python app.py