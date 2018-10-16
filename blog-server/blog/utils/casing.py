from stringcase import camelcase, snakecase

__all__ = ['dict_to_camelcase_dict', 'dict_to_snakecase_dict']


def _dict_to_case_dict(dct, func, cls=dict):
    return cls({func(k): v for k, v in dct.items()})


def dict_to_camelcase_dict(dct, cls=dict):
    return _dict_to_case_dict(dct, camelcase, cls)


def dict_to_snakecase_dict(dct, cls=dict):
    return _dict_to_case_dict(dct, snakecase, cls)
