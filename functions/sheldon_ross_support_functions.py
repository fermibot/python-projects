from functions.random_functions import RandomReal


def randomChoiceCustom(_probability):
    _result = 0
    if RandomReal() <= _probability:
        _result = 1
    return _result
