ARG DOCKER_PLATFORM=$TARGETPLATFORM
FROM --platform=$DOCKER_PLATFORM python:3.11.4-bookworm

ENV PYTHONBUFFERED 1

# Create directory
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Mirror the current directory to the working directory for hotreloading
ADD . /code/

# Copy the .env file
COPY .env /.env

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

# Generate DRF Spectacular Documentation
RUN python backend/manage.py spectacular --color --file backend/schema.yml

# Expose port 8000 for the web server
EXPOSE 8000
