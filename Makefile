init:
	pip install -U pip
	pip install pdm
	pdm install
	pdm run pre-commit install

format:
	pdm run black .
	pdm run isort .
