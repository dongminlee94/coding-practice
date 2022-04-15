format:
		black . --line-length 104
		isort .

init:
		pip install -r requirements.txt
		pre-commit install