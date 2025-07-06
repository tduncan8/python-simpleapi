# Define variables
FLASK_APP = app.py
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
FLASK = $(PYTHON) -m flask

.PHONY: all install run clean

all: install run

install: $(VENV_DIR)
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

$(VENV_DIR):
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)

run:
	@echo "Running Flask application..."
	FLASK_ENV=development $(FLASK) run --debug

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
