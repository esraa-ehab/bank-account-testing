import pytest
from unittest.mock import Mock
from src.main import BankAccount

# fixture 
@pytest.fixture 
def account():
    mock_logger = Mock()
    bank_acc = BankAccount(balance=100, logger=mock_logger)
    return bank_acc

# operations
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150
    account.logger.log.assert_called_with("Deposited 50")

def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
    account.logger.log.assert_called_with("Withdrew 30")

# edge cases
def test_deposit_zero(account):
    account.deposit(0)
    assert account.balance == 100             
    account.logger.log.assert_called_with("Deposited 0")

def test_withdraw_all_balance(account):
    account.withdraw(100)
    assert account.balance == 0
    account.logger.log.assert_called_with("Withdrew 100")

# exception
def test_overdraft(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200)
    account.logger.log.assert_called_with("Failed withdrawal of 200")