FROM public.ecr.aws/docker/library/python:3.11

# Create app directory
WORKDIR /app

# Copy all files
COPY . .

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install 

CMD [ "pipenv", "run", "start" ]

