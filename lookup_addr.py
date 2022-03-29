#!/usr/bin/env python

import re
import os
import time
import sys
import argparse
import requests
from asn.lookup import LookUp
from asn.validate import ValidateIP
from definitions import *


validate_ip = ValidateIP()
asn = LookUp()
result = []

def generate_data(line,args):
    """
    Function to generate the result data and append it to final List
    :param str str: line, arguments
    """
    if validate_ip.validate(args.ip):
        if validate_ip.validate(str(line.split()[0].split("/")[0])) and asn.ip_in_prefix(args.ip, str(line.split()[0])):
            result.append(line.rstrip())
    elif validate_ip.validate_v6(args.ip):
        if validate_ip.validate_v6(str(line.split()[0].split("/")[0])) and asn.ip_in_prefix(args.ip, str(line.split()[0])):
            result.append(line.rstrip())
    else:
        raise ValueError("Invalid IP")


def run():
    """
    Driver function to validate the argument and check if the env variable is set (if not make rest call to get the config data)
    parse the data to find the ASN and append it to the final list.
    :return list:
    """
    parser = argparse.ArgumentParser(description='ASN lookup for the IP address provided as an argument')
    parser.add_argument('ip',  help='IP address')
    args = parser.parse_args()

    if CONFIG_FILE_LOCATION in os.environ:
        with open(os.getenv(CONFIG_FILE_LOCATION),"r") as f:
            for line in f:
                generate_data(line,args)
    else:
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        for line in resp.iter_lines():
            generate_data(line,args)            

    return sorted(result, key=lambda x : [int(m) for m in re.findall("\d+",x)],reverse=True) if result else sys.exit(1)


if __name__ == "__main__":
    start_time = time.time()
    print(run())
    print("Total time taken: --- %s seconds ---" % (time.time() - start_time))