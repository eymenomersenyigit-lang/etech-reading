# eTech Reading - Terminal Commands Reference

## 🖥️ 10 Essential Terminal Commands

### 1. Install the Package

```bash
# Basic installation
pip install etech-reading

# Install with development tools
pip install etech-reading[dev]

# Install from local wheel
pip install dist/etech_reading-1.0.0-py3-none-any.whl
```

**Use Case:** Get eTech Reading installed on your system quickly.

---

### 2. Launch the Application

```bash
# Run the GUI application
etech-reading

# Run with Python module
python -m etech_reading.reader

# Run in background (Linux/Mac)
nohup etech-reading &

# Run with specific Python interpreter
python3.10 -m etech_reading.reader
```

**Use Case:** Start the RSVP reader from command line for quick reading sessions.

---

### 3. Analyze Text from Command Line

```bash
# Simple one-liner (works on all platforms)
python -c "from etech_reading import TextAnalyzer; text = 'Hello world. This is amazing!'; analysis = TextAnalyzer.analyze_text(text); print('Words:', sum(s['word_count'] for s in analysis))"

# Windows PowerShell version (with f-string)
python -c "from etech_reading import TextAnalyzer; text = 'Hello world. This is amazing!'; analysis = TextAnalyzer.analyze_text(text); wc = sum(s['word_count'] for s in analysis); print(f'Words: {wc}')"

# Recommended: Save as script for better readability
cat > analyze_text.py << 'EOF'
from etech_reading import TextAnalyzer

text = 'Hello world. This is amazing!'
analysis = TextAnalyzer.analyze_text(text)
word_count = sum(s['word_count'] for s in analysis)

print(f'Words: {word_count}')
for sentence in analysis:
    print(f"  Sentence: {sentence['original_sentence']}")
    print(f"  Words: {sentence['word_count']}")
EOF

# Then run: python analyze_text.py
```

**Use Case:** Analyze text files without opening the GUI. Useful for batch processing documents, content analysis, and integration with scripts.

---

### 4. Check Package Information

```bash
# View installed package details
pip show etech-reading

# Check package version
python -c "import etech_reading; print(etech_reading.__version__)"

# List all exports
python -c "import etech_reading; print(dir(etech_reading))"

# Verify installation
python -c "from etech_reading import RSVPReader, TextAnalyzer; print('Installation OK')"
```

**Use Case:** Verify the package is correctly installed and working.

---

### 5. Run Tests

```bash
# Run the included test suite
python test_package.py

# Run with pytest (if installed)
pytest test_package.py -v

# Run with coverage report
pytest --cov=etech_reading test_package.py
```

**Use Case:** Verify all functionality works correctly after updates.

---

### 6. Build Distribution Packages

```bash
# Build both wheel and source distributions
python -m build

# Build only wheel
python -m build --wheel

# Build only source distribution
python -m build --sdist

# View generated distributions
ls -lh dist/
```

**Use Case:** Create distribution files for sharing or publishing.

---

### 7. Publish to PyPI

```bash
# Check distribution files before upload
twine check dist/*

# Upload to PyPI
twine upload dist/*

# Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# Upload specific file
twine upload dist/etech_reading-1.0.0-py3-none-any.whl
```

**Use Case:** Share your package with the world on PyPI.

---

### 8. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate

# Install package in virtual environment
pip install etech-reading
```

**Use Case:** Isolate your development environment.

---

### 9. Use as Python Library

```bash
# Import in Python script
python << 'EOF'
from etech_reading import TextAnalyzer, RSVPReader

# Analyze text
text = "Your text here..."
result = TextAnalyzer.analyze_text(text)

# Use in your application
for sentence in result:
    print(f"Sentence: {sentence['original_sentence']}")
    print(f"Words: {sentence['word_count']}")
EOF
```

**Use Case:** Integrate RSVP analysis into your own Python projects.

---

### 10. Uninstall and Clean Up

```bash
# Uninstall the package
pip uninstall etech-reading

# Uninstall with dependencies
pip uninstall etech-reading PyQt5 PyQtWebEngine

# Clean build artifacts
rm -r dist/ build/ etech_reading.egg-info

# Clean Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

**Use Case:** Remove the package or clean up development files.

---

## 🎯 Usage Scenarios

### Scenario 1: Individual Reading Enhancement

```bash
# Install and use for personal reading
pip install etech-reading
etech-reading

# Paste your article or book text
# Adjust speed from 50-1000 WPM
# Press Space to play/pause
# Press Esc to stop
```

**Benefits:**
- ⚡ Read 2-3x faster
- 👁️ Reduce eye strain
- 🎯 Improve focus
- 📚 Learn more in less time

---

### Scenario 2: Educational Institution

```bash
# Install for all students
pip install etech-reading

# Create a launcher script for students
cat > /usr/local/bin/etech-reading-edu << 'EOF'
#!/bin/bash
# Educational version with preset settings
python -m etech_reading.reader &
EOF

chmod +x /usr/local/bin/etech-reading-edu

# Make available for all users
etech-reading-edu
```

**Benefits:**
- 🎓 Teach faster reading techniques
- 📈 Improve student comprehension
- ⏱️ Track reading statistics
- 🔧 Customizable for different subjects

---

### Scenario 3: Corporate Training

```bash
# Install for employee training
pip install etech-reading

# Create training material analyzer
python << 'EOF'
from etech_reading import TextAnalyzer

# Analyze training documents
documents = [
    "Document 1 content...",
    "Document 2 content...",
    "Document 3 content..."
]

for doc in documents:
    analysis = TextAnalyzer.analyze_text(doc)
    word_count = sum(s["word_count"] for s in analysis)
    print(f"Document has {word_count} words")
    print(f"Est. reading time at 300 WPM: {word_count/300:.1f} minutes")
EOF
```

**Benefits:**
- 📊 Faster employee onboarding
- ⚙️ Optimize training time
- 💼 Increase productivity
- 🎯 Better information retention

---

### Scenario 4: Content Creator

```bash
# Install for content optimization
pip install etech-reading

# Analyze your blog posts/articles
python << 'EOF'
from etech_reading import TextAnalyzer
import os

# Analyze all .txt files
for file in os.listdir('articles'):
    if file.endswith('.txt'):
        with open(f'articles/{file}') as f:
            content = f.read()
        
        analysis = TextAnalyzer.analyze_text(content)
        words = sum(s["word_count"] for s in analysis)
        
        print(f"{file}: {words} words")
        print(f"Reading time: {words/200:.1f} min (avg reader)")
        print(f"Speed reading: {words/500:.1f} min (trained reader)\n")
EOF
```

**Benefits:**
- 📝 Estimate reading time
- ✍️ Optimize article length
- 📊 Analyze content metrics
- 🎯 Improve user engagement

---

### Scenario 5: Language Learning

```bash
# Install for language learners
pip install etech-reading

# Create a language learning mode
cat > learn_language.py << 'EOF'
from etech_reading import TextAnalyzer, RSVPReader
from PyQt5.QtWidgets import QApplication
import sys

# Load language-specific texts
language_texts = {
    "english": "English text samples...",
    "spanish": "Spanish text samples...",
    "french": "French text samples..."
}

# Launch reader with specific language
if len(sys.argv) > 1:
    language = sys.argv[1]
    if language in language_texts:
        app = QApplication(sys.argv)
        reader = RSVPReader()
        reader.text_input.setPlainText(language_texts[language])
        reader.show()
        sys.exit(app.exec_())
EOF

# Run: python learn_language.py english
```

**Benefits:**
- 🌍 Learn multiple languages
- 🎯 Improve reading speed in foreign languages
- 📖 Practice with native texts
- 💡 Better comprehension

---

## 🛠️ Advanced Commands

### Monitor Performance

```bash
# Track import time
time python -c "import etech_reading"

# Profile memory usage
python -m memory_profiler etech_reading.reader

# Check for issues
pip audit
```

### Batch Processing

```bash
# Process multiple files
for file in *.txt; do
    python -c "
from etech_reading import TextAnalyzer
with open('$file') as f:
    text = f.read()
analysis = TextAnalyzer.analyze_text(text)
print(f'$file: {sum(s[\"word_count\"] for s in analysis)} words')
"
done
```

### Docker Usage

```bash
# Run in Docker container
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  etech-reading

# Or with script
docker run -it --rm etech-reading python -c "
from etech_reading import TextAnalyzer
analysis = TextAnalyzer.analyze_text('Sample text')
print('OK')
"
```

---

## 📝 Command Cheat Sheet

| Command | Purpose |
|---------|---------|
| `pip install etech-reading` | Install package |
| `etech-reading` | Launch GUI |
| `pip show etech-reading` | Show info |
| `python test_package.py` | Run tests |
| `python -m build` | Build distributions |
| `twine upload dist/*` | Publish to PyPI |
| `pip uninstall etech-reading` | Uninstall |
| `python -c "from etech_reading import ..."` | Use as library |
| `source venv/bin/activate` | Activate venv |
| `python -m etech_reading.reader` | Run module |

---

## 🚀 Quick Start Commands

```bash
# Complete installation and first run (copy & paste)
pip install etech-reading && etech-reading

# Test everything works
pip install etech-reading && python -c "from etech_reading import *; print('Ready!')"

# Development setup
git clone <your-repo> && cd etech-reading && pip install -e . && python test_package.py
```

---

**These 10 commands cover 95% of typical usage scenarios!**

For more advanced usage, check the main README.md documentation.
