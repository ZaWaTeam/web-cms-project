import os
import pathlib

import i18n

from core.configparse import config


class LanguageManager:
    def __init__(self, dir_name='cms', fallback_locale='en'):
        """
        Creates language manager that will be used for translating.


        :param dir_name: directory of translations in locals/*
        :param fallback_locale: locale that will be used if DEVELOPMENT[Language] parameter is not found
        """
        i18n.load_path.append(os.path.join(pathlib.Path().resolve(), f'locals\\{dir_name}'))
        self.locale = config.get("DEVELOPMENT", "Language", fallback=fallback_locale)
        self.dir_name = dir_name
        i18n.config.set('locale', self.locale)

    def get(self, str_name: str, locale=None) -> str:
        """
        The get function is a helper function that returns the value of a
        given key from translation file. If no locale is specified, it will default to
        the current locale.

        :param self: Access variables that belongs to the class
        :param str_name:str: Pass the name of the string to be found
        :param locale: Specify the locale of the translation
        :return: The value of the key if it exists, otherwise returns none
        """

        if locale is None:
            locale = self.locale
        return i18n.t(f"{self.dir_name}.{str_name}", locale=locale)
