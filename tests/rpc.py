#!/usr/bin/env python

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

from rpc_client import Jagare


print Jagare.get('/home/vagrant/github/code-distribute/node/tmp/testproj-2')
print Jagare.list_branches('/home/vagrant/github/code-distribute/node/tmp/testproj-2')
