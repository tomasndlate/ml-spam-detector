FROM public.ecr.aws/lambda/python:3.13

WORKDIR /var/task

COPY requirements.txt requirements.txt
COPY app.py .

RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]