# ----------------------------------------------------------------------------
# ryse "package" plugin
#
# Copyright 2014 (C) ryse2d-x.org
#
# License: MIT
# ----------------------------------------------------------------------------
'''
"package" plugins
'''

__docformat__ = 'restructuredtext'

import os
import sys
import ryse
import subprocess
from MultiLanguage import MultiLanguage

class CCPluginPackage(ryse.CCPlugin):
    @staticmethod
    def plugin_name():
        return "package"

    @staticmethod
    def brief_description():
        return MultiLanguage.get_string('PACKAGE_BRIEF')

    def parse_args(self, argv):
        return {"command": argv[0]}

    def run(self, argv, dependencies):
        if '--anysdk' in argv:
            argv.remove('--anysdk')
            cmd = self._get_rysepackage_path() + ' --runinryse ' + ' '.join(argv)
            ret = self._run_cmd(cmd)
        else:
            if '--sdkbox' in argv:
                argv.remove('--sdkbox')
            cmd = self._get_sdkbox_path() + ' --runinryse ' + ' '.join(argv)
            ret = self._run_cmd(cmd)
        if 0 != ret:
            message = MultiLanguage.get_string('RYSE_ERROR_RUNNING_CMD_RET_FMT', str(ret))
            raise ryse.CCPluginError(message, ryse.CCPluginError.ERROR_RUNNING_CMD)

    def _run_cmd(self, command, cwd=None):
        # ryse.CMDRunner.run_cmd(command, False, cwd=cwd)
        return subprocess.call(command, shell=True, cwd=cwd)

    def _get_sdkbox_path(self):
        path = ''
        if getattr(sys, 'frozen', None):
            path = os.path.realpath(os.path.dirname(sys.executable))
        else:
            path = os.path.realpath(os.path.dirname(__file__))
        return os.path.join(path, 'sdkbox')

    def _get_rysepackage_path(self):
        path = ''
        if getattr(sys, 'frozen', None):
            path = os.path.realpath(os.path.dirname(sys.executable))
        else:
            path = os.path.realpath(os.path.dirname(__file__))
        return os.path.join(path, 'rysepackage')

    def print_help(self):
            print(MultiLanguage.get_string('PACKAGE_HELP'))
