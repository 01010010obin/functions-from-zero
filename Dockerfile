FROM public.ecr.aws/lambda/python:latest


RUN mkdir -p /app
COPY ./main.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]