from aiodataloader import DataLoader


class DbDataLoader(DataLoader):

    def __init__(self, db, loader):
        super().__init__()
        self.db = db
        self.loader = loader

    async def batch_load_fn(self, keys):
        return await self.loader(self.db, keys)


class DbDataLoaderContext:

    def __init__(self, db, loaders):
        self.loaders = {name: DbDataLoader(db, func) for name, func in loaders.items()}

    async def load(self, name, keys):
        return await self.loaders[name].load(keys)


class DbDataLoaderRegistry:

    def __init__(self, **kwargs):
        self.funcs = {name: func for name, func in kwargs.items()}

    def register(self, name, func):
        self.funcs[name] = func

    def create_loders(self, db):
        return DbDataLoaderContext(db, self.funcs)
