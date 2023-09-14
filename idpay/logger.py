# -*- coding: utf-8 -*-

import sys
import logging


def GetLogger():
    logLevel = logging.INFO
    logformat = logging.Formatter("[IDPAY - %(levelname)s] [%(asctime)s] - %(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logLevel)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logLevel)
    handler.setFormatter(logformat)
    logger.addHandler(handler)  
    return logger