import argparse
from ast import parse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num', 
        type = int,
        required=True,
        help='input for the multiplyby9 function'
    )
    args = parser.parse_args()
    return args

def printHello():
    print("Hello World!") #no input/output have only process

def multiplyby9(inputV):
    print(9*inputV) # have input and process

if __name__=="__main__":

    input_v = parse_input()
    print(f'the input num is {input_v.num}')

    print("we are in the main function") #control program's flow
    multiplyby9(20)
    printHello()