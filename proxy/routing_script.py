# coding: utf-8

import re
from router.router import Router


re_user_agent = re.compile("User\-Agent: git/.*")
router = Router()


def proxy(data):
    lines = data.splitlines()
    if not re_user_agent.match(lines[1]):
        return None
    if "HTTP" in lines[0]:
        protocol = "http"
        # e.g.
        # GET /([\w\.\-]+)/[\w\.\-]+/info/refs?service=git-upload-pack HTTP/1.1
        # POST /([\w\.\-]+)/[\w\.\-]+/git-upload-pack HTTP/1.1
        path = lines[0].split()[1]
        parts = path.split("/")
        # e.g. lh/testproj
        project_name = "/".join(parts[1:3])
    else:
        # TODO: support ssh
        protocol = 'ssh'
    host = router.lookup(project_name, protocol)
    if host:
        return {"remote": host}
    return None
