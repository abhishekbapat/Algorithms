import random
import string
import math
from datetime import datetime

import Lib.sorters as sorters
import Lib.string_matchers as matchers
import Lib.graph_search as searchers


def sorter_tester():
    inp = []
    for i in range(10000):
        inp.append(random.randint(0, 2000000))
    max_inp = max(inp)
    start = datetime.now()
    ans = sorters.radix_sort(inp, arr_max=max_inp)
    end = datetime.now()
    print("Report:")
    print(f"Start time: {start}")
    print(f"End time: {end}")
    print(f"Input: {inp}")
    print(f"Output {ans}")
    print(f"Time taken: {end - start}")


def string_tester():
    inp = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(1000000))
    inp_len = len(inp)
    pattern = inp[inp_len - 100:inp_len - 1]
    start = datetime.now()
    match = matchers.string_match(inp, pattern)
    end = datetime.now()
    if match:
        print(f"Pattern exists in input.")
    else:
        print(f"Pattern does exist in input.")

    print(f"Start time: {start}")
    print(f"End time: {end}")
    print(f"Time taken: {end - start}")


def graph_tester():
    adj = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'a': 2, 'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7},
           'e': {'d': 9}}
    initial_point = 'a'
    q = {'a': 0, 'b': math.inf, 'c': math.inf, 'd': math.inf, 'e': math.inf}  # node having 0 as value will be
    # treated as starting point
    ans = searchers.dijkstra(q, adj)
    print(f"Ans: {ans}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sorter_tester()
    # string_tester()
    graph_tester()
