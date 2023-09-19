"""Logging module"""
import logging
from logging import config, Logger

import yaml

from ..settings import settings


def setup_logging() -> Logger:
    """
    Setup logging configuration.
    ENV - prod, stage, dev (see logging.yaml)
    """
    with open('crypto_data_provider/utils/logging.yaml', 'rt', encoding="utf-8") as file:
        yaml_config = yaml.safe_load(file.read())
        config.dictConfig(yaml_config)
    if settings.env:
        return logging.getLogger(settings.env.lower())
    return logging.getLogger('prod')
