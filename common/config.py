from configparser import ConfigParser
import os


def get_conf(section=None, option=None):
    """
    读取config文件函数：
    1.指定section和option时，返回对应的内容；
    2.不指定section和option时，以列表形式，按组返回config文件所有内容
    """
    conf_path = os.path.dirname(os.path.dirname(__file__)) + '/conf/conf.ini'
    config = ConfigParser()
    config.read(conf_path)

    if not section and not option:
        sections = [section for section in config.sections()]
        conf = [config.items(section) for section in sections]
        return sections, conf
    elif config.has_section(section) and not option:
        conf = config.items(section)
        return conf
    elif config.has_section(section) and option:
        conf = config.get(section, option)
        return conf
    else:
        return 'section not exist'


if __name__ == '__main__':
    conf = get_conf('mongo', 'url')
    print(conf)
