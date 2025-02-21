# Use the official Python image as base
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /blog_applications

# Copy the application code
COPY . /blog_applications/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirement.txt

# Expose the port the app runs on
EXPOSE 8000

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script to wait for db before starting Django
ENTRYPOINT ["/entrypoint.sh"]
