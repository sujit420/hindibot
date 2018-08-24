import logging.handlers
import traceback
import logging
import logging.config
import loggingConfig
from handlers import applicationLogger

logging.config.dictConfig(loggingConfig.LOGGING)

logger = logging.getLogger("Bot")
logger.addFilter(applicationLogger.ContextFilter())


def log_traceback():
    trace_back = traceback.format_exc().split("\n")
    trace_back.pop()  # removing empty string
    for line in trace_back:
        logger.error(line)
