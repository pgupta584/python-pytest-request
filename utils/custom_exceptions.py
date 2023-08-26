class SessionTimesOutException(Exception):
    """Exception raised for errors in case Session times out """
    def __init__(self, message=None):
        self.message = message
        super().__init__(self.message)
