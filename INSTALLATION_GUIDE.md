# eTech Reading - Installation & Deployment Guide

## Package Status ✅

Your eTech Reading package is now ready for publishing to PyPI!

### Distribution Files Generated

```
dist/
├── etech_reading-1.0.0-py3-none-any.whl      (11.9 KB)
└── etech_reading-1.0.0.tar.gz                (14.8 KB)
```

### Package Structure

```
etech_reading/
├── __init__.py              # Package initialization & exports
├── analyzer.py              # TextAnalyzer for text analysis
└── reader.py                # RSVPReader GUI application
```

## Installation Methods

### 1. From PyPI (After Publishing)

```bash
pip install etech-reading
```

### 2. From Local Distribution

```bash
# Wheel installation (recommended)
pip install dist/etech_reading-1.0.0-py3-none-any.whl

# Or from source tarball
pip install dist/etech_reading-1.0.0.tar.gz
```

### 3. From Source (Development Mode)

```bash
cd /path/to/etech-reading
pip install -e .
```

### 4. With Development Dependencies

```bash
pip install -e ".[dev]"
```

## Running the Application

### As Command Line Tool

```bash
etech-reading
```

### From Python Script

```python
from etech_reading import RSVPReader
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
reader = RSVPReader()
reader.show()
sys.exit(app.exec_())
```

### Using TextAnalyzer Only

```python
from etech_reading import TextAnalyzer

text = "Your text here..."
analysis = TextAnalyzer.analyze_text(text)

for sentence in analysis:
    print(f"Sentence: {sentence['original_sentence']}")
    for word in sentence['words']:
        print(f"  - {word['clean']}: {word['focus_letter']}")
```

## System Requirements

- **Python**: 3.7 or higher
- **PyQt5**: >= 5.15.0
- **PyQtWebEngine**: >= 5.15.0
- **OS**: Windows, Linux, macOS

## Platform-Specific Installation

### Windows

```bash
pip install etech-reading
etech-reading
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine
pip install etech-reading
etech-reading
```

### macOS

```bash
pip install etech-reading
etech-reading
```

## Publishing to PyPI

See [PUBLISH_TO_PYPI.md](PUBLISH_TO_PYPI.md) for detailed instructions.

Quick summary:
```bash
# 1. Update version in setup.py and pyproject.toml
# 2. Install twine
pip install twine

# 3. Test on TestPyPI (optional)
twine upload --repository testpypi dist/*

# 4. Upload to PyPI
twine upload dist/*
```

## Environment Setup

### Using venv

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install etech-reading
```

### Using conda

```bash
conda create -n etech python=3.10
conda activate etech
pip install etech-reading
```

### Using pipenv

```bash
pipenv install etech-reading
pipenv run etech-reading
```

## Troubleshooting

### "Module not found" Error

Ensure the package is installed:
```bash
pip list | grep etech-reading
pip install --upgrade etech-reading
```

### PyQt5 Installation Issues

#### Linux:
```bash
sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.qtwebengine
```

#### macOS:
```bash
brew install pyqt5
```

### Application Won't Start

Check dependencies:
```bash
python -c "import etech_reading; print('OK')"
python -c "from PyQt5 import QtWidgets; print('OK')"
```

## Uninstallation

```bash
pip uninstall etech-reading
```

## Updating to New Version

```bash
pip install --upgrade etech-reading
```

## Building from Source

### Install Build Tools

```bash
pip install build wheel setuptools
```

### Build Distribution Packages

```bash
python -m build
```

This creates:
- `dist/etech_reading-1.0.0.tar.gz` (source distribution)
- `dist/etech_reading-1.0.0-py3-none-any.whl` (wheel)

## Testing

```bash
# Run included test suite
python test_package.py

# Or with pytest (if installed)
pytest
```

## Environment Variables

### Custom Configuration (Future)

```bash
export ETECH_FONT_SIZE=56
export ETECH_DEFAULT_WPM=400
etech-reading
```

## Package Information

```bash
pip show etech-reading
```

Output:
```
Name: etech-reading
Version: 1.0.0
Summary: Fast Reading System using RSVP Technology
Author: Your Name
Author-email: your.email@example.com
License: MIT
Location: /path/to/site-packages/etech_reading
Requires: PyQt5, PyQtWebEngine
```

## Integration with Other Tools

### As a Library in Your Project

```python
# requirements.txt
etech-reading>=1.0.0

# Install with
pip install -r requirements.txt
```

### Docker

```dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qtwebengine

RUN pip install etech-reading

ENTRYPOINT ["etech-reading"]
```

```bash
docker build -t etech-reading .
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix etech-reading
```

## Virtual Environment Recommendations

### Development Setup

```bash
# Create virtual environment
python -m venv venv_dev

# Activate
source venv_dev/bin/activate  # Linux/macOS
# or
venv_dev\Scripts\activate  # Windows

# Install in development mode
pip install -e ".[dev]"

# Install development tools
pip install pytest black flake8 mypy
```

### Production Setup

```bash
# Create virtual environment
python -m venv venv_prod

# Activate
source venv_prod/bin/activate

# Install package
pip install etech-reading
```

## Uninstalling Development Environment

```bash
deactivate
rm -rf venv_dev  # Linux/macOS
# or
rmdir /s venv_dev  # Windows
```

## Version Management

Current version: **1.0.0**

To check version in code:
```python
from etech_reading import __version__
print(__version__)
```

## Migration from Old Installation

If upgrading from the standalone `fastread.py`:

```bash
# Remove old version
rm fastread.py

# Install new package version
pip install etech-reading

# Update imports in your code:
# Old: import fastread
# New: from etech_reading import RSVPReader
```

---

For more information, see [README.md](README.md) and [PUBLISH_TO_PYPI.md](PUBLISH_TO_PYPI.md)
