# eTech Reading - Quick Command Reference

## Installation & Setup

```bash
# Install in development mode
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"

# Install from PyPI (after publishing)
pip install etech-reading

# Upgrade to latest version
pip install --upgrade etech-reading

# Show package information
pip show etech-reading

# Uninstall
pip uninstall etech-reading
```

## Running the Application

```bash
# As command-line tool
etech-reading

# As Python module
python -m etech_reading.reader

# In Python script
python -c "from etech_reading import RSVPReader; RSVPReader()"
```

## Development & Testing

```bash
# Run test suite
python test_package.py

# Run with pytest (if installed)
pytest

# Code formatting with black
black etech_reading/

# Linting with flake8
flake8 etech_reading/

# Type checking with mypy
mypy etech_reading/
```

## Building & Distribution

```bash
# Install build tools
pip install build wheel setuptools twine

# Build distribution packages
python -m build

# List generated distributions
ls dist/

# Clean build artifacts
rm -r dist/ build/ *.egg-info  # Linux/macOS
rmdir /s dist build *.egg-info  # Windows
```

## Publishing to PyPI

```bash
# Install twine (if not already installed)
pip install twine

# Test upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Check upload status
twine check dist/*

# View package on PyPI
# https://pypi.org/project/etech-reading/
```

## Package Information

```bash
# Import and check version
python -c "from etech_reading import __version__; print(__version__)"

# Check all exports
python -c "import etech_reading; print(dir(etech_reading))"

# Test TextAnalyzer
python -c "from etech_reading import TextAnalyzer; print(TextAnalyzer.analyze_text('Hello world'))"

# Test RSVPReader import
python -c "from etech_reading import RSVPReader; print('OK')"
```

## Virtual Environment Management

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Activate (Windows Command Prompt)
venv\Scripts\activate.bat

# Deactivate
deactivate

# Remove virtual environment
rm -r venv  # Linux/macOS
rmdir /s venv  # Windows
```

## Version Management

```bash
# Check current version
python -c "from etech_reading import __version__; print(__version__)"

# Update version (edit setup.py and pyproject.toml)
# Change: version = "1.0.0" to version = "1.0.1"

# Rebuild after version update
python -m build
twine upload dist/*
```

## Troubleshooting

```bash
# Check if module is installed
pip list | grep etech

# Verify installation integrity
python -c "import etech_reading; print('Installation OK')"

# Check dependencies
pip show etech-reading | grep Requires

# Reinstall from scratch
pip uninstall etech-reading
pip install etech-reading

# Force reinstall with no cache
pip install --no-cache-dir --force-reinstall etech-reading

# Check for package conflicts
pip check
```

## File Structure Reference

```bash
# List package contents
ls -la etech_reading/

# List distribution files
ls -lh dist/

# Check MANIFEST
cat MANIFEST.in

# View package metadata
cat setup.py
cat pyproject.toml

# Read documentation
cat README.md
cat INSTALLATION_GUIDE.md
cat PUBLISH_TO_PYPI.md
```

## Interactive Python

```python
# Start Python interactive shell
python

# Inside Python:
from etech_reading import RSVPReader, TextAnalyzer

# Test TextAnalyzer
text = "Hello world. This is a test."
analysis = TextAnalyzer.analyze_text(text)
print(f"Words: {len(analysis[0]['words'])}")

# Test imports
from etech_reading import __version__
print(f"Version: {__version__}")

# Exit
exit()
```

## Continuous Integration Setup

```bash
# Create GitHub Actions workflow
mkdir -p .github/workflows

# Create publish.yml for automatic PyPI uploads
# (See PUBLISH_TO_PYPI.md for workflow code)
```

## Documentation Commands

```bash
# Generate package documentation
pip install sphinx

# Create docs directory
sphinx-quickstart docs

# Build HTML documentation
cd docs
make html
```

## Maintenance

```bash
# Clean temporary files
rm -r __pycache__ etech_reading/__pycache__  # Linux/macOS
rmdir /s __pycache__ etech_reading\__pycache__  # Windows

# Remove egg-info
rm -r etech_reading.egg-info  # Linux/macOS
rmdir /s etech_reading.egg-info  # Windows

# Full cleanup
python setup.py clean --all
```

## Advanced Commands

```bash
# Install with all extras (including dev tools)
pip install -e ".[dev]"

# Install specific version
pip install etech-reading==1.0.0

# Install from git (if on GitHub)
pip install git+https://github.com/yourusername/etech-reading.git

# Install from local wheel
pip install dist/etech_reading-1.0.0-py3-none-any.whl

# Install from local tar.gz
pip install dist/etech_reading-1.0.0.tar.gz

# Create editable install from GitHub
pip install -e git+https://github.com/yourusername/etech-reading.git#egg=etech-reading
```

## Security & Auditing

```bash
# Check for security issues in dependencies
pip install safety
safety check

# Audit installed packages
pip audit

# Generate requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

## Performance Checking

```bash
# Check import time
time python -c "import etech_reading"

# Profile application
python -m cProfile -s cumulative etech_reading.reader

# Memory usage check
pip install memory-profiler
python -m memory_profiler etech_reading.reader
```

## Distribution Testing

```bash
# Extract and test wheel
cd /tmp
unzip -q etech_reading-1.0.0-py3-none-any.whl
ls etech_reading/

# Extract and test source distribution
tar xzf etech_reading-1.0.0.tar.gz
cd etech_reading-1.0.0
pip install -e .
```

---

## Common Scenarios

### Scenario 1: Clean Install from PyPI
```bash
pip uninstall etech-reading
pip install etech-reading
etech-reading
```

### Scenario 2: Development Setup
```bash
git clone <repo>
cd etech-reading
pip install -e ".[dev]"
python test_package.py
```

### Scenario 3: Local Testing
```bash
cd /path/to/etech-reading
pip install -e .
python test_package.py
etech-reading
```

### Scenario 4: Publish New Version
```bash
# Update version in setup.py & pyproject.toml
python -m build
twine upload dist/*
pip install --upgrade etech-reading
```

### Scenario 5: CI/CD Pipeline
```yaml
# GitHub Actions example (in .github/workflows/test.yml)
name: Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -e ".[dev]"
      - run: python test_package.py
```

---

**Tip:** Save this file and bookmark it for quick reference!
