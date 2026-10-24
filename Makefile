PY ?= .venv/bin/python

.PHONY: venv ingest index test run

venv:     ## Python 3.12 virtualenv with the dev dependencies
	python3.12 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt

ingest:   ## crawl the live manual into content/, then index it
	$(PY) -m scripts.ingest

index:    ## index the committed content/ (no network)
	$(PY) -m scripts.ingest --offline

test:
	$(PY) -m pytest -q

run: index  ## http://localhost:8000 with reload
	$(PY) -m uvicorn --factory app.main:create_app --reload
