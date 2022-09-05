install-poetry:
	@echo "Install poetry";\
	if [ `command -v brew` ];\
		then brew install poetry;\
	else\
		curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - ;\
	fi;\

all: init format lint

init:
	@echo "Construct Development Environment";\
	if [ -z $(VIRTUAL_ENV) ]; then echo Warning, Virtual Environment is required; fi;\
	if [ -z `command -v poetry` ];\
		then make install-poetry;\
	fi;\
	pip install -U pip
	poetry install
	pre-commit install

format:
	poetry run black .
	poetry run isort .

publish:
	poetry export --dev -f requirements.txt --output requirements.txt --without-hashes
