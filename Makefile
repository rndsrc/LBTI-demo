PY ?= .venv/bin/python

.PHONY: venv test run

venv:     ## Python 3.12 virtualenv with the dev dependencies
	python3.12 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt

test:
	$(PY) -m pytest -q

run:      ## http://localhost:8000 with reload
	$(PY) -m uvicorn --factory app.main:create_app --reload
