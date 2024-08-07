# Dockerfile for backend
# Step 1: Use a Python base image
FROM python:3.9-alpine

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements.txt
COPY requirements.txt ./

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=./yourGCPcredit.json
ENV PROJECT=peoplemuseumyeah
ENV OPENAI_API_KEY=your openAI api key for this project

# Step 6: Expose the port your application runs on (e.g., 5000)
EXPOSE 8080

# Step 7: Start the backend server
CMD ["python", "run.py"]
