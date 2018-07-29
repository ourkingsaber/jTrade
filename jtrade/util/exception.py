

class JtradeError(Exception):
    """Base Error in this library"""
    pass


class NoDataError(JtradeError):
    """Exception raised when there is no data for query."""

    def __init__(self, message):
        super().__init__(message)