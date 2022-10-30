'''
from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer

def gcd(a: int, b: int) -> int:
    if a < b:
        c: int = a
        a = b
        b = c

    while b != 0:
        c: int = a
        a = b
        b = c % b

    return a

gcd_fuzzer = AdvancedSymbolicFuzzer(gcd, max_tries=10, max_iter=10,max_depth=10)

for i in range(10):
    args = gcd_fuzzer.fuzz()
    # a = args['a'].as_long()
    a = args['a'].as_long()
    b = args['b'].as_long()
    d = gcd(a, b)
    print(f"gcd({a}, {b}) = {d}")
    # print(args)

import inspect
from fuzzingbook.ControlFlow import PyCFG, to_graph, gen_cfg

def check_triangle(a: int, b: int, c: int) -> str:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"

def show_cfg(fn, **kwargs):
    return to_graph(gen_cfg(inspect.getsource(fn)), **kwargs)

show_cfg(check_triangle)
'''
import inspect
from fuzzingbook import Fuzzer
from fuzzingbook.ControlFlow import PyCFG, to_graph, gen_cfg


def check_triangle(a: int, b: int, c: int) -> str:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"
    

