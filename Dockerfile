FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /src/requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /src;
WORKDIR /src