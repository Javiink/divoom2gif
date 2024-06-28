FROM python:3.9.19-bullseye
RUN apt-get update && \
apt-get install -y liblzo2-dev zlib1g-dev unzip
RUN pip install APIxoo Pillow
WORKDIR /srv
ADD main.py requirements.txt /srv/
RUN cd /srv && pip install -r requirements.txt
CMD ["python", "./main.py"] 