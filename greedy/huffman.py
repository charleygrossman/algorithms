# Find the maximum and minimum lengths of huffman-encoded symbols in a language S.
# At each step, symbols a and b are merged to ab. There are three cases:
# 1. a and b are from S
# 2. One is from s and the other is from S' (it's been previously merged)
# 3. Both are from their own S'


import sys


def main():
    data = _input()

    depths = {x[0]: 0 for x in data}
    depths_merged = merge(data, depths)
    vals = sorted(list(depths_merged.values()))
    
    print('Maximum depth: {}\nMinimum depth: {}'.format(vals[-1], vals[0]))


def merge(data, depths):
    while len(data) > 1:
        # Get two smallest-weighted nodes
        tmp = data.copy()
        tmp.sort(key=lambda _: _[1])
        x = tmp[0]
        y = tmp[1]

        # Update the atomics of the two smallest-weighted nodes depth
        update_depths(depths, x[0])
        update_depths(depths, y[0])

        # Merge two smallest-weighted nodes and add to data.
        # Remove the two original from data
        symbol_xy = get_symbol(x[0], y[0])
        xy = (symbol_xy, x[1] + y[1])
        tmp = [xy] + tmp[2:]
        data = tmp

    return depths


# Anytime a node is seen by merge(), its depth increases by 1
def update_depths(depths, symbol):
    for atomic in symbol.split(','):
        depths[atomic] += 1


def get_symbol(v1, v2=None):
    return str(v1) if not v2 else str(v1) + ',' + str(v2)


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        data = []
        i = 1

        for line in f.readlines()[1:]:
            weight = int(line.strip())
            symbol = get_symbol(i)

            data.append((symbol, weight))
            i += 1

        return data


if __name__ == '__main__':
    main()
