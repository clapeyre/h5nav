init:
	pandoc -o README.rst README.md

req: init
	pip install -r requirements.txt

develop: init
	pip install -e .[dev]

install: req
	python setup.py install

uninstall:
	pip uninstall h5nav
	\rm -rf h5nav.egg-info/

test: req
	pytest --cov=h5nav tests

dummy:
	python -c "import tests.test_cli as tc; tc.setup_module()"

wheel: init
	rm -r dist
	python setup.py bdist_wheel

upload: wheel
	twine upload dist/*

.PHONY: test
