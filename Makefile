SHELL=/bin/bash

VENV=.venv

setup:
    python -m venv build_env
    call .git/hooks/post-commit.bat


run:
	source $(VENV)/bin/activate && python app.py

clean:
	rm -rf $(VENV) __pycache__
	py3clean .
