from googletrans import Translator
import yaml
from pprint import pprint

wrap = input


def input(prompt: str = '', default=None) -> str:
    """
    The input function is a wrapper for the built-in input function.
    It allows to set default result of input if user just presses enter

    :param prompt:str: Specify the prompt string
    :param default: Set a default value in case the user just presses enter
    :return: User input result
    """
    inp = wrap(prompt)
    if inp == '':
        return default
    else:
        return inp


def populate_yml_google_translate(in_file: str):
    translator = Translator()
    with open(in_file) as f:
        templates = yaml.safe_load(f)
    result = {'ru': dict()}
    for key in templates['en'].keys():
        result['ru'].update({key: translator.translate(templates['en'][key], dest='ru').text})
    with open('result.yml', 'w+', encoding='utf-8') as f:
        yaml.dump(result, f, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    populate_yml_google_translate('../../locals/iplogger/iplogger.en.yml')