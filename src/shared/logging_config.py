LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters" : {
        "default": {
            "format": "%(asctime)s %(levelname)s %(name)s - %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "uvicorn": {"level": "INFO", "handlers": ["default"], "propagate": False},
        "uvicorn.error": {"level": "INFO", "handlers": ["default"], "propagate": False},
        "uvicorn.access": {"level": "INFO", "handlers": ["access"], "propagate": False},
    },
    "root": {"level": "INFO", "handlers": ["access"], "propagate": False},
}