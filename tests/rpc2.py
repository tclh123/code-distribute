#!/usr/bin/env python

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

from rpc_client import Jagare
from router.router import Router


# router
router = Router()
ip = router.lookup('lh/testproj')

# set node (host:port)
Jagare.host = ip
Jagare.port = 7303

Jagare.init('/home/vagrant/data/lh/testproj', None, True)
print Jagare.get('/home/vagrant/data/lh/testproj')
# print Jagare.list_branches('/home/vagrant/github/code-distribute/node/tmp/testproj-2')

print Jagare.host, Jagare.port
