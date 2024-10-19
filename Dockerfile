# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn, a production-ready WSGI server
RUN pip install gunicorn

# Initialize the database
RUN python database.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
