# Create the base Python image .
# Here we use the latest version of Python with the slim version .
FROM python:3.10-slim
# Set the environment variable to ensure the output that
# ... Django writes to the terminal comes out inreal time without
# ... being buffered somewhere. This makes Dockerlogs useful and complete .
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc -y
RUN addgroup customer
RUN mkdir /desdcustomer
WORKDIR /desdcustomer
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
# Command to be executed when starting acontainer
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]