# FROM python:3.9.11-alpine3.15 as base
FROM python:3.9-slim

# Bash is installed for more convenient debugging.
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*
# RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

ENV AIRBYTE_ENTRYPOINT "python /airbyte/integration_code/main.py"

WORKDIR /airbyte/integration_code
COPY setup.py ./
RUN pip install .
COPY source_google_ads ./source_google_ads
COPY main.py ./

ENTRYPOINT ["python", "/airbyte/integration_code/main.py"]

LABEL io.airbyte.version=2.0.0
LABEL io.airbyte.name=airbyte/source-google-ads
	