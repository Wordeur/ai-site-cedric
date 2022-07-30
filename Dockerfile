FROM python
WORKDIR /app
ADD . .
RUN pip3 install -r requirement.txt
CMD uvicorn --host 0.0.0.0 main:app
