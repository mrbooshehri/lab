#! /usr/bin/env python

import subprocess

def ls():
    subprocess.call(["ls", "-l"])

def main():
    ls()

if __name__ == "__main__":
    main()
