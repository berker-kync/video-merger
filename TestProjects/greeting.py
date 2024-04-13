# https://www.youtube.com/watch?v=aGy7U5ItLRk

import argparse
from argparse import ArgumentParser, Namespace

# # argparse objesi 
# parser = argparse.ArgumentParser(description='A simple greeting program')
# # argparse argumentı
# parser.add_argument('name', type=str, help='Your name')


# args = parser.parse_args()
# print(f"Hello, {args.name}!")


parser = ArgumentParser()
parser.add_argument('square', help='squares number', type=int)
args: Namespace = parser.parse_args()

print(args.square ** 2)



