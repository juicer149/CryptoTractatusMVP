PYTHON := python3

.PHONY: help compile test check

help:
	@echo "CryptoTractatusMVP commands"
	@echo ""
	@echo "  make compile   Compile Python files"
	@echo "  make test      Run unit tests"
	@echo "  make check     Run compile + tests"

compile:
	$(PYTHON) -m compileall -q cipher cli language utils tests

test:
	$(PYTHON) -m unittest discover -v

check: compile test
