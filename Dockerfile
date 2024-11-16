# Python Image
FROM python:3.11-slim

# Environment Variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Working Directory
WORKDIR /app

# Copy Requirements to Working Directory
COPY requirements.txt /app/requirements.txt

# Install Requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

