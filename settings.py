import os
import sys
import yaml


class Setting:
    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        settings_yaml = os.path.join(self.root, 'settings.yaml')
        try:
            self.settings = yaml.load(file(settings_yaml))
        except IOError, e:
            sys.exit(e)
        self.keys = ['Settings', 'Candidate']

    def setting(self, key):
        try:
            return self.settings[self.keys[0]][key]
        except KeyError:
            return '%s: Not Defined' % key

    def candidate(self, key):
        try:
            return self.settings[self.keys[1]][key]
        except KeyError:
            return '%s: Not Defined' % key

    def check_settings_file(self):
        for key in self.keys:
            if not self.settings.has_key(key):
                sys.exit("Please check your settings.yaml file. "
                         "Two keys required: %s" % ', '.join(self.keys))
