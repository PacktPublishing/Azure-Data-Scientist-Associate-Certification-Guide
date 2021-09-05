from azureml.core.run import Run
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=int, dest="a", help="The alpha parameter")
parser.add_argument("--b", type=int, dest="b", help="The beta parameter")
args = parser.parse_args()

# Produce bad values if 'a' greater than 2
if (args.a > 2):
    args.a = 0

run = Run.get_context()


def fake_train(run, a, b):
    time.sleep(5)
    metric = a + b
    run.log("fake_metric", metric)


for epoch in range(20):
    fake_train(run, args.a * epoch, args.b)
