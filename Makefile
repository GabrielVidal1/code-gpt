# Define the directory paths
SRC_DIR := src
TEST_DIR := $(SRC_DIR)/tests

# Specify the Python version
PYTHON := python3

# Set the PYTHONPATH environment variable to include the source directory
export PYTHONPATH := $(SRC_DIR):$$PYTHONPATH

# Run all tests
.PHONY: tests
tests:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

up:
	$(PYTHON) -m fastapi_cli dev src/__init__.py --reload