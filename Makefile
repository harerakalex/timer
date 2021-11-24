PYTHON ?= python

POETRY := poetry run

line-length := 88

.PHONY: help
help:
	@echo "Makefile for Timer"
		@echo
		@echo "Usage: "
		@echo "		make test		- Run test and produce coverage report"
		@echo "		make lint		- Run flake8 for linting purpose"
		@echo "		make black		- Format codebase"
		@echo "		make isort		- Foramt and arrange imports"
		@echo "		make typing		- Run type checker"

.PHONY: test
test: lint typing
	$(POETRY) coverage run -m pytest tests/
	$(POETRY) coverage report -m

.PHONY: typing
typing:
	$(POETRY) mypy .

.PHONY: lint
lint:
	$(POETRY) flake8 .

.PHONY: black
black: lint
	$(POETRY) black --line-length=${line-length} .

.PHONY: isort
isort: lint
	$(POETRY) isort --line-length=${line-length} .

.PHONY: test-only
test-only:
	$(POETRY) coverage run -m pytest tests/
