# File and Data

File handling, data processing, and database operations. This section covers reading/writing files, working with CSV, databases, and data analysis with pandas.

## 📂 Contents

### [File Manipulation](./file_manipulation/)
Reading, writing, and manipulating files.

- **reading_files_example.py** - Reading text files with proper error handling
- **file_handling_example.py** - File operations (open, read, write, close)
- **reading_writing_files.py** - Combined read/write operations
- **file_copying_example.py** - Copying files
- **files.py** - Various file operations

**File Modes:**
- `'r'` - Read (default)
- `'w'` - Write (overwrites)
- `'a'` - Append
- `'r+'` - Read and write
- `'b'` - Binary mode

**Best Practices:**
```python
# Always use context manager (with statement)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed
```

**Key Concepts:** open(), read(), write(), close(), context managers, file modes

---

### [CSV Operations](./csvprog/)
Working with CSV (Comma-Separated Values) files.

- **csv_prog.py** - CSV processing program
- **csv_reader.py** - Reading CSV files
- **README.md** - CSV module documentation

**Common Operations:**
- Reading CSV: `csv.reader()`, `csv.DictReader()`
- Writing CSV: `csv.writer()`, `csv.DictWriter()`
- Handling headers
- Different delimiters

**Example:**
```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

**Key Concepts:** csv module, reader, writer, DictReader, DictWriter

---

### [Database Operations](./db_operations/)
Database connectivity and SQL queries.

- **db_operations_example.py** - SQLite database operations
- Creating tables
- CRUD operations (Create, Read, Update, Delete)
- Query execution
- Connection management

**Common Databases:**
- SQLite (built-in, file-based)
- PostgreSQL (with psycopg2)
- MySQL (with mysql-connector)
- MongoDB (with pymongo)

**Key Concepts:** SQL, connections, cursors, transactions, ORM

---

### [Pandas](./pandas/)
Data analysis and manipulation with pandas library.

#### Data Frame Operations
- **data_frame_iteration/** - Iterating through DataFrames
  - iterrows(), itertuples()
  - Efficient iteration patterns
  - Applying functions to rows/columns

#### Data Manipulation
- **data_manipulation/** - Transforming and cleaning data
  - Filtering, sorting, grouping
  - Handling missing data
  - Merging and joining DataFrames
  - Aggregation operations

#### Projects
- **squirrel_census/** - Analyzing squirrel census data
  - Reading CSV into DataFrame
  - Data cleaning and filtering
  - Aggregation and statistics
  - Data visualization

- **us_states_game/** - Interactive US states quiz
  - DataFrame for state data
  - User input handling
  - Score tracking
  - Data export

**Core Pandas Concepts:**
- Series: 1D labeled array
- DataFrame: 2D labeled table
- Index: Row labels
- Columns: Column labels

**Common Operations:**
```python
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Filter data
filtered = df[df['age'] > 25]

# Group and aggregate
grouped = df.groupby('city')['sales'].sum()

# Save to CSV
df.to_csv('output.csv', index=False)
```

**Key Concepts:** DataFrame, Series, read_csv(), groupby(), merge(), pivot

---

### [OCR](./OCR/)
Optical Character Recognition - extracting text from images.

- OCR with Tesseract
- Image preprocessing
- Text extraction
- Accuracy improvement techniques

**Key Concepts:** pytesseract, image processing, text recognition

---

## 🎯 Learning Path

1. **File Manipulation** - Start with basic file I/O
2. **CSV Operations** - Structured data handling
3. **Database Operations** - Persistent data storage
4. **Pandas** - Data analysis and manipulation
5. **OCR** - Advanced: extracting text from images

## 💡 Tips

### File Operations
- Always use `with` statements to ensure files are closed
- Handle exceptions (FileNotFoundError, PermissionError)
- Use pathlib for cross-platform path handling
- Read large files line-by-line to save memory

### CSV
- Use DictReader/DictWriter for better readability
- Specify encoding for non-ASCII data: `encoding='utf-8'`
- Handle different delimiters (comma, tab, semicolon)
- Use pandas for complex CSV operations

### Databases
- Use parameterized queries to prevent SQL injection
- Always close connections and cursors
- Use transactions for data consistency
- Consider using an ORM (SQLAlchemy) for complex apps

### Pandas
- Vectorized operations are faster than loops
- Use `read_csv()` parameters for efficiency (usecols, nrows)
- Chain operations for cleaner code
- Use `inplace=False` (default) to avoid modifying original data
- Check dtypes after reading data
- Handle missing values explicitly (dropna(), fillna())

## 📊 Data Processing Comparison

| Tool | Best For | Performance | Complexity |
|------|----------|-------------|------------|
| **Built-in file I/O** | Simple text files | Fast | Low |
| **csv module** | Structured CSV data | Fast | Low |
| **sqlite3** | Local databases | Medium | Medium |
| **pandas** | Data analysis | Very fast (vectorized) | Medium |
| **OCR** | Image text extraction | Slow | High |

## ⚡ Performance Tips

### Reading Large Files
```python
# Bad: Loads entire file into memory
with open('large_file.txt') as f:
    content = f.read()

# Good: Process line by line
with open('large_file.txt') as f:
    for line in f:
        process(line)
```

### Pandas Optimization
```python
# Use efficient dtypes
df = pd.read_csv('data.csv', dtype={'id': 'int32'})

# Read only needed columns
df = pd.read_csv('data.csv', usecols=['name', 'age'])

# Use chunksize for large files
for chunk in pd.read_csv('huge.csv', chunksize=10000):
    process(chunk)
```
