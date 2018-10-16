from easydict import EasyDict as edict
from graphql import (GraphQLError)
from stringcase import camelcase, snakecase
from .linq import group_by, first_or_default


def dict_to_camelcase_edict(dct):
    return edict({camelcase(k): v for k, v in dct.items()})


async def aiterable_to_camelcase_edict(aiterable):
    return [dict_to_camelcase_edict(document.to_dict()) for document in documents]


def dict_to_camelcase(dct):
    return {camelcase(k): v for k, v in dct.items()}


def dict_to_snakecase(dct):
    return {snakecase(k): v for k, v in dct.items()}


def document_to_camelcase_dict(document, dct={}):
    for k, v in document.to_dict().items():
        dct[camelcase(k)] = v
    return dct


async def organise(cursor, keys, key_selector, projection=None, is_single=True):
    documents = [document async for document in cursor]
    groups = group_by(documents, key_selector)
    result = []
    for key in keys:
        values = [
            projection(document) if projection else dict_to_camelcase_edict(document.to_dict())
            for document in groups.get(key, {})
        ]
        if values:
            if is_single:
                result.append(first_or_default(values))
            else:
                result.append(values)
        else:
            result.append(None)

    return result


async def resolver_wrapper(func, *args, **kwargs):
    return await func(*args, **kwargs)


async def resolve_with_loader(loader, authorize, context, key, default=None):
    if not authorize(context):
        raise GraphQLError('unauthorized')

    result = await context.request.app['data_loaders'][loader].load(key)
    return result or default
