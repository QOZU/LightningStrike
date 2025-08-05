# test_lightningstrike.py
"""
Tests for LightningStrike module.
"""

import unittest
from lightningstrike import LightningStrike

class TestLightningStrike(unittest.TestCase):
    """Test cases for LightningStrike class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LightningStrike()
        self.assertIsInstance(instance, LightningStrike)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LightningStrike()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
