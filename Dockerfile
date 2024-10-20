# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn, a production-ready WSGI server, psycopg2 for PostgreSQL
RUN pip install gunicorn psycopg2-binary 


# Make port 80 available to the world outside this container
EXPOSE 80

# Run the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
