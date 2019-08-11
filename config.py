import yaml


class ConfigParse:
    """
    このクラスは設定ファイルから設定を読み込むファイルです。
    """
    HOST_CONFIG = None
    HOST_TYPE = None

    def __init__(self):
        self.parse_config()

    def parse_config(self):
        config_file = open('config.yaml', 'r')
        config_txt = config_file.read()
        parse_config = yaml.safe_load(config_txt)
        self.HOST_CONFIG = parse_config.get('host_config')
        self.HOST_TYPE = self.HOST_CONFIG.get('host_type')


print(ConfigParse().HOST_TYPE)
