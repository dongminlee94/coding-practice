all: init format
	echo 'Makefile for the coding-practice-leetcode repository'

init:
	pip install poetry
	pip install -U pip
	poetry install
	poetry run pre-commit install

format:
	poetry run black .
	poetry run isort .
