import argparse
from asciistuff import Banner 
import os

parser = argparse.ArgumentParser()
parser.add_argument('--greet-name', type=str, 
                    dest='name', help='The name to greet')
args = parser.parse_args()

name = args.name
greet_header = os.environ.get('GREET_HEADER','Message:')

print(greet_header)
print(Banner(f"Hello {name}!"))
