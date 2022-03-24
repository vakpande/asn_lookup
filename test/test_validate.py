#!/usr/bin/env python

import sys
sys.path.append('../')
import unittest
from asn.validate import ValidateIP

class TestValidateIP(unittest.TestCase):

    def setUp(self):
        self.validate_ip = ValidateIP()

    def test_validate_ip(self):
        """
        Tests if the IP is a valid IPv4.
        """
        self.assertEqual(self.validate_ip.validate("444.444.444.444"), False)
        self.assertEqual(self.validate_ip.validate("8.8.8:8"), False)
        self.assertEqual(self.validate_ip.validate("10.10.10.1"),True)

if __name__ == "__main__":
    unittest.main()
