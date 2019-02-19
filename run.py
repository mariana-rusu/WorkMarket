import HTMLTestRunner
import datetime
import fnmatch
import os
import unittest

class Run_all_Tests(unittest.TestCase):

     def tests_runner(self):


        self.suite = unittest.TestSuite()

        module_names = all_test_modules('./src', '*.py')
        tests = [unittest.defaultTestLoader.loadTestsFromName(mname) for mname
                  in module_names]

        print(tests)
        self.suite.addTests(tests)

        # Invoke TestRunner
        file_name = "{}-report.html".format(datetime.datetime.now().date())

        buf = open(file_name, "wb")

        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='Regression tests {}'.format(datetime.datetime.now()),
                    description=''
                    )
        runner.run(self.suite)




def all_test_modules(root_dir, pattern):
    test_file_names = all_files_in(root_dir, pattern)
    return [path_to_module(str) for str in test_file_names]

def all_files_in(root_dir, pattern):
    matches = []

    for root, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))

    return matches

def path_to_module(py_file):
    return strip_leading_dots( \
        replace_slash_by_dot(  \
            strip_extension(py_file)))

def strip_extension(py_file):
    return py_file[0:len(py_file) - len('.py')]

def replace_slash_by_dot(str):
    return str.replace('\\', '.').replace('/', '.')

def strip_leading_dots(str):
    while str.startswith('.'):
       str = str[1:len(str)]
    return str



if __name__ == "__main__":
    Run_all_Tests().tests_runner()