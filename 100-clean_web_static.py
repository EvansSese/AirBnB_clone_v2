#!/usr/bin/python3
""" Create an archive file and deploy """


from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['54.87.250.91', '3.89.160.129']
env.user = 'ubuntu'


def do_clean(number=0):
    """Clean up old archives and releases."""
    try:
        number = int(number)
        if number < 0:
            number = 0

        # Clean up archives
        local("ls -t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))
        run("ls -t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))

        print("Cleaned up old archives and releases.")
        return True
    except Exception:
        return False
