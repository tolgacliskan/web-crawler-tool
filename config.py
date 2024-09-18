import uuid
from datetime import datetime
from helpers.url_helpers import remove_http_https, ensure_secure_url
from url_parser import parse_url

class ConfigManager:
    _instance = None

    # Konfigürasyon değişkenleri
    _target = None
    _secure_url = None
    _project_name = None
    _session_id = None
    _session_start = None

    def __init__(self, url=None, name=None):
        if url is not None:
            self.set_target(url)
            self.set_secure_url(url)
        if name is not None:
            self.set_project_name(name)
        if ConfigManager._session_id is None:
            ConfigManager._session_id = str(uuid.uuid4())
        if ConfigManager._session_start is None:
            ConfigManager._session_start = int(datetime.now().timestamp())

    @classmethod
    def set_target(cls, url):
        cls._target = parse_url(url)

    @classmethod
    def get_target(cls):
        return cls._target

    @classmethod
    def set_base_url(cls, url):
        cls._base_url = url

    @classmethod
    def get_base_url(cls):
        return cls._base_url
    
    @classmethod
    def set_secure_url(cls, url):
        cls._secure_url = url

    @classmethod
    def get_secure_url(cls):
        return cls._secure_url

    @classmethod
    def set_project_name(cls, name):
        cls._project_name = name

    @classmethod
    def get_project_name(cls):
        return cls._project_name

    @classmethod
    def get_session_id(cls):
        return cls._session_id

    @classmethod
    def get_session_start(cls):
        return cls._session_start

    @classmethod
    def reset_config(cls, url=None, name=None):
        cls.set_target(url)
        cls.set_project_name(name)
        cls._session_id = str(uuid.uuid4())
        cls._session_start = int(datetime.now().timestamp())
