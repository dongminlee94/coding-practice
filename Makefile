all: init format
	echo 'Makefile for the coding-practice repository'

install-poetry:
	@echo "Install poetry";\
	if [ `command -v brew` ];\
		then brew install poetry;\
	else\
		curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.3.2 python3 -;\
	fi;\

init:
	@echo "Construct Development Environment";\
	if [ -z $(VIRTUAL_ENV) ]; then echo Warning, Virtual Environment is required; fi;\
	if [ -z `command -v poetry` ];\
		then make install-poetry;\
	fi;\
	pip install -U pip
	poetry install
	poetry run pre-commit install

format:
	poetry run black .
	poetry run isort .
