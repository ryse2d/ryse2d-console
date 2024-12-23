#!/usr/bin/python
# ----------------------------------------------------------------------------
# ryse2d "version" plugin
#
# Author: Ricardo Quesada
# Copyright 2013 (C) Zynga, Inc
#
# License: MIT
# ----------------------------------------------------------------------------
'''
"version" plugin for ryse2d command line tool
'''

__docformat__ = 'restructuredtext'

import re
import os
import ryse2d
import inspect


#
# Plugins should be a sublass of CCJSPlugin
#
class CCPluginVersion(ryse2d.CCPlugin):

    @staticmethod
    def plugin_name():
    	return "version"

    @staticmethod
    def brief_description():
        return "prints the version of the installed components"

    def _show_versions(self):
        path = os.path.join(self._src_dir, "ryse2dx", "ryse2d.cpp")
        if not os.path.exists(path):
            path = os.path.join(self._src_dir, "ryse", "2d", "ryse2d.cpp")
            if not os.path.exists(path):
                raise ryse2d.CCPluginError("Couldn't find file with version information")

    	with open(path, 'r')  as f:
    		data = f.read()
    		match = re.search('ryse2dVersion\(\)\s*{\s*return\s+"([^"]+)"\s*;', data)
    		if match:
    			print 'ryse2d %s' % match.group(1)
    		else:
    			raise ryse2d.CCPluginError("Couldn't find version info")

    def run(self, argv, dependencies):
    	self.parse_args(argv)
        self._show_versions()

