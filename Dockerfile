FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'
#WORKDIR /app
COPY . .
RUN apt-get update -y && apt-get install curl -y \
&& curl -sSL https://install.python-poetry.org | python3 - \
&& poetry install \
&& apt-get remove curl -y

COPY ./app /app
WORKDIR /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000