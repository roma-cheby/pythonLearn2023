class Redirect():
    def __init__(self, errors):
        self.errors = errors
    def __enter__(self):
        return 1
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.errors or Exception in self.errors:
            return 1

print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')


with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')


print('Hello stdout again')
raise Exception('Hello stderr')