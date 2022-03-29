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

    def test_validate_ip_v6(self):
        """
        Tests if the IP is a valid IPv4.
        """
        self.assertEqual(self.validate_ip.validate_v6("2001:db8:3333:4444:5555:6666:7777:8888"), True)
        self.assertEqual(self.validate_ip.validate_v6("20002::"), False)
        self.assertEqual(self.validate_ip.validate_v6("::"), True)


if __name__ == "__main__":
    unittest.main()
