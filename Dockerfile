# The image you are going to inherit your Dockerfile from
FROM python:3.10
# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /django_recipe_api
# Set the /django_recipe_api directory as the working directory
WORKDIR /django_recipe_api
# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt