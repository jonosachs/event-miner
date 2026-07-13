.PHONY: install deps test lint validate format build deploy run clean

# Creates/refreshes local venv from uv.lock
install:
	uv sync

deps:
	uv lock
	uv export --no-dev --no-emit-project --no-hashes \
              -o layers/dependencies/requirements.txt

test:
	uv run pytest

test-integration:
	uv run pytest -m integration

lint:
	uv run ruff check .
	uv run ruff format --check .

validate:
	uv run cfn-lint template.yaml

format:
	uv run ruff format .

	
# Use 'sam build --use-container' to build the layer inside an Amazon Linux image 
build: validate
	sam build 

deploy: build
	sam deploy

run:
	uv run python src/main.py


clean:
	rm -rf .aws-sam .pytest_cache .ruff_cache


