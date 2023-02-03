from sym import Sym
from num import Num
from utils import rand ,rint, rnd, show, get_repgrid_file_contents
from data import Data, rep_cols
from csv import get_csv_rows
from globals import global_options, K_FILE, K_DEFAULT_DATA_FILE
from collections import OrderedDict

import copy

# _all_ = ['test_global_options', 'test_num', 'test_sym', 'test_get_stats', 'read_from_csv', 'read_data_csv', 'test_around', 'test_half', 'test_cluster', 'test_optimize' ]

def test_global_options() -> bool:
    print(global_options)
    return True

def test_num() -> bool:
    num=Num()
    nums=[1,1,1,1,2,2,3]
    for i in nums:
        num.add(i)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

def test_sym() -> bool:
    sym=Sym()
    symbols=["a","a","a","a","b","b","c"]
    for s in symbols:
        sym.add(s)
    return ("a"==sym.mid() and 1.379 == rnd(sym.div()))

def test_get_stats():
    data = Data(global_options[K_FILE])
    x_div={}
    x_mid={}
    y_div={}
    y_mid={}
    
    for col in data.cols.x:
        col = [col]
        mid_temp = data.stats(2, col, True)
        x_mid[mid_temp[0][0]] = mid_temp[0][1]
        div_temp = data.stats(2, col, False)
        x_div[div_temp[0][0]] = div_temp[0][1]

    for col in data.cols.y :
        col = [col]
        mid_temp = data.stats(2, col, True)
        y_mid[mid_temp[0][0]] = mid_temp[0][1]
        div_temp = data.stats(2, col, False)
        y_div[div_temp[0][0]] = div_temp[0][1]
    x_mid = OrderedDict(sorted(x_mid.items()))
    x_div = OrderedDict(sorted(x_div.items()))
    x_mid_p = {}
    x_div_p = {}
    for i in x_mid:
        x_mid_p[i] = x_mid[i]
        x_div_p[i] = x_div[i]
    y_mid = OrderedDict(sorted(y_mid.items()))
    y_div = OrderedDict(sorted(y_div.items()))
    y_mid_p = {}
    y_div_p = {}
    for i in y_mid:
        y_mid_p[i] = y_mid[i]
        y_div_p[i] = y_div[i]
    print("x")
    print(f"x \t mid \t {x_mid_p}")
    print(f"  \t div \t {x_div_p}")
    print("y")
    print(f"y \t mid \t {y_mid_p}")
    print(f"  \t div \t {y_div_p}")

    return True


def test_read_from_csv():    
    rows = get_csv_rows(global_options[K_FILE])
    total_rows = len(rows)
    total_columns = len(rows[0])
    return total_columns*total_rows==8*399

def test_read_data_csv():
    data = Data(global_options[K_FILE])
    return (len(data.rows)==398) and (data.cols.x[0].at==0) and (len(data.cols.x)==4) and (data.cols.y[0].wt==-1) 

def test_around():
    data = Data(global_options[K_FILE])
    print("0   0 ", data.rows[0])
    A = data.around(data.rows[0])
    
    for i in range(len(A)):
        if (i+1)%50 == 0 :
            print(i+1, rnd( data.dist(A[i],data.rows[0]),2), A[i])
    return True

def test_half():
    data = Data(global_options[K_FILE])
    left,right,A,B,mid,c = data.half()
    print(len(left), len(right), len(data.rows))
    print(A,c)
    print(mid)
    print(B)
    return True

def test_cluster():
    """ N-Level bi-Clustering """
    data = Data(global_options[K_FILE])
    show(data.cluster(), cols =  data.cols.y, nPlaces = 1, is_mid = True)
    return True

def test_optimize():
    """ Semi-Supervised Optimization"""
    data = Data(global_options[K_FILE])
    show(data.sway(), cols = data.cols.y, nPlaces = 1, is_mid = True)
    return True

def test_copy():
    table_1 = dict(a=1, b=dict(c=2, d=[3]))
    table_2 = copy.deepcopy(table_1)
    table_2['b']['d'][0]=1000
    print("before: ", table_1)
    print("after: ", table_2)
    return True

def test_rep_cols():
    contents = get_repgrid_file_contents(global_options[K_FILE])
    rep_data = rep_cols(contents['cols'])
    rep_data.cols.print_cols()
    return True

def test_synonyms():
    print("TODO - TEST SYNONYMS")
    return True

def test_rep_rows():
    print("TODO - TEST REP ROWS")
    return True

def test_prototypes():
    print("TODO - TEST PROTOTYPES")
    return True

def test_position():
    print("TODO - TEST POSITION")
    return True

def test_every():
    print("TODO - TEST EVERY")
    return True

