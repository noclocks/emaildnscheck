"""DNS Exceptions"""

import logging
import dns
import dns.resolver
import re


class DNSException(Exception):
    """Raised when a general DNS Error Occurs"""

    def __init__(self, error):
        if isinstance(error, dns.exception.Timeout):
            error.kwargs["timeout"] = round(error.kwargs["timeout"], 1)


class DNSExceptionNXDOMAIN(DNSException):
    """Raised when a NXDOMAIN DNS error (RCODE:3) occurs"""
