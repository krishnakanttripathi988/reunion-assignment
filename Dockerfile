# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myapp.settings
ENV PYTHONPATH=/app

# Expose the necessary ports
EXPOSE 8000

# Start the MongoDB service

# Run test cases
RUN python manage.py test --exclude-tag no_db 

# Start the Django app
CMD ["python", "manage.py", "runserver"]
