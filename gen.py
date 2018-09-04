'''
Author: Alexey Avdeev.
'''

from itertools import product, combinations_with_replacement
from random import shuffle
from getopt import getopt, GetoptError
import sys

range_to_generate = 20
columns = 4
addition = True
shuffle_list = True

def generate_list_addition(range_to_generate):
    ret = []
    b = list(product(range(1 + range_to_generate // 2), repeat = 2))
    for pair in b:
        ret.append('%d + %d = ' % pair)
    return ret

def generate_list_substraction(range_to_generate):
    ret = []
    b = list(combinations_with_replacement(range(range_to_generate, -1, -1), 2))
    for pair in b:
        ret.append('%d - %d = ' % pair)
    return ret

def split_list(list_to_split, k):
    b = []

    if (shuffle_list):
        shuffle(list_to_split)

    ran = (len(list_to_split) // k)
    if (len(list_to_split) % k > 0):
        ran += 1
    for i in range(ran):
        b.append(','.join(list_to_split[i * k: (i + 1) * k]))

    elements_in_last_line = len(list_to_split) % k
    if elements_in_last_line != 0:
        b[-1] = b[-1] + ',' * (k - elements_in_last_line)

    return b

try:
    opts, args = getopt(sys.argv[1:], 's', ['operation=', 'columns=', 'range='])
except GetoptError:
    print 'Something went wrong here...'

for opt, arg in opts:
    if opt in ('--operation'):
        if arg == 'substraction':
            addition = False
    elif opt in ('--columns'):
        columns = int(arg)
    elif opt in ('--range'):
        range_to_generate = int(arg)
    elif opt in ('-s'):
        shuffle_list = False

if addition:
    generated_list = generate_list_addition(range_to_generate)
else:
    generated_list = generate_list_substraction(range_to_generate)

print '\n'.join(split_list(generated_list, columns))
