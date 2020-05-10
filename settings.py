import os
import yaml
import errno

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(dict):
    def __init__(self, root_path=BASE_DIR):
        self.root_path = root_path
        self.from_yaml()
        super().__init__({})

    def from_yaml(self, silent=False):
        if self.root_path:
            filename = os.path.join(self.root_path, "config.yml")
        try:
            with open(filename, 'rt', encoding='utf8') as f:
                obj = yaml.safe_load(f)
        except IOError as e:
            if silent and e.errno in (errno.ENOENT, errno.EISDIR):
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        if obj:
            return self.from_mapping(obj)
        return True

    def from_mapping(self, *mapping, **kwargs):
        mappings = []
        if len(mapping) == 1:
            if hasattr(mapping[0], 'items'):
                mappings.append(mapping[0].items())
            else:
                mappings.append(mapping[0])
        elif len(mapping) > 1:
            raise TypeError(
                'expected at most 1 positional argument, got %d' % len(mapping)
            )
        mappings.append(kwargs.items())
        for mapping in mappings:
            for (key, value) in mapping:
                if key.isupper():
                    self[key] = value
        return True

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))

    def __getitem__(self, item):
        try:
            value = super().__getitem__(item)
        except KeyError:
            value = None
        if value is not None:
            return value

    def __getattr__(self, item):
        return self.__getitem__(item)


GET = Config()


def get_db_url(db_info):
    engine = db_info.get("ENGINE")
    driver = db_info.get("DRIVER")
    host = db_info.get("HOST")
    port = db_info.get("PORT")
    user = db_info.get("USER")
    password = db_info.get("PASSWORD")
    name = db_info.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        engine, driver, user, password, host, port, name
    )


DATABASE_URI = get_db_url(GET.DATABASE)
