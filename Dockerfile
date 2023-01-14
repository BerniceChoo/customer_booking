# Create the base Python image .
# Here we use the latest version of Python with the slim version .
FROM python:3.10-slim
# Set the environment variable to ensure the output that
# ... Django writes to the terminal comes out inreal time without
# ... being buffered somewhere. This makes Dockerlogs useful and complete .
ENV PYTHONUNBUFFERED 1
# Update the packages
RUN apt-get update
# Install other packages needed for Django
# ...( in this case , we need mysqlclient for the database ).
RUN apt-get install python3-dev default-libmysqlclient-dev gcc -y
# As root , create ’customer ’ group.
RUN addgroup customer
# As root , create 'desdcustomer' directory
RUN mkdir /desdcustomer
# Set the working directory to ’/desdcustomer ’
WORKDIR /desdcustomer
# Copy the requirements .txt file to the ’/desdcustomer ’directory .
COPY requirements.txt ./
# Install the requirements
RUN pip install -r requirements.txt
# Copy the other files in the project to the ’/desdcustomer ’ directory .
COPY . .
# Tell the container to listen on port 8000
EXPOSE 8000
# Command to be executed when starting acontainer
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
