#!/usr/bin/env python


#NOTE: you can store routing table in mysql or somewhere


ROUTING_TABLE = {
    'lh/testproj':      '192.168.2.11',
    'lh/testproj2':     '192.168.2.11',
    'testuser/proj1':   '192.168.2.8',
    'testuser/proj2':   '192.168.2.9',
}


class Router(object):

    # def lookup(self, project_name, protocol):

    #     # for test
    #     if project_name != "lh/testproj":
    #         return None

    #     if protocol == 'http':
    #         host = ("127.0.0.1", 2200)
    #     elif protocol == 'ssh':
    #         host = ("127.0.0.1", 2201)
    #     else:
    #         return None
    #     return host

    def lookup(self, project_name):
        if project_name not in ROUTING_TABLE:
            return None
        return ROUTING_TABLE[project_name]
