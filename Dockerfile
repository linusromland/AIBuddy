FROM public.ecr.aws/docker/library/python:3.11

# Create app directory
WORKDIR /app

# Copy all files
COPY . .

# Set environment variables for compose
ARG DISCORD_TOKEN
ENV DISCORD_TOKEN=$DISCORD_TOKEN
ARG DISCORD_SERVER_GUILD_ID
ENV DISCORD_SERVER_GUILD_ID=$DISCORD_SERVER_GUILD_ID
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install --system

CMD [ "python3", "./src/main.py" ]

