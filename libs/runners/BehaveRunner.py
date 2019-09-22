from os import mkdir
from datetime import datetime
from behave.__main__ import main as behave_main

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", "--tags", default=None, help="Desired tags to run, multiple tags logic not implemented now")

args = parser.parse_args()
tags = args.tags
if tags is not None:
    tags =  '-t @' + tags
    print('Running test with tags :' + args.tags)    
else:
    tags = ''
    print('Running all tests')

report_path =  './../reports/' + datetime.now().strftime("%d%m%Y_%H%M%S") + '/report.junit'
print('Report will be saved to ' + report_path)
behave_main(['./features', tags, '--junit', '-o ' + report_path])