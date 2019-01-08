# Compute the maximum weight independent set of a path graph
#
#
# A maximum weight independent set of a path graph is the set of non-adjacent
# nodes with a maximal sum of their combined weights


def main():
    # [(node, weight)]
    data = []
    try:
        with open('mwis.txt') as file:
            node = 1
            for line in file.readlines()[1:]:
                weight = int(line.strip())
                data.append((node, weight))
                node += 1
    except:
        raise
    max_wis_path = max_wis(data)
    max_wis_weight = sum([data[node-1][1] for node in max_wis_path])
    print('Path: {} Weight: {}'.format(max_wis_path, max_wis_weight))


def max_wis(data):
    weights = get_weights(data)
    path = get_path(data, weights)
    return path


# S[i] = max{S[i-1], S[i-2] + w_i}
def get_weights(data):
    S = [0, data[0][1]]
    for i in range(2, len(data)+1):
        G_1_wis = S[i-1]
        G_2_wis = S[i-2] + data[i-1][1]
        if G_1_wis >= G_2_wis:
            S.append(G_1_wis)
        else:
            S.append(G_2_wis)
    return S


# Reconstruction of the path given the weights
# NOTE: S contains the weight for the empty set, so it has one more element than weights
def get_path(data, weights):
    S = []
    i = len(weights)-1
    while i > 0:
        if weights[i-1] >= weights[i-2] + data[i-1][1]:
            i -= 1
        else:
            S.append(data[i-1][0])
            i -= 2
    return S[::-1]


if __name__ == '__main__':
    main()
