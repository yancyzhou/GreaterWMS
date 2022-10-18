FROM python:3.9-slim as base
#RUN mkdir -p /GreaterWMS/templates
#copy requirements.txt
#Configure working directory
RUN mkdir AIIRCWMS
WORKDIR /AIIRCWMS
COPY ./ /AIIRCWMS
#Installation foundation dependency
#RUN sed -i s/deb.debian.org/mirrors.163.com/g /etc/apt/sources.list
#RUN apt-get clean

ADD ./requirements.txt /AIIRCWMS/requirements.txt
#RUN apt-get update --fix-missing && apt-get upgrade -y
#RUN apt-get install build-essential -y
#RUN apt-get install supervisor -y
RUN python3 -m pip install --upgrade pip
#Install supervisor
#RUN pip3 install supervisor
#RUN pip3 install -U 'Twisted[tls,http2]'
RUN pip3 install -r requirements.txt
CMD ["daphne","-b","0.0.0.0","-p", "8008", "greaterwms.asgi:application"]
EXPOSE 8008
