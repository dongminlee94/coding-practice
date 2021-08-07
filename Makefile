format:
		black .
		isort .

setup:
		pip install -r requirements.txt
		pre-commit install