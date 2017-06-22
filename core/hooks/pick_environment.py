# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook which chooses an environment file to use based on the current context.
"""

from sgtk import Hook


class PickEnvironment(Hook):
    def execute(self, context, **kwargs):
        if context.project is None:
            # On Flame startup before a shotgun project is attached.
            return "site"

        else:
            import os

            flame_version_major = os.environ.get('SHOTGUN_FLAME_MAJOR_VERSION')
            flame_version_minor = os.environ.get('SHOTGUN_FLAME_MINOR_VERSION')
            flame_version_patch = os.environ.get('SHOTGUN_FLAME_PATCH_VERSION')

            flame_version = (flame_version_major, flame_version_minor, flame_version_patch)

            if flame_version >= (2018, 2, 0):
                return 'project.2018.2'

            return 'project.2018'
