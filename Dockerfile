FROM python
WORKDIR /app
ADD . .
RUN pip3 install -r requirement.txt
CMD uvicorn main:app
