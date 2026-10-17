# test_throbpennant.py
"""
Tests for ThrobPennant module.
"""

import unittest
from throbpennant import ThrobPennant

class TestThrobPennant(unittest.TestCase):
    """Test cases for ThrobPennant class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThrobPennant()
        self.assertIsInstance(instance, ThrobPennant)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThrobPennant()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
