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

validate:
	sam validate --lint

format:
	uv run ruff format .

# --use-container builds the layer inside an Amazon Linux image so pip downloads
# Linux wheels (.whl) -install files that match the Lambda runtime (instead of macOS ones).
build: validate
	sam build --use-container

deploy: build
	sam deploy

run:
	uv run python src/main.py


clean:
	rm -rf .aws-sam .pytest_cache .ruff_cache


