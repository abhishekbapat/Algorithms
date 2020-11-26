from datetime import datetime
import random, string
import Lib.sorters as sorters
import Lib.string_matchers as matchers


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
    print(f"Time taken: {end-start}")


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sorter_tester()
    string_tester()
