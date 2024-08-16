# Dockerfile for backend
# Use a Python base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS='./.peoplemuseum-431817-cadf29853fd4.json'

# GCP Credential will be set by docker compose build process using secret files on local directory

# Expose the port the application runs on
EXPOSE 8080

# Start the backend server
CMD ["python", "run.py"]
