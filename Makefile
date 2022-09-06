all: init format lint

init:
	pip install poetry==1.1.15
	pip install -U pip
	poetry install
	pre-commit install

format:
	black .
	isort .

publish:
	poetry export --dev -f requirements.txt --output requirements.txt --without-hashes
