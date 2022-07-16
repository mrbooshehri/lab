import re

# play with findall, finditr, match, search, and regex
# play with .VERBOSE

regex_pattern = "\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}"

regex_object = re.compile(regex_pattern)

target_string = """
192.168.1.13
192.168.1.15
192.168.1.19
192.168.1.12
192.168.1.10
"""

#for match in re.findall(regex_pattern, target_string):
#    print(match)


#for match in regex_object.findall(target_string):
#    print(match)

#searched = re.search(regex_pattern, target_string)
#print(searched.group(0))

match = regex_object.match(target_string)

print(match)
