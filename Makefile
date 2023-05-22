.ONESHELL:

SHELL	= /bin/bash
VENV	= .venv

run:
	@python3 srcs/main.py

venv: ${VENV}
	@printf "Update virtual environment ... "
	@pip install --upgrade pip >/dev/null 2>&1 
	@${VENV}/bin/pip install -r requirements.txt > /dev/null 2>&1
	@printf "done\n"
	
${VENV}:
	@printf "Create virtual environment... "
	@python3 -m venv ${VENV}
	@printf "done\n"

freeze:
	@printf "Update requirements.txt ... "
	@pip freeze > requirements.txt
	@printf "done\n"

activate: ${VENV}
	@printf "Activate virtual environment... "
	@source ${VENV}/bin/activate
	@printf "done\n"

deactivate:
	@printf "Deactivate virtual environment... "
	@deactivate
	@printf "done\n"

.PHONY: run venv freeze activate deactivate

.NOTPARALLEL: run venv freeze activate deactivate