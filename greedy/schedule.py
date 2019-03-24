# Minimizing weighted sum of completion times for scheduled jobs
import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    wl = []
    with open(os.path.join(BASE_DIR, 'test/schedule.txt')) as file:
        for line in file.readlines()[1:]:
            w, l = map(int, line.strip().split())
            wl.append((w, l))
    print('By difference: {}'.format(order_by_difference(wl)))
    print('By ratio: {}'.format(order_by_ratio(wl)))


# NOTE: This greedy approach is not always optimal
# Order by decreasing values of (weight - length), then take weighted sum
# sum(weight*C). NOTE: If two jobs have equal difference, schedule the job
# with higher weight first
def order_by_difference(wl):
    wl_ordered = sorted(wl, key=lambda x: x[0] - x[1], reverse=True)
    schedule = []
    same_dist = []
    dist = wl_ordered[0][0] - wl_ordered[0][1]
    for x in wl_ordered:
        if x[0] - x[1] == dist:
            same_dist.append(x)
        else:
            same_dist.sort(key=lambda x: x[0], reverse=True)
            for y in same_dist:
                schedule.append(y)
            same_dist = [x]
            dist = x[0] - x[1]
    same_dist.sort(key=lambda x: x[0], reverse=True)
    for y in same_dist:
        schedule.append(y)
    return weighted_sum(schedule)


# NOTE: This greedy approach IS always optimal
# Order by decreasing values of (weight/length), then take weighted sum
# sum(weight*C)
def order_by_ratio(wl):
    wl_ordered = sorted(wl, key=lambda x: x[0] / x[1], reverse=True)
    return weighted_sum(wl_ordered)


def weighted_sum(wl):
    weighted_sum = 0
    length = 0
    for x in wl:
        length += x[1]
        weighted_sum += x[0] * length
    return weighted_sum


if __name__ == '__main__':
    main()
