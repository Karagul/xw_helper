import string
import pandas as pd
import numpy as np
from sympy import symbols
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


def make_mapping(table, edge=(1,1)):
    '''
    Constructs a mapping matrix with symbolic excel fields
    '''
    # better with generators..
    sz = table.shape
    idx = np.arange(edge[0],edge[0]+sz[0]).astype(str)
    tdx = list(string.ascii_uppercase[edge[1]:edge[1]+sz[1]])
    return pd.DataFrame([[ symbols(x + y)  for x in tdx] for y in idx], columns=table.columns)

def clc(x):
    '''
    Creates a symbolic formula
    '''
    return x.apply(lambda x: '='+str(x))


if __name__=='__main__':
    table = pd.DataFrame({'price':[3,4,5,6], 'stu':[1,2,2,3]})
    m = make_mapping(table, edge=(10,10))
    table['test'] = clc((m['price']+m['stu'])/m['stu'])
