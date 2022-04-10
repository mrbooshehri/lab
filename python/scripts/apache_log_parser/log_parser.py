#! /usr/bin/env python

import re
from collections import Counter

def main():
    parser()

def parser():
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    re_obj = re.compile(pattern)
    with open('log', 'r') as f:
        log = f.read()
        ips = re_obj.findall(log)
        ip_count = Counter(ips)
        for i ,j in ip_count.items():
            print(f"ip: {str(i)} count: {str(j)}")


if __name__ == "__main__":
    main()
