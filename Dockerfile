# Base image
# Use a slim Python image for efficiency
FROM python:3.8-slim 

# Working directory
WORKDIR /app

# Install dependencies (requirements.txt)
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy script and stop word file (optional)
COPY . .

# Set the main command

CMD ["python", "cloud_ass.py"]  
