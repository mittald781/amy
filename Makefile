# How to run Python.
PYTHON = python3

# How to run the management tool.
MANAGE = ${PYTHON} manage.py

# Database used by this application.
APP_DB = db.sqlite3

# Run a SQL query.
QUERY = sqlite3 ${APP_DB}

# Error messages.
E_CERT_PATH = "error: must set CERT_PATH before running command"


all : commands

## commands     : show all commands.
commands : Makefile
	@sed -n 's/^## //p' $<

## test         : run all tests.
test :
	${MANAGE} test

## fast_test    : run all tests really fast.
fast_test:
	${MANAGE} test --keepdb --parallel

## fast_test_fail	: run all tests really fast, fails as soon as any test fails.
fast_test_fail:
	${MANAGE} test --keepdb --parallel --failfast

## dev_database : re-make database using saved data
dev_database :
	@if test  -f ${APP_DB}; \
	then \
		echo "You must remove database file yourself!"; \
		exit 1; \
	fi
	${MANAGE} migrate
	${MANAGE} loaddata amy/autoemails/fixtures/templates_triggers.json
	${MANAGE} fake_database
	${MANAGE} createinitialrevisions
	${MANAGE} create_superuser

## airports     : display YAML for airports
airports :
	@${MANAGE} export_airports

## check-certs  : check that all instructor certificates have been set (must set CERT_PATH to run)
check-certs :
	@if [ -z "${CERT_PATH}" ]; then echo ${E_CERT_PATH}; else ${MANAGE} check_certificates ${CERT_PATH}; fi

## schema       : display the database schema
schema :
	${QUERY} .schema

## node_modules : install front-end dependencies using Yarn
node_modules : package.json
	yarn install --frozen-lockfile
	touch node_modules

## serve        : run a server
serve : node_modules
	${MANAGE} runserver

## serve_now    : run a server now
serve_now :
	${MANAGE} runserver

## outdated     : show outdated dependencies
outdated :
	-pip list --outdated
	-yarn outdated

## upgrade      : force package upgrade using pip
upgrade :
	pip install --upgrade -r requirements.txt
	yarn upgrade --frozen-lockfile

## clean        : clean up.
clean :
	rm -rf \
		$$(find . -name '*~' -print) \
		$$(find . -name '*.pyc' -print) \
		$$(find . -name '__pycache__' -print) \
		htmlerror \
		$$(find . -name 'test_db*.sqlite3*' -print) \

## coverage     : run tests and generate HTML coverage
coverage :
	coverage --source=amy manage.py test
	coverage html

## bumpversion  : bump version strings in various files, expected envvars CURRENT, NEXT
bumpversion :
	@if [ "${CURRENT}" -a "$(NEXT)" ]; \
	then \
		echo "Bumping version $(CURRENT) to $(NEXT)"; \
		sed -i "s/$(CURRENT)/$(NEXT)/" amy/workshops/__init__.py ; \
		sed -i "s/$(CURRENT)/$(NEXT)/" package.json ; \
	fi

## build_docs      : build static docs in `site`
build_docs :
	mkdocs build

## serve_docs      : serve docs at `localhost:8000`
serve_docs :
	mkdocs serve
