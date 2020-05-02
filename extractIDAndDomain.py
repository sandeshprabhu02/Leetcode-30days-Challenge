import re
from urllib.parse import urlparse

def extractIDAndDomain(message):
    id_regex = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
    domain_regex = r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
    print(re.findall(id_regex, message)[0])
    print(re.findall(domain_regex, message)[0])
    print(re.findall(id_regex, message)[0], re.findall(domain_regex, message)[0])


message = "hi i am ABCDE1234F and working at http:www.oyo.com/hi"
extractIDAndDomain(message)