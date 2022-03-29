#!/usr/bin/env python

from asn.validate import ValidateIP

class LookUp:

    def __init__(self):
        self.validate_ip = ValidateIP()
        return

    def check_version(self,ip):
        if self.validate_ip.validate(ip):
            return "IPv4"
        elif self.validate_ip.validate_v6(ip):
            return "IPv6"
        else:
            raise ValueError("Invalid IP Address")

    def ip_to_binary(self,ip):
        """
        Convert IP address to binary
        :param str: IP
        :return str: Binary
        """
        if self.check_version(ip) == "IPv4":
            octet_list_int = ip.split(".")
            octet_list_bin = [format(int(i), '08b') for i in octet_list_int]
            binary = ("").join(octet_list_bin)
        elif self.check_version(ip) == "IPv6":
            octet_list_hex = ip.split(":")
            for i in range(len(octet_list_hex)):
                if len(octet_list_hex[i]) < 4:
                    octet_list_hex[i] = (4-len(octet_list_hex[i]))*"0"+octet_list_hex[i]
            while len(octet_list_hex) < 8:
                octet_list_hex.append("0000")
            octet_list_bin = [format(int(i,16), '08b') for i in octet_list_hex]
            binary = ("").join(octet_list_bin)
        return binary

    def get_addr_network(self,address, net_size):
        """
        Extract network ID from 32 bit binary
        :param str,int: IP address, Network Size
        :return str: Network ID
        """
        #Convert ip address to 32 bit binary
        ip_bin = self.ip_to_binary(address)
        #Extract Network ID from 32 binary
        if self.check_version(address)=="IPv4":
            network = ip_bin[0:32-(32-int(net_size))]
        else:
            network = ip_bin[0:128-(128-int(net_size))]
        return network

    def ip_in_prefix(self,ip_address, prefix):
        """
        Checks if the IP address falls in CIDR range
        :param str,str: IP, CIDR
        :return boolean:
        """
        #CIDR based separation of address and network size
        [prefix_address, net_size] = prefix.split("/")
        #Convert string to int
        net_size = int(net_size)
        #Get the network ID of both prefix and ip based net size
        prefix_network = self.get_addr_network(prefix_address, net_size)
        ip_network = self.get_addr_network(ip_address, net_size)
        return ip_network == prefix_network
