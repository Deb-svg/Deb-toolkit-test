# Makefile for Deb Toolkit

.PHONY: all analyze deps build test package deploy docs

# Default target to run all tasks
all: analyze deps build test docs package

# Run code analysis
analyze:
	@echo "Running code analyzer..."
	python toolsrc/scripts/code_analyzer.py

# Manage dependencies
deps:
	@echo "Managing dependencies..."
	pip install -r requirements.txt

# Build the project
build:
	@echo "Building project..."
	python toolsrc/scripts/build_automation.py

# Run tests
test:
	@echo "Running tests..."
	pytest

# Package the project
package:
	@echo "Packaging project..."
	python toolsrc/scripts/deploy_package.py

# Deploy the project
deploy:
	@echo "Deploying project..."
	@echo "Usage: make deploy PACKAGE_PATH=path/to/package.tar.gz SERVER_IP=server_ip USERNAME=username PASSWORD=password"
	@echo "Example: make deploy PACKAGE_PATH=path/to/package.tar.gz SERVER_IP=192.168.1.1 USERNAME=user PASSWORD=pass"
	@echo "You need to specify PACKAGE_PATH, SERVER_IP, USERNAME, and PASSWORD as environment variables."

# Generate documentation
docs:
	@echo "Generating documentation..."
	sphinx-build -b html docs/source docs/build

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf toolsrc/scripts/docs/build
	rm -rf *.egg-info
	rm -rf toolsrc/build
	rm -rf toolsrc/dist
