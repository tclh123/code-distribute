#!/usr/bin/env python


#TODO: get data from routing table

class Router(object):
    def lookup(self, project_name, protocol):

        # for test
        if project_name != "lh/testproj":
            return None

        if protocol == 'http':
            host = ("127.0.0.1", 2200)
        elif protocol == 'ssh':
            host = ("127.0.0.1", 2201)
        else:
            return None
        return host
