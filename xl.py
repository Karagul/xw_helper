import string
import pandas as pd
import numpy as np
from sympy import symbols, sympify
import itertools

# # define the generator itself
# def iter_all_strings():
#     size = 1
#     while True:
#         for s in itertools.product(ascii_lowercase, repeat=size):
#             yield "".join(s)
#         size +=1
#
# def label_gen():
#     for s in gen:
#         return s


def make_mapping(table, edge=(1, 1)):
    '''
    Constructs a mapping matrix with symbolic excel fields
    '''
    # better with generators..
    sz = table.shape
    idx = np.arange(edge[0] + 1, edge[0] + sz[0]).astype(str)
    tdx = list(string.ascii_uppercase[edge[1]:edge[1]+sz[1]])
    return pd.DataFrame([[ x + y  for x in tdx] for y in idx], columns=table.columns)

def clc(expression):
    '''
    Parses the input string expression into an excel formula with correct cell references
    '''
    return eval(("'" + expression + "'").replace('{',  "'+m['").replace('}', "']+'"))


if __name__=='__main__':
    tabl = pd.DataFrame({'price':np.arange(1, 500), 'stu':np.arange(1, 500)})
    m = make_mapping(tabl, edge=(0, 0))

    
    tabl['test'] = clc(' =BDP({price},{stu})^3 ') # set an excel formula for a full column
    print(tabl)
