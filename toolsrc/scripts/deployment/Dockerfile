# Dockerfile

# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set the entry point
ENTRYPOINT ["python", "src/main.py"]

# Expose the necessary port (if applicable)
EXPOSE 8000
