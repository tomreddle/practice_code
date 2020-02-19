# 读取config.ini中的数据
# 导入包
import os
import configparser


class ConfigPrac(object):
    def __init__(self, config_path):
        self.config_path = config_path      # 配置文件config.ini文件路径
        self.conf = configparser.ConfigParser()     # 实例化
        self.conf.read(config_path, encoding='UTF-8')

    # 获取指定section中对应option的值
    def read_value(self, section, option):    # section区段名  key_name区段中指定的option
        return self.conf.get(section, option)

    # 获取指定section中所有键值对
    def get_item_values(self, section):
        return self.conf.items(section)

    # 获取指定section中所有option名
    def get_option_values(self, section):
        return self.conf.options(section)

    # 获取文件中所有section
    def get_section_values(self):
        return self.conf.sections()


if __name__ == '__main__':
    config_path = os.path.dirname(os.path.abspath(__file__)) + '\\' + 'config.ini'
    # config_path = r'E:\for_learn\code\config.ini'
    print(config_path)
    conf = ConfigPrac(config_path)
    print('DATABASE中username的值{}'.format(conf.read_value('DATABASE', 'username')))
    print('所有的section值为{}'.format(conf.get_section_values()))
    print('指定section中所有option的值{}'.format(conf.get_option_values('DATABASE')))
    print('指定section中所有键值对{}'.format(conf.get_item_values('DATABASE')))
