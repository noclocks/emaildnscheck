"""Regular Expressions"""

import re

WSP_REGEX = r"[ \t]"

HTTPS_REGEX  = (
    r"https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]"
    r"[0-9a-fA-F]))+"
)

MAILTO_REGEX_STRING = (
    r"^(mailto):([\w\-!#$%&'*+-/=?^_`{|}~]"
    r"[\w\-.!#$%&'*+-/=?^_`{|}~]*@[\w\-.]+)(!\w+)?"
)

MAILTO_REGEX = re.compile(MAILTO_REGEX_STRING, re.IGNORECASE)
