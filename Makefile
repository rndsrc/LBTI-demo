PY ?= .venv/bin/python
IMAGE ?= lbti-demo

.PHONY: venv ingest index test eval run image up

venv:     ## Python 3.12 virtualenv with the dev dependencies
	python3.12 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt

ingest:   ## crawl the live manual into content/, then index it
	$(PY) -m scripts.ingest

index:    ## index the committed content/ (no network)
	$(PY) -m scripts.ingest --offline

test:
	$(PY) -m pytest -q

eval:     ## golden questions through Claude (~$1)
	$(PY) -m scripts.eval

run: index  ## http://localhost:8000 with reload
	$(PY) -m uvicorn --factory app.main:create_app --reload

image:    ## build the Docker image
	docker build -t $(IMAGE) .

up:       ## build and run with Docker Compose
	docker compose up -d --build
