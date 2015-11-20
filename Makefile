#
# Copyright (c) 2010 Juan Palacios juan.palacios.puyana@gmail.com
# Subject to the Lesser GNU Public License - see < http://www.gnu.org/licenses/lgpl.html>
#
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

VENV := test_venv
VENV_BIN := $(VENV)/bin

# simulate running in headless mode
unexport DISPLAY

# Test coverage pass threshold (percent)
MIN_COV ?= 95

FIND_LINT_PY=`find pyhistuples examples -name "*.py" -not -path "*/*test*"`
LINT_PYFILES := $(shell find $(FIND_LINT_PY))

$(VENV):
	virtualenv --system-site-packages $(VENV)
	$(VENV_BIN)/pip install --ignore-installed -r requirements_dev.txt
	$(VENV_BIN)/pip install -e .

run_pep8: $(VENV)
	$(VENV_BIN)/pep8 --config=pep8rc $(LINT_PYFILES) > pep8.txt

run_pylint: $(VENV)
	$(VENV_BIN)/pylint --rcfile=pylintrc --extension-pkg-whitelist=numpy $(LINT_PYFILES) > pylint.txt

run_tests: $(VENV)
	$(VENV_BIN)/nosetests -v --with-coverage --cover-min-percentage=$(MIN_COV) --cover-package pyhistuples

run_tests_xunit: $(VENV)
	@mkdir -p $(ROOT_DIR)/test-reports
	$(VENV_BIN)/nosetests pyhistuples --with-coverage --cover-min-percentage=$(MIN_COV) --cover-inclusive --cover-package=pyhistuples  --with-xunit --xunit-file=test-reports/nosetests_pyhistuples.xml

lint: run_pep8 run_pylint

test: run_tests

doc: $(VENV)
	make SPHINXBUILD=$(ROOT_DIR)/$(VENV_BIN)/sphinx-build -C doc html

doc_pdf: $(VENV)
	make SPHINXBUILD=$(ROOT_DIR)/$(VENV_BIN)/sphinx-build -C doc latexpdf

clean_test_venv:
	@rm -rf $(VENV)
	@rm -rf $(ROOT_DIR)/test-reports

clean_doc:
	@test -x $(ROOT_DIR)/$(VENV_BIN)/sphinx-build && make SPHINXBUILD=$(ROOT_DIR)/$(VENV_BIN)/sphinx-build  -C doc clean || true
	@rm -rf $(ROOT_DIR)/doc/source/_pyhistuples_build

clean: clean_doc clean_test_venv
	@rm -f pep8.txt
	@rm -f pylint.txt
	@rm -rf pyhistuples.egg-info
	@rm -f .coverage
	@rm -rf test-reports
	@rm -rf dist

.PHONY: run_pep8 test clean_test_venv clean doc
