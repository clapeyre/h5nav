# Modern Makefile for h5nav using uv

install:
	uv pip install .

develop:
	uv pip install -e ".[dev]"

uninstall:
	uv pip uninstall h5nav
	rm -rf h5nav.egg-info/

test:
	uv run pytest --cov=h5nav tests

build:
	rm -rf dist
	uv build

clean:
	rm -rf dist build *.egg-info .pytest_cache
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

dummy:
	uv run python -c "import tests.test_cli as tc; tc.setup_module()"

.PHONY: install develop uninstall test build clean dummy