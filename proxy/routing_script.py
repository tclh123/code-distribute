import re
from router.router import Router


# TODO:
# 获得 project_name
# 分辨 http请求 ssh请求
# user-agent 是 git 的

re_host = re.compile("Host:\s*(.*)\r\n")
router = Router()


def proxy(data):
    matches = re_host.findall(data)
    if matches:
        host = router.lookup(matches.pop())
        return {"remote": host}
    return None
