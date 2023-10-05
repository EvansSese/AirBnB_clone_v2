#!/usr/bin/python3
""" Create an archive file """


from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a compressed archive from web_static folder."""
    try:
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(time_format)
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
