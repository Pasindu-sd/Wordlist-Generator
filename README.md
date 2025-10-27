# Wordlist Generator

A powerful, customizable, and efficient wordlist generator tool written in [Python/Java/C++/etc.]. This tool creates comprehensive wordlists for security testing, password recovery, data analysis, and linguistic research.

## Features

### Core Functionality

- **Multiple Generation Modes**: Create wordlists using combinations, permutations, or rule-based patterns
- **Custom Character Sets**: Define your own character sets, including lowercase, uppercase, numbers, and special characters
- **Pattern Support**: Generate words based on specific patterns (e.g., "abc123", "word##")
- **Dictionary Attack Mode**: Combine base words with common prefixes/suffixes and leet speak variations

### Advanced Options

- **Length Control**: Specify minimum and maximum word length
- **Custom Rules**: Apply transformation rules (capitalization, leet speak, etc.)
- **Input Word Integration**: Use existing dictionaries as base words
- **Smart Filtering**: Exclude or include specific patterns
- **Progress Tracking**: Real-time progress indicator for large generations

### Performance & Usability

- **Memory Efficient**: Stream-based generation for handling large wordlists
- **Multi-threading Support**: Utilize multiple CPU cores for faster generation
- **CLI & GUI Interfaces**: Command-line for automation and GUI for easy use
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Method 1: Install from PyPI (if published)

```bash
pip install wordlist-generator
```

---

### Example:

```
RandWordlistGen - Random Password Wordlist Generator
Enter password length (e.g., 8): 3
How many passwords to generate (e.g., 1000): 100
Output filename (default = generated_wordlist.txt): sample.txt

Wordlist saved as 'sample.txt'
Total passwords generated: 100
Password length: 3 characters

```

---
