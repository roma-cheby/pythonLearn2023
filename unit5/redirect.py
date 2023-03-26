import subprocess
import sys
import traceback


class Redirect():
    def __init__(self, stdout = sys.stdout, stderr=sys.stderr):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr
    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
    def __exit__(self, exc_type, exc_val, exc_tb):
        traceback.print_exc()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        return 1

print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')


with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')

print('Hello stdout again')
raise Exception('Hello stderr')