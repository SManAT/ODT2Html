import logging
import yaml
import sys
import os


class ConfigTool():
    """ a Tool to handel Config File in YAML Style """
    def __init__(self, window):
        self.logger = logging.getLogger('ConfigTool')
        self.window = window
        self.configFile = self.window.configFile

    def updateConfig(self):
        """ update the config File """
        with open(self.configFile, 'w') as fp:
            yaml.dump(self.window.config, fp, sort_keys=False, default_flow_style=False)

    def createEmptyConfigFile(self):
        """ will create an Empty Config File """
        data = dict(
            app=dict(
                title='LOPath',
            ),
        )
        self.writeConfig(data)

    def writeConfig(self, data):
        """ write into the config File """
        with open(self.configFile, 'w') as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False)

    def load_yml(self):
        """ Load the yaml file config.yaml, or create a dummy FIle """
        if os.path.exists(self.configFile) is False:
            self.createEmptyConfigFile()
            self.logger.error("New config.yml File created ...")
            self.logger.error("Please edit src/config/config.yml as needed ...")
            self.logger.error("- Exit -")
            sys.exit(-1)
        with open(self.configFile, 'rt') as f:
            yml = yaml.safe_load(f.read())
        return yml
