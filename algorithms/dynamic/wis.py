# Compute the maximum-weight independent set of a path graph, which is
# the set of non-adjacent nodes with a maximal sum of their combined weights


import sys


def main():
    data = _input()
    max_wis_path = max_wis(data)
    max_wis_weight = sum([data[node-1][1] for node in max_wis_path])

    print('Path: {}\nWeight: {}'.format(max_wis_path, max_wis_weight))


def max_wis(data):
    weights = get_weights(data)
    return get_path(data, weights)


# S[i] = max{S[i-1], S[i-2] + w_i}
def get_weights(data):
    S = [0, data[0][1]]

    for i in range(2, len(data)+1):
        g1_wis = S[i-1]
        g2_wis = S[i-2] + data[i-1][1]

        if g1_wis >= g2_wis:
            S.append(g1_wis)
        else:
            S.append(g2_wis)

    return S


# Reconstruction of the path given the weights.
# S contains the weight for the empty set, so it has one more element than weights
def get_path(data, weights):
    S = []
    i = len(weights) - 1

    while i > 0:
        if weights[i-1] >= weights[i-2] + data[i-1][1]:
            i -= 1
        else:
            S.append(data[i-1][0])
            i -= 2

    return S[::-1]


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        data = []
        node = 1

        for line in f.readlines()[1:]:
            weight = int(line.strip())
            data.append((node, weight))
            node += 1

        return data


if __name__ == '__main__':
    main()
