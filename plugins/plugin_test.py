#!/usr/bin/python
# ----------------------------------------------------------------------------
# ryse2d "test" plugin
#
# Author: Ricardo Quesada
# Copyright 2014 (C) Chukong Technologies
#
# License: MIT
# ----------------------------------------------------------------------------
'''
"test" plugin for ryse2d command line tool
'''

__docformat__ = 'restructuredtext'

import ryse


#
# Plugins should be a sublass of CCPlugin
#
class CCPluginTest(ryse.CCPlugin):

    @staticmethod
    def plugin_name():
        return "test"

    @staticmethod
    def brief_description():
        return "useful to test the plugin framework"

    def run(self, argv, dependencies):
        print("ryse2d path: %s" % self.get_ryse2d_path())
        print("console path: %s" % self.get_console_path())
        print("templates paths: %s" % self.get_templates_paths())

        parser = ryse.Ryse2dIniParser()
        print("plugins path: %s" % parser.get_plugins_path())

        print("ryse2d mode: %s" % self.get_ryse2d_mode())
