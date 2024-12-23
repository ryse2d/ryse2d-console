#!/usr/bin/python
# ----------------------------------------------------------------------------
# ryse2d "gui" plugin
#
# ----------------------------------------------------------------------------
'''
"gui" plugin for ryse2d command line tool
'''
from __future__ import print_function
from __future__ import unicode_literals

__docformat__ = 'restructuredtext'

import ryse
import subprocess


class CCPluginGUI(ryse.CCPlugin):
    """
    launches the ryse2d console gui
    """

    @staticmethod
    def plugin_name():
        return "gui"

    @staticmethod
    def brief_description():
        return "shows the GUI"

    def run(self, argv, dependencies):
        subprocess.Popen(['open', '-a', self.get_console_path() + '/' + 'Ryse2d-Console-GUI.app'])
