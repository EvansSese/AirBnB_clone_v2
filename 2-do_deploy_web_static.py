#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers."""

from fabric.api import env, put, run
import os

env.hosts = ['54.87.250.91', '3.89.160.129']

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_name)[0]

        # Upload the archive to /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Create the directory if it doesn't exist
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, archive_no_ext))

        # Remove the uploaded archive
        run("rm /tmp/{}".format(archive_name))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_no_ext))

        print("New version deployed!")
        return True
    except Exception:
        return False
