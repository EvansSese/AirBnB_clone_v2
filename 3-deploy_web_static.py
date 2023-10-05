#!/usr/bin/python3
""" Create an archive file and deploy """


from fabric.api import local, env, put, run
from datetime import datetime
import os



env.hosts = ['54.87.250.91', '3.89.160.129']
env.user = 'ubuntu'


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

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False

def deploy():
    """Deploy the web_static content to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
