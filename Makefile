format:
	black .
	isort .

init:
	pip install -U pip
	pip install -r requirements.txt
	pre-commit install
