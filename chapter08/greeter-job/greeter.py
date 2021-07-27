import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--greet-name', type=str, 
                    dest='name', help='The name to greet')
args = parser.parse_args()

name = args.name

print(f"Hello {name}!")
