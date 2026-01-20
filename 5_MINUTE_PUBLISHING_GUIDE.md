# eTech Reading - 5-Minute Publishing Guide

## 🚀 Publish to PyPI in 5 Steps

### Step 1: Customize Your Package Metadata (2 minutes)

**Edit `setup.py` (Line ~12-14):**
```python
author="John Doe",                          # Change to YOUR name
author_email="john.doe@example.com",       # Change to YOUR email
url="https://github.com/johndoe/etech-reading",  # Change to YOUR GitHub URL
```

**Edit `pyproject.toml` (Line ~5-6):**
```toml
authors = [
    {name = "John Doe", email = "john.doe@example.com"},  # Update
]
```

**Edit `README.md`:** 
Replace all:
- `yourusername` → your GitHub username
- `Your Name` → your name
- `your.email@example.com` → your email

### Step 2: Install Twine (1 minute)

```bash
pip install twine
```

### Step 3: Create PyPI Account (1 minute)

1. Go to: https://pypi.org/account/register/
2. Create account
3. Go to: https://pypi.org/manage/account/
4. Scroll to "API tokens"
5. Create new token
6. Copy token (keep it safe!)

### Step 4: Configure Credentials (30 seconds)

Create `~/.pypirc` file:

**Windows:** `C:\Users\YourUsername\.pypirc`
**Linux/Mac:** `~/.pypirc`

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE
```

### Step 5: Upload to PyPI (30 seconds)

```bash
cd c:\Users\XYZ\Desktop\cp
twine upload dist/*
```

**That's it!** 🎉

Your package is now on PyPI!

---

## ✅ Verify Installation

Test your published package:

```bash
# Open new terminal/PowerShell
pip install etech-reading

# Run it
etech-reading
```

---

## 🔗 Your Package is Live!

Once published, your package will be at:
```
https://pypi.org/project/etech-reading/
```

Share this link with users!

---

## 📝 For Future Updates

To publish a new version (e.g., 1.0.1):

1. Update version in setup.py and pyproject.toml
2. Run: `python -m build`
3. Run: `twine upload dist/*`

Done! Users can update with: `pip install --upgrade etech-reading`

---

## 🆘 Troubleshooting

### "Invalid token"
- Check PyPI website for your token
- Make sure token starts with `pypi-`
- Regenerate token if needed

### "Package already exists"
- Change version number first
- Example: 1.0.0 → 1.0.1

### "Cannot import twine"
```bash
pip install twine --upgrade
```

### "No distributions found"
```bash
python -m build
```

---

## 💡 Pro Tips

1. **Test First (Optional but Recommended)**
   ```bash
   twine upload --repository testpypi dist/*
   pip install --index-url https://test.pypi.org/simple/ etech-reading
   ```

2. **Check Your Upload**
   ```bash
   twine check dist/*
   ```

3. **Get Help**
   ```bash
   twine --help
   twine upload --help
   ```

---

**You're ready to publish!** 🚀

Next command: `twine upload dist/*`
