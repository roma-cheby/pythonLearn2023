import sys

class Redirect():
    def __init__(self, stdout, stderr):
        self.strout = stdout
        self.stderr = stderr
    def __enter__(self):
        sys.stdout = self.strout
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr = self.stderr

print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')


with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')


print('Hello stdout again')
raise Exception('Hello stderr')