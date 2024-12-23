# ----------------------------------------------------------------------------
# ryse2d "update" plugin
#
# Author: Luis Parravicini
#
# License: MIT
# ----------------------------------------------------------------------------
'''
"update" plugin for ryse2d command line tool
'''

__docformat__ = 'restructuredtext'

import re
import os
import ryse2d
import httplib


class CCPluginUpdate(ryse2d.CCPlugin):

    @staticmethod
    def plugin_name():
    	return "update"

    @staticmethod
    def brief_description():
        return "checks if there's an update available"

    def _check_versions(self):
        latest_version = self._get_latest_version()
        current_version = '2.1.0'
        #FIXME check version numbers with verlib? https://wiki.python.org/moin/Distutils/VersionComparison
        


    def _get_latest_version(self):
        ryse2d.Logging.info("obtaining latest version number")

        conn = httplib.HTTPConnection('ryse2d-x.org', timeout=10)
        try:
            conn.request('GET', '/download')
            res = conn.getresponse()
            if res.status != httplib.OK:
                raise ryse2d.CCPluginError("Unexpected response status (%d)" % res.status)
            data = res.read()

            #FIXME: quick and dirty (and error prone) way to extract the latest version
            #from the html page
            match = re.search('href="http://cdn.ryse2d-x.org/ryse2d-x-(.*?).zip"', data)
            if match is None:
                raise ryse2d.CCPluginError("Couldn't extract latest version from site")
            
            return match.group(1)
        finally:
            conn.close()


    def run(self, argv, dependencies):
    	self.parse_args(argv)
        self._check_versions()
