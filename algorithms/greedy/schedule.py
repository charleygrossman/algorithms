# Minimize the weighted sum of completion times for scheduled tasks
# (a comparison of a suboptimal greedy strategy versus an optimal one)


import sys


def main():
    data = _input()

    suboptimal_solution = order_by_difference(data)
    optimal_solution = order_by_ratio(data)

    print('Suboptimal solution by difference: {}'.format(suboptimal_solution))
    print('Optimal solution by ratio: {}'.format(optimal_solution))


# This greedy approach is not always optimal.
# Order by decreasing values of (weight - length), then take weighted sum sum(weight*C).
# If two jobs have equal difference, schedule the job with higher weight first
def order_by_difference(wl):
    schedule = []
    same_dist = []
    wl_ordered = sorted(wl, key=lambda _: _[0] - _[1], reverse=True)
    dist = wl_ordered[0][0] - wl_ordered[0][1]

    for x in wl_ordered:
        if x[0] - x[1] == dist:
            same_dist.append(x)
        else:
            same_dist.sort(key=lambda _: _[0], reverse=True)

            for y in same_dist:
                schedule.append(y)

            same_dist = [x]
            dist = x[0] - x[1]

    same_dist.sort(key=lambda _: _[0], reverse=True)

    for y in same_dist:
        schedule.append(y)

    return weighted_sum(schedule)


# This greedy approach IS always optimal.
# Order by decreasing values of (weight/length), then take weighted sum sum(weight*C)
def order_by_ratio(wl):
    wl_ordered = sorted(wl, key=lambda _: _[0] / _[1], reverse=True)

    return weighted_sum(wl_ordered)


def weighted_sum(wl):
    ws = 0
    length = 0

    for x in wl:
        length += x[1]
        ws += x[0] * length

    return ws


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        data = []

        for line in f.readlines()[1:]:
            w, l = map(int, line.strip().split())
            data.append((w, l))

        return data


if __name__ == '__main__':
    main()
