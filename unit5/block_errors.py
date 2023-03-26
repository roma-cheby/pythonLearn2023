class BlockErrors():
    def __init__(self, errors):
        self.errors = errors
    def __enter__(self):
        return 1
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.errors or Exception in self.errors:
            return 1
