#!/usr/bin/env python


class LookUp:

    def __init__(self):
        return

    def ip_to_binary(self,ip):
        """
        Convert IP address to binary
        :param str: IP
        :return str: Binary
        """
        octet_list_int = ip.split(".")
        octet_list_bin = [format(int(i), '08b') for i in octet_list_int]
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
        network = ip_bin[0:32-(32-int(net_size))]    
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
