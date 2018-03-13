init:
	pip install -r requirements.txt

develop:
	python setup.py develop

install:
	python setup.py install

uninstall:
	pip uninstall h5nav
	\rm -rf h5nav.egg-info/

test: init
	pytest --cov=h5nav tests

dummy:
	python -c "import tests.test_cli as tc; tc.setup_module()"

wheel:
	python setup.py bdist_wheel

upload: wheel
	twine upload dist/*

.PHONY: test
