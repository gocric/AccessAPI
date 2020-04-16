FROM python:3
ADD AccessAPI.py /
RUN pip install requests
CMD [ "python", "./AccessAPI.py" ]