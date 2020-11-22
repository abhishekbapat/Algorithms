from datetime import datetime
import random
import Lib.sorters as sorters


def tester():
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
    print(f"Time taken: {end-start}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tester()
