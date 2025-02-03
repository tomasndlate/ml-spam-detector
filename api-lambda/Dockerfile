FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY requirements.txt requirements.txt
COPY src/ .

RUN pip install -r requirements.txt

CMD ["predict_lambda.handler"]