import json
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", type=str, help="Input File")
parser.add_argument("-o","--output", type=str, help="Output File")
parser.add_argument("-s","--samples", type=str, nargs="+", help="Samples to output")
args = parser.parse_args()

print(args.input)
exec(open(args.input))

out = {k:v for k,v in samples.items() if k in args.samples}

json.dump(out, open(args.output, "w"), indent=4)