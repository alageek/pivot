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
        self.setting_values = {
            'Settings': None,
            'Candidate': [
                'experience',
                'expertise',
                'education',
                'other'
            ]
        }
        self.keys = self.setting_values.keys()

    def setting(self, key):
        try:
            return self.settings['Settings'][key]
        except KeyError:
            return '%s: Not Defined' % key

    def candidate(self, key):
        try:
            return self.settings['Candidate'][key]
        except KeyError:
            if key == 'mugshot':
                return '/static/img/mugshot.png'

            return '%s: Not Defined' % key

    def check_settings_file(self):
        for key in self.keys:
            if not self.settings.has_key(key):
                sys.exit("Please check your settings.yaml file. "
                         "%s keys required: %s"
                    % (len(self.keys), ', '.join(self.keys)))

            if self.setting_values[key]:
                sub_keys = self.setting_values[key]
                for sub_key in sub_keys:
                    if not self.settings[key].has_key(sub_key):
                        sys.exit("Please check your settings.yaml file. "
                                 "%s sub keys required for %s: %s"
                            % (len(sub_keys), key, ', '.join(sub_keys)))
