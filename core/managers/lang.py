import os
import pathlib

import i18n

from core.configparse import config


class LanguageManager:
    def __init__(self, dir_name='cms', fallback_locale='en'):
        i18n.load_path.append(os.path.join(
            pathlib.Path().resolve(), f'locals/{dir_name}'))
        self.locale = config.get(
            "DEVELOPMENT", "Language", fallback=fallback_locale)
        self.dir_name = dir_name
        i18n.config.set('locale', self.locale)

    def get(self, str_name: str, locale=None, **kwargs) -> str:
        if locale is None:
            locale = self.locale
        return i18n.t(f"{self.dir_name}.{str_name}", locale=locale, **kwargs)
