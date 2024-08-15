# Dockerfile for backend
# Use a Python base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

RUN --mount=type=secret,id=OPENAI_API_KEY,target=/run/secrets/OPENAI_API_KEY.txt \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

ENV PROJECT=peoplemuseum-431817
ENV GOOGLE_APPLICATION_CREDENTIALS=./newYJpeoplemuseum-431817-cd4d14f169c9.json

# Expose the port the application runs on
EXPOSE 8080

# Start the backend server
CMD ["python", "run.py"]
