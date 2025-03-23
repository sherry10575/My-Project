SHELL=/bin/bash

VENV=.venv

setup:
	python3 -m venv $(VENV)
	source $(VENV)/bin/activate && pip install -r requirements.txt

run:
	source $(VENV)/bin/activate && python app.py

clean:
	rm -rf $(VENV) __pycache__
	py3clean .
