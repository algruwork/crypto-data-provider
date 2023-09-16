"""Logging module"""
import logging
from logging import config, Logger
import os

import yaml


def setup_logging() -> Logger:
    """
    Setup logging configuration.
    ENV - prod, stage, dev (see logging.yaml)
    """
    value = os.getenv('ENV', None)
    # Load the config file
    with open('crypto_data_provider/utils/logging.yaml', 'rt', encoding="utf-8") as file:
        yaml_config = yaml.safe_load(file.read())
        config.dictConfig(yaml_config)
    if value:
        return logging.getLogger(value.lower())
    return logging.getLogger('prod')
