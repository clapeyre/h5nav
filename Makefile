req:
	pip install -r requirements.txt

develop:
	pip install -e .[dev]

install: req
	python setup.py install

uninstall:
	pip uninstall h5nav
	\rm -rf h5nav.egg-info/

test:
	pytest --cov=h5nav tests

dummy:
	python -c "import tests.test_cli as tc; tc.setup_module()"

wheel:
	rm -r dist
	python setup.py bdist_wheel

upload_test: test wheel
	twine upload -r test dist/*

upload: wheel
	twine upload dist/*

.PHONY: test
