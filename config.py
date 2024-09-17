import uuid
from datetime import datetime

class ConfigManager:
    _instance = None

    # Konfigürasyon değişkenleri
    _target_url = None
    _project_name = None
    _session_id = None
    _session_start = None

    def __new__(cls, url=None, name=None, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, url=None, name=None):
        if url is not None:
            self.set_target_url(url)
        if name is not None:
            self.set_project_name(name)
        if ConfigManager._session_id is None:
            ConfigManager._session_id = str(uuid.uuid4())
        if ConfigManager._session_start is None:
            ConfigManager._session_start = int(datetime.now().timestamp())

    @classmethod
    def set_target_url(cls, url):
        cls._target_url = url

    @classmethod
    def get_target_url(cls):
        return cls._target_url

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
        cls.set_target_url(url)
        cls.set_project_name(name)
        cls._session_id = str(uuid.uuid4())
        cls._session_start = int(datetime.now().timestamp())
