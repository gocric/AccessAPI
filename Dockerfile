FROM ubuntu
ADD AccessAPI.py /
RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install requests
CMD [ "python", "./AccessAPI.py" ]