# Publishing eTech Reading to PyPI

This guide explains how to publish your eTech Reading package to PyPI.

## Prerequisites

1. PyPI Account: Register at https://pypi.org/account/register/
2. TestPyPI Account: Register at https://test.pypi.org/account/register/

## Step 1: Generate API Tokens

1. Go to your PyPI account settings: https://pypi.org/manage/account/
2. Scroll to "API tokens" section
3. Create a new token named "etech-reading-upload"
4. Copy the token (you'll need it)

## Step 2: Configure Your System

### Option A: Using .pypirc (Recommended)

Create or edit `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
```

### Option B: Using Environment Variables

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR_TOKEN_HERE
```

## Step 3: Install Twine

```bash
pip install twine
```

## Step 4: Update Package Metadata

Before uploading, update the following files:

### setup.py / pyproject.toml
- `version`: Increment version number (1.0.0 → 1.0.1)
- `author`: Your actual name
- `author_email`: Your email
- `url`: Your GitHub repository URL
- `description`: Update if needed

### README.md
- Update all references from "yourusername" to your actual GitHub username
- Verify all URLs are correct

## Step 5: Test on TestPyPI (Recommended)

```bash
twine upload --repository testpypi dist/*
```

This will upload to TestPyPI for testing without affecting the real PyPI.

### Test Installation

```bash
pip install --index-url https://test.pypi.org/simple/ etech-reading
```

## Step 6: Upload to PyPI

Once you've tested successfully:

```bash
twine upload dist/*
```

## Step 7: Verify Installation

Check that your package is available:

```bash
pip install etech-reading
etech-reading
```

Or verify online at: https://pypi.org/project/etech-reading/

## Publishing Updates

For new versions:

1. Update version in setup.py and pyproject.toml
2. Update CHANGELOG/README with changes
3. Clean old distributions: `rm -r dist/ build/`
4. Build new packages: `python -m build`
5. Upload: `twine upload dist/*`

## Version Numbering

Follow Semantic Versioning: MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features (1.0.0 → 1.1.0)
- **PATCH**: Bug fixes (1.0.0 → 1.0.1)

## Current Distribution Files

Located in `dist/` directory:

- `etech_reading-1.0.0-py3-none-any.whl` - Wheel (binary distribution)
- `etech_reading-1.0.0.tar.gz` - Source distribution

## Troubleshooting

### "Invalid token"
- Check your .pypirc file format
- Verify token is correct
- Regenerate token if needed

### "Package already exists"
- Increment version number
- Don't reuse version numbers

### "Invalid package name"
- Package names must be lowercase with hyphens
- Cannot have underscores in the name (converted to hyphens)

## Resources

- PyPI Help: https://pypi.org/help/
- Twine Documentation: https://twine.readthedocs.io/
- Packaging Guide: https://packaging.python.org/
- Setuptools Guide: https://setuptools.readthedocs.io/

## Next Steps After Publishing

1. Create a release on GitHub
2. Add badges to README
3. Update documentation
4. Promote on social media
5. Consider adding CI/CD for automatic uploads

---

Happy publishing! 🎉
