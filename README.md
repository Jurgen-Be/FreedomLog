# FreedomLog

A lightweight and flexible logging module built on [Loguru](https://github.com/Delgan/loguru), designed to provide clean and maintainable log handling with minimal setup.

---

## 📦 Features

- ✅ Simple API: `FreedomLog.info(...)`, `FreedomLog.error(...)`, etc.
- ✅ Centralized configuration via `FreedomLog.init(...)`
- ✅ File logging with automatic rotation and retention
- ✅ Console logging (optional)
- ✅ Predefined formatting styles (selectable via `format_option`)
- ✅ Object-oriented implementation hidden behind a clean module-level interface
- ✅ Safe to import and use across multiple modules after initialization

---

## ⚙️ Installation

To use `FreedomLog` as a module in your project:

### Clone and use directly:

```bash
git clone https://github.com/Jurgen-Be/FreedomLog.git
```

### With pip install:
```bash
pip install https://github.com/Jurgen-Be/FreedomLog/releases/download/V1.0.0/freedomlog-1.0.0-py3-none-any.whl
```
---
## 🚀 Usage

### 1. Initialization (required once, typically in `main.py`)

```python
import FreedomLog

FreedomLog.init(
    path="logs",
    filename="application",
    max_size="10 MB",
    backups=5,
    console=True,
    format_option=2
)
```

### 2. Logging anywhere in your codebase

```python
import FreedomLog

FreedomLog.info("Application started")
FreedomLog.warning("This is a warning")
FreedomLog.error("Something went wrong")
FreedomLog.success("Task completed successfully")
```

After initialization, the logger is globally available — no need to reconfigure or import Loguru directly.

---

## 🔣 Format Options

Pass `format_option` during initialization to choose log formatting:

| Option | Format Description                            | Example Output                                      |
|--------|------------------------------------------------|-----------------------------------------------------|
| 1      | Basic timestamp and level                      | `2025-07-26 14:12:02 | INFO | Message here`         |
| 2      | Includes file, function, and line              | `2025-07-26 14:12:02 | INFO | [main.py:foo:23] ...` |
| 3      | JSON-style for log parsing or external tools   | `{"time": "...", "level": "...", "message": "..."}` |

---

## 🧩 Module Structure

```text
FreedomLog/
├── FreedomLog.py            # Main module with logging implementation
├── __version__.py      # Version string (optional)
├── README.md           # This file
└── pyproject.toml
```

## 📄 License

MIT — free to use, modify, and distribute

---

## 👤 Author

**Bergmans Jurgen**  
Belgium  
Crafted for clarity, reusability, and control.
```

---