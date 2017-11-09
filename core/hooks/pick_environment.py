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
import os
from sgtk import Hook


class PickEnvironment(Hook):
    def execute(self, context, **kwargs):
        if context.project is None:
            # On Flame startup before a shotgun project is attached.
            return "site"

        else:
            flame_major = int(os.environ.get("SHOTGUN_FLAME_MAJOR_VERSION", 2018))
            flame_minor = int(os.environ.get("SHOTGUN_FLAME_MINOR_VERSION", 0))

            if flame_major >= 2019:
                return "project.2019.0"

            if flame_major >= 2018 or (flame_major == 2018 and flame_minor >= 3):
                return "project.2018.3"

            # First version with the python API
            elif flame_major == 2018 and flame_minor == 2:
                return "project.2018.2"

            # 2018.1 and lower versions
            else:
                return 'project.2018.0'
