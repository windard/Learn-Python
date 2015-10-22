# import argparse

# parser = argparse.ArgumentParser()
# parser.parse_args()

import argparse
parser = argparse.ArgumentParser(description="input your host and port")
# parser.add_argument("echo")
# parser.add_argument("echo",help="echo this str")
# parser.add_argument("--host",help="chose host",action="store",default='127.0.0.1',dest="host")
parser.add_argument("-host",help="chose host",action="store",default='127.0.0.1')
args = parser.parse_args()
host = args.host
print host

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v","--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#    print "verbosity turned on"
#    print args.verbose