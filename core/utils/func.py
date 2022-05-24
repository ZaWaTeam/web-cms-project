wrap = input
def input(prompt: str = '', default = None) -> str:
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
