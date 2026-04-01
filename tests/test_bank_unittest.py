import unittest
from unittest.mock import Mock
from src.main import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.mock_logger = Mock()
        self.account = BankAccount(balance=100, logger=self.mock_logger)

    #  NORMAL OPERATIONS 
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
        self.mock_logger.log.assert_called_with("Deposited 50")

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)
        self.mock_logger.log.assert_called_with("Withdrew 30")

    #  EDGE CASES 
    def test_deposit_zero(self):
        self.account.deposit(0)
        self.assertEqual(self.account.balance, 100)
        self.mock_logger.log.assert_called_with("Deposited 0")

    def test_withdraw_exact_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)
        self.mock_logger.log.assert_called_with("Withdrew 100")

    #  EXCEPTION 
    def test_overdraft_raises_and_logs(self):
        with self.assertRaises(ValueError) as ctx:
            self.account.withdraw(500)
        self.assertEqual(str(ctx.exception), "Insufficient funds")
        self.mock_logger.log.assert_called_with("Failed withdrawal of 500")


if __name__ == "__main__":
    unittest.main()