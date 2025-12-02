# Standard Library

Working with Python's built-in modules and libraries. This section covers the powerful standard library that comes with Python.

## 📂 Contents

### [DateTime](./datetime/)
Date and time operations, formatting, and calculations.

- **datetime_usage.py** - Creating date, time, and datetime objects; accessing components
- **datetime_formatting.py** - Formatting dates with strftime()
- **datetime_calc.py** - Date arithmetic and timedelta
- **dateReformat.py** - Converting between date formats
- **updateProduce.py** - Practical example with date updates
- **tuple_update_workaround.py** - Working with immutable date tuples

**Common Operations:**
- Creating dates: `date.today()`, `datetime.now()`
- Formatting: `strftime()`, `strptime()`
- Arithmetic: `timedelta` for date differences
- Components: `.year`, `.month`, `.day`, `.hour`, `.minute`

**Key Concepts:** date, time, datetime, timedelta, formatting, parsing

---

### [JSON](./json/)
JSON parsing, serialization, and file operations.

- **python_json_module.py** - Complete JSON guide:
  - Parsing JSON strings with `json.loads()`
  - Converting Python objects to JSON with `json.dumps()`
  - Handling all JSON data types
  - Pretty printing with indent and sort_keys
- **json_manipulation.py** - JSON data manipulation
- **jsonoutput.json** - Sample JSON file

**Python ↔ JSON Type Mapping:**
- dict ↔ object
- list/tuple ↔ array
- str ↔ string
- int/float ↔ number
- True/False ↔ true/false
- None ↔ null

**Key Concepts:** json.loads(), json.dumps(), serialization, deserialization

---

### [Regular Expressions](./regex/)
Pattern matching and text processing with regex.

- Regex patterns and syntax
- Matching, searching, replacing
- Groups and capturing
- Common regex patterns

**Common Patterns:**
- Email validation
- Phone number extraction
- URL parsing
- Text cleaning

**Key Concepts:** re module, patterns, match(), search(), findall(), sub()

---

### [Itertools](./itertools/)
Iterator building blocks for efficient looping.

- Infinite iterators: count(), cycle(), repeat()
- Combinatoric iterators: combinations(), permutations()
- Terminating iterators: chain(), compress(), zip_longest()
- Efficient iteration patterns

**Key Concepts:** Lazy evaluation, memory efficiency, functional iteration

---

### [Standard Library](./standard_library/)
Other useful standard library modules.

- Various built-in modules
- System operations
- File operations
- Utility functions

**Common Modules:**
- os, sys, pathlib
- collections
- math, random
- subprocess
- logging

---

### [Modules](./modules/)
Module creation, imports, and packages.

- **func_module.py** - Creating a module
- **imported_func_module.py** - Importing from modules
- Module search path
- __name__ == "__main__" pattern
- Package structure

**Import Patterns:**
```python
import module
from module import function
from module import *
import module as alias
from package import module
```

**Key Concepts:** import, from, __init__.py, packages, namespaces

---

### [URL Manipulation](./url_manipulation/)
URL parsing, construction, and encoding.

- URL parsing with urllib.parse
- Building URLs
- URL encoding/decoding
- Query string handling

**Common Operations:**
- Parse URLs into components
- Join URL parts
- Encode special characters
- Extract query parameters

**Key Concepts:** urlparse(), urljoin(), quote(), unquote()

---

## 🎯 Learning Path

1. **Modules** - Understand import system first
2. **DateTime** - Essential for most applications
3. **JSON** - Data interchange standard
4. **Regular Expressions** - Powerful text processing
5. **Itertools** - Efficient iteration patterns
6. **URL Manipulation** - Web development essential

## 💡 Tips

### DateTime
- Always use `datetime.now()` for current time, not manual creation
- Use `strptime()` to parse strings into datetime objects
- Use `timedelta` for date arithmetic
- Store dates in UTC, convert to local for display

### JSON
- Use `indent=4` for readable JSON output
- `json.loads()` for strings, `json.load()` for files
- Handle JSONDecodeError for invalid JSON
- Custom serialization with default parameter

### Regex
- Test regex patterns at regex101.com
- Use raw strings: `r"\d+"` to avoid escaping
- Compile patterns for reuse: `pattern = re.compile(r"...")`
- Use named groups for readability

### Modules
- One module per major functionality
- Use `__all__` to control what's exported
- Avoid circular imports
- Use relative imports within packages

## 📚 Essential Modules Reference

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| **datetime** | Date/time handling | now(), strftime(), timedelta() |
| **json** | JSON processing | loads(), dumps(), load(), dump() |
| **re** | Regular expressions | match(), search(), findall(), sub() |
| **itertools** | Iterator tools | combinations(), permutations(), chain() |
| **os** | OS interface | listdir(), path.join(), environ |
| **sys** | System specific | argv, exit(), path |
| **pathlib** | Path handling | Path(), exists(), mkdir() |
| **collections** | Container types | Counter, defaultdict, namedtuple |
| **urllib.parse** | URL handling | urlparse(), urljoin(), quote() |
