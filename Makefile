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
	pytest tests

.PHONY: init test
