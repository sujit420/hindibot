import logging.handlers


class ContextFilter(logging.Filter):
    """
    This is a filter is used to inject user id into the log.
    """
    userId = None
    messageId = None

    def filter(self, record):
        record.userId = ContextFilter.userId
        record.messageId = ContextFilter.messageId
        return True
