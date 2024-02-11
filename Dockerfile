# Use Python 3.11 official image as the base image
FROM python:3.11


# Copy the contents of the current directory (.) on the host machine
# to the '/app' directory inside the Docker image
COPY . /app

# Set the working directory inside the Docker image to '/app'
# All subsequent RUN, CMD, ADD, and COPY instructions will use '/app' as the starting point
WORKDIR /app

# Update pip (Python package installer) to the latest version
RUN python -m pip install --upgrade pip


# Install the Python packages listed in the 'requirements.txt' file
RUN pip install -r requirements.txt