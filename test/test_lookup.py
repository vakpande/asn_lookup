#!/usr/bin/env python

import sys
sys.path.append('../')
import unittest
from asn.lookup import LookUp


class TestLookUp(unittest.TestCase):

    def setUp(self):
        self.lookup = LookUp()

    def test_binary(self):
        """
        Testing the ip to euivalent binary conversion.
        """
        self.assertEqual(self.lookup.ip_to_binary("0.0.0.0"),"00000000000000000000000000000000")
        self.assertEqual(self.lookup.ip_to_binary("255.255.255.255"),"11111111111111111111111111111111")
    
    def test_get_addr_network(self):
        """
        Test to get the network address bits.
        """
        data = self.lookup.get_addr_network("8.8.0.0", "16")
        self.assertIsNotNone(data)
        self.assertEqual(data, "0000100000001000")

    def test_ip_in_prefix(self):
        """
        Test to compare the network bits for CIDR and provided IP.
        """
        self.assertEqual(self.lookup.ip_in_prefix("8.8.8.8","8.0.0.0/12"), True)
        self.assertEqual(self.lookup.ip_in_prefix("1.1.1.1","8.0.0.0/12"), False)

if __name__ == "__main__":
    unittest.main()