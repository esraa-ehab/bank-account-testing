# Bank Account Testing - pytest & unittest

A hands-on demonstration of Python testing best practices, showing how to write
comprehensive test suites using both **pytest** and **unittest** side by side.

## What this project demonstrates

- **Fixtures & setUp()** — reusable setup logic that runs a fresh environment before every test
- **Mocking** — replacing a real external dependency (`AuditLogger`) with a `Mock()` object so tests stay fast, isolated, and deterministic
- **Verifying mock calls** — using `assert_called_with()` to confirm the exact log message written on every operation
- **Normal operations** — deposit and withdrawal with balance and log verification
- **Edge cases** — depositing zero, withdrawing the exact balance
- **Exception testing** — verifying a `ValueError` is raised on overdraft *and* that the failed attempt was logged before the exception propagated

## Project structure
```
bank-account-testing/
├── src/
│   └── main.py                  # BankAccount + AuditLogger (code under test)
├── tests/
│   ├── test_bank_pytest.py      # pytest test suite (uses @pytest.fixture)
│   └── test_bank_unittest.py    # unittest test suite (uses setUp())
├── requirements.txt
└── README.md
```

## Running the tests

**Run the pytest suite**
```bash
pytest tests/test_bank_pytest.py -v
```

**Run the unittest suite**
```bash
python -m unittest tests/test_bank_unittest.py -v
```

## Why mocking matters

`AuditLogger` in a real application would write to a file or database. Running
that code in every test would make the suite slow, fragile, and dependent on
external infrastructure. By passing in a `Mock()` instead, each test runs in
complete isolation — and `assert_called_with()` lets us verify the logger
received exactly the right message without anything ever being written to disk.

## Requirements

- Python 3.8+
- pytest 8.x