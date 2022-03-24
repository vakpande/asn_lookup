#!/usr/bin/env python

import re

class ValidateIP:

    def __init__(self):
        """
        regex to find the valid IPv4
        """
        self.ipv4 = re.compile("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$")

    def validate(self,ip):
        """
        validates if the IP provided in a valid IPv4 address.
        :param str: IP address
        :return boolean:
        """
        if re.match(self.ipv4,ip):
            return True
        return False
    
