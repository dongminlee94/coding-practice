format:
		black . --line-length 104
		isort .

setup:
		pip install -r requirements.txt
		pre-commit install