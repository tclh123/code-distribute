#!/usr/bin/env python

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

from rpc_client import Jagare


# set node (host:port)
Jagare.host = "127.0.0.1"
Jagare.port = 7303

print Jagare.get('/home/vagrant/github/code-distribute/node/tmp/testproj-2')
print Jagare.list_branches('/home/vagrant/github/code-distribute/node/tmp/testproj-2')

print Jagare.host, Jagare.port
