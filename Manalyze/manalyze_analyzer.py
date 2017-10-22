#!/usr/bin/env python
from cortexutils.analyzer import Analyzer
import os
import json

class ManalyzeAnalyzer(Analyzer):
    """
    Checking binaries through manalyze.
    """

    def __init__(self):
        Analyzer.__init__(self)

    def check(self, file):
        """
        Checks a given file against manalyze

        :param file: Path to file
        :type file:str
        :returns: Python dictionary containing the results
        :rtype: list
        """
        folder, filename = os.path.split(file)
        docker_image = "evanowe/manalyze"
        import subprocess
        command = ['docker', 'run', '--rm', '-v', folder + ":/data",
                   docker_image, "/Manalyze/bin/manalyze", "-p",
                   "clamav,compilers,peid,strings,findcrypt,btcaddress,packer,imports,resources,mitigation,authenticode",
                   "/data/" + filename, "-o", "json"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        result, err = process.communicate()
        p_status = process.wait()
	result = json.loads(result)
	result = result[result.keys()[0]]
        return result

    def summary(self, raw):
        return {"matches": len(raw["results"])}

    def run(self):
        if self.data_type == 'file':
            self.report({'results': self.check(self.getParam('file'))})
        else:
            self.error('Wrong data type.')

if __name__ == '__main__':
    ManalyzeAnalyzer().run()