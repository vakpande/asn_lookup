**ASN lookup utility**
======================

## asn_lookup

The client implements a simple python module to search for an IP in the config file and returns the ASN and the networks the IP is within. It check if the IP is part of multiple ranges and then returns the result in most specific to least spefic order.

## Supported version:
- IPv4
- IPv6

**Design Pattern**
==================

There are mainly 4 portions of the design.

- Validates the argument and checks if the input is a valid IP address.
- Checks if the env variable is set else makes rest call to cofig file URL
- Parses the data and finds CIDRs where the IP address falls in range and appends the CIDR and ASN to final result.
- Returns the result sorted based on most specific to least.

## Logic to find the IP address in CIDR.

IP address consists of 2 portions Network bits and Host bits, In order for us to check if any IP address is part of the CIDR we can follow the steps listed below to find the Network bits for CIDR and the IP address. once we have that information, we can compare both the network bits and if both are same, we found the IP in CIDR.

- Convert the IP address to binary.
- Get Network bits for IP and CIDR.
- Compare both to find if the IP is in CIDR range.


## Code layout

The code consist of modules for different tasks and a unit testing module which verifies each definition to make sure those definitions returns the value as expected.
To make code look clean, there is a definitions module to pass the fix values such as env variable name and URL for config file.

```
asn_lookup
  |
  asn/
    |
    lookup module --> converts IP to binary, gets the network bits, compares both network bits
    validate module --> validates IPv4 address
  test/
    |
    test_lookup --> unit test module to verify the lookup module functions
    test_validate --> unit test validate to verify the validate function.
  definitions --> holds constant definitions
  lookup_addr.py --> holds the logic to validate the argument, parse the config file and print the result.
  ```



**Usage**
=========

It takes the IP address as an argument.

```
./lookup_addr.py 8.8.8.8
['8.8.8.0/24 15169', '8.0.0.0/12 3356', '8.0.0.0/9 3356']
```

The utility looks for **CONFIG_FILE_PATH** env variable to find the config file location. If the env variable is found not set it alternatively makes a rest call to the config URL and parses the data to find the ASN and CIDRs (where IP address falls in range)


**Steps to use the utility**
============================

The tool can be cloned directly from the git repository. once cloned, the tool can then be directly run from root directory using the command below

./lookup_addr.py <IP_Addr>

this will print the list of CIDRs along with the ASN.

```
./lookup_addr.py -h     
usage: lookup_addr.py [-h] ip

ASN lookup for the IP address provided as an argument

positional arguments:
  ip          IP address

optional arguments:
  -h, --help  show this help message and exit
```


**Code Metrics**
================

## Test Coverage

```
python -m unittest discover
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```


## Execution Time

```
./lookup_addr.py 8.8.8.8   
['8.8.8.0/24 15169', '8.0.0.0/12 3356', '8.0.0.0/9 3356']
Total time taken: --- 28.2627489567 seconds ---

./lookup_addr.py 1.1.1.1
['1.1.1.0/24 13335']
Total time taken: --- 18.3940188885 seconds ---

./lookup_addr.py 2.2.2.2
['2.2.0.0/16 3215']
Total time taken: --- 18.3473639488 seconds ---

./lookup_addr.py 192.168.2.1
['192.168.2.0/24 62538', '192.168.0.0/16 62538']
Total time taken: --- 18.331496954 seconds ---
```

**Average time taken: 21 Seconds**  
> not the best way to calculate the excuetion time as there are lot of variables involved and this can vary on different systems.

