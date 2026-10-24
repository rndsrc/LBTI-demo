# Self-contained image: the app, the committed manual (content/) and its search index, built here.
# Configuration comes from the environment at run time (at least ANTHROPIC_API_KEY); the container writes nothing.
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
COPY scripts scripts
COPY web web
COPY content content
RUN python -m scripts.ingest --offline
USER nobody
EXPOSE 8000
HEALTHCHECK CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz')"]
CMD ["uvicorn", "--factory", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
