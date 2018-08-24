LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s - %(asctime)s - %(messageId)s - %(userId)s - %(module)s - %(funcName)s() - %(lineno)d] - %(message)s'
        },
    },
    'filters': {
        'custom': {
            '()': 'handlers.applicationLogger.ContextFilter'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'triniti': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'filter': 'custom',
            'propagate': False
        },
        'root': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
    }
}
