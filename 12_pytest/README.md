# 12. Pytest

**Location:** [`12_pytest/`](.)

A progressive introduction to testing Python code with [pytest](https://docs.pytest.org/), organised from beginner to advanced concepts. Each test file builds on the previous one, introducing new pytest features alongside a small set of source modules that serve as the subjects under test.

---

## Directory Structure

```
12_pytest/
├── requirements.txt          # pytest, requests and supporting packages
├── source/                   # Source modules being tested
│   ├── __init__.py
│   ├── my_functions.py       # Basic arithmetic functions
│   ├── shapes.py             # OOP shape classes (Circle, Rectangle, Square)
│   └── service.py            # Service layer with an external HTTP call
└── tests/                    # Test suite
    ├── __init__.py
    ├── conftest.py            # Shared fixtures
    ├── test_my_functions.py  # Beginner – basic assertions and markers
    ├── test_circle.py        # Intermediate – class-based tests with setup/teardown
    ├── test_rectangle.py     # Intermediate – function fixtures from conftest
    ├── test_square.py        # Intermediate/Advanced – parametrized tests
    └── test_service.py       # Advanced – mocking external dependencies
```

---

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests from the 12_pytest/ directory
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run a specific test file
pytest tests/test_my_functions.py -v

# Run only tests marked as slow
pytest tests/ -v -m slow
```

---

## Sections (Beginner → Advanced)

### 1. Basic Assertions and Test Functions

**Source:** [`source/my_functions.py`](source/my_functions.py)  
**Tests:** [`tests/test_my_functions.py`](tests/test_my_functions.py)

`my_functions.py` provides four simple arithmetic operations: `add`, `subtract`, `multiply`, and `divide`. The `divide` function raises a `ValueError` when the divisor is zero.

`test_my_functions.py` introduces the fundamental building blocks of pytest:

| Concept | Description |
|---|---|
| **Basic assertions** | Each test calls a source function and uses a plain `assert` statement to verify the result. |
| **Type flexibility** | `test_add_strings` shows that the same `add` function works with strings, demonstrating that Python's duck-typing is naturally exercised through tests. |
| **Exception testing** | `test_divide_by_zero` uses `pytest.raises(ValueError, match=...)` to assert that the expected exception is raised with the correct message. |
| **`@pytest.mark.slow`** | Marks `very_slow_test` so it can be included or excluded from a run with `-m slow` / `-m "not slow"`. |
| **`@pytest.mark.skip`** | Unconditionally skips a test, with a mandatory `reason` string explaining why. |
| **`@pytest.mark.xfail`** | Documents a known failure. pytest reports it as `XFAIL` rather than `FAILED`, keeping the suite green while the issue is tracked. |

---

### 2. Class-Based Tests with Setup and Teardown

**Source:** [`source/shapes.py`](source/shapes.py)  
**Tests:** [`tests/test_circle.py`](tests/test_circle.py)

`shapes.py` defines a `Shape` base class and three subclasses:

- **`Circle`** – stores a `radius`; computes `area` (πr²) and `perimeter` (2πr).
- **`Rectangle`** – stores `length` and `width`; implements `__eq__` for value comparison.
- **`Square`** – inherits from `Rectangle`, passing `side` as both `length` and `width`.

`test_circle.py` groups related tests into a **test class** (`TestCircle`) and uses pytest's per-method lifecycle hooks:

| Concept | Description |
|---|---|
| **`setup_method`** | Runs before each test method; creates a fresh `Circle(radius=10)` instance so tests remain isolated from one another. |
| **`teardown_method`** | Runs after each test method; deletes the instance to release resources and confirm clean state. |
| **Attribute assertion** | `test_radius` checks that the constructor stored the value correctly. |
| **Formula assertions** | `test_area` and `test_perimeter` recompute the expected values inline (using `math.pi`) instead of hard-coding magic numbers, making the intent self-documenting. |

---

### 3. Fixtures and `conftest.py`

**Source:** [`source/shapes.py`](source/shapes.py)  
**Tests:** [`tests/test_rectangle.py`](tests/test_rectangle.py), [`tests/conftest.py`](tests/conftest.py)

`conftest.py` is a special pytest file that makes fixtures available to every test file in the same directory without an explicit import:

```python
@pytest.fixture
def rectangle():
    return shapes.Rectangle(length=5, width=3)

@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(length=10, width=2)
```

`test_rectangle.py` demonstrates how to consume those fixtures and also shows module-level `setup_module` / `teardown_module` functions as an alternative to class-based lifecycle hooks:

| Concept | Description |
|---|---|
| **Fixture injection** | Test functions declare fixture names as parameters; pytest resolves and injects them automatically. |
| **`conftest.py` scope** | Fixtures defined in `conftest.py` are shared across all test files in the directory, eliminating duplication. |
| **Module-level setup/teardown** | `setup_method` / `teardown_method` at module level (outside a class) run before/after each test function in that file. |
| **Equality and inequality** | `test_not_equal` and `test_area_not_equal` compare two different `Rectangle` instances, verifying that the `__eq__` implementation behaves correctly. |

---

### 4. Parametrized Tests

**Source:** [`source/shapes.py`](source/shapes.py)  
**Tests:** [`tests/test_square.py`](tests/test_square.py)

`test_square.py` uses `@pytest.mark.parametrize` to run the same test logic against multiple sets of input data without writing repetitive test functions:

```python
@pytest.mark.parametrize(
    "side_length, expected_area, random_param",
    [
        (2, 4, 12),
        (3, 9, 15),
        (4, 16, 20),
        (5, 25, 25),
    ],
)
def test_square_area(side_length, expected_area, random_param):
    assert shapes.Square(side_length).area() == expected_area
```

| Concept | Description |
|---|---|
| **`@pytest.mark.parametrize`** | Generates one independent test case per tuple; each appears as a separate entry in the test report. |
| **Extra parameters** | `random_param` is accepted by the test signature but not used in the assertion, illustrating that parametrize tuples can carry additional context values. |
| **Inheritance testing** | `Square` delegates to `Rectangle.__init__`, so these tests implicitly verify the inheritance chain as well. |

---

### 5. Mocking External Dependencies

**Source:** [`source/service.py`](source/service.py)  
**Tests:** [`tests/test_service.py`](tests/test_service.py)

`service.py` contains two functions:

- **`get_user(user_id)`** – looks up a user in a local in-memory dictionary.
- **`get_db_users()`** – makes a live `GET` request to `https://jsonplaceholder.typicode.com/users` and raises `requests.HTTPError` on a non-200 status.

`test_service.py` uses `unittest.mock.patch` (available in the standard library) to replace real network calls with controlled fake objects:

| Concept | Description |
|---|---|
| **`@mock.patch`** | Temporarily replaces the target object for the duration of the test; the mock is injected as an extra argument. |
| **Patching by dotted path** | `"source.service.get_user"` patches the name as it is looked up in the module under test, not the original definition site. |
| **`mock_get_user.return_value`** | Sets what the mock returns when called, allowing the test to verify downstream logic without touching real data. |
| **`mock.Mock()` for responses** | A `Mock` object stands in for `requests.Response`; its `status_code` and `json()` attributes are set explicitly to control the test scenario. |
| **Happy-path mocking** | `test_get_db_users` asserts that a 200 response causes the function to return the parsed JSON body. |
| **Error-path mocking** | `test_get_db_users_failure` asserts that a 400 response causes the function to raise `requests.HTTPError` with the expected message. |

---

## Key pytest Concepts Summary

| Concept | Where demonstrated |
|---|---|
| Basic `assert` | `test_my_functions.py` |
| `pytest.raises` | `test_my_functions.py` |
| `mark.skip` / `mark.xfail` / `mark.slow` | `test_my_functions.py` |
| Class-based tests (`TestCircle`) | `test_circle.py` |
| `setup_method` / `teardown_method` | `test_circle.py`, `test_rectangle.py` |
| `@pytest.fixture` | `conftest.py`, `test_rectangle.py` |
| `conftest.py` shared fixtures | `conftest.py` |
| `@pytest.mark.parametrize` | `test_square.py` |
| `unittest.mock.patch` | `test_service.py` |
| `mock.Mock()` response objects | `test_service.py` |
