# Use the official Python image from Docker Hub
FROM python:3.9-slim

## Set the working directory inside the container
#WORKDIR /app
#
# Copy the current directory contents into the container at /app
COPY . .
#COPY . .


# Install the required dependencies, including pytest and requests
#RUN pip install --no-cache-dir pytest requests curlify
RUN pip install --no-cache-dir -r requirements.txt


# Run pytest when the container starts
#CMD ["pytest", "-s", "--host=prod", "--disable-pytest-warnings"]
CMD ["pytest", "-s", "--host=prod", "--disable-pytest-warnings", "--html=report.html"]