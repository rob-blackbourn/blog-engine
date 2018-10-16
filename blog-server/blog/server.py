from aiohttp import web
import argparse
from easydict import EasyDict as edict
import yaml
from .initialization import initialize

from . import __version__ as version


def parse_args(argv: list):
    parser = argparse.ArgumentParser(
        description='JetBlack GraphQL Blog',
        add_help=False)

    parser.add_argument(
        '--help', help='Show usage',
        action='help')
    parser.add_argument(
        '--version', help='Show version',
        action='version', version='%(prog)s ' + version)
    parser.add_argument(
        '-f', '--config-file', help='Path to the configuration file.',
        action="store", dest='CONFIG_FILE')

    return parser.parse_args(argv)


def load_config(filename):
    with open(filename, 'rt') as fp:
        config = yaml.load(fp)
    return edict(config)


def start_server(config):
    app = web.Application()

    app['config'] = config

    initialize(app)

    web.run_app(app, host=config.http.host, port=config.http.port)


def startup(argv):
    args = parse_args(argv[1:])
    config = load_config(args.CONFIG_FILE)
    start_server(config)
