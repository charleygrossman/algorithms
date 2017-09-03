# Select the ith-order statistic from a list of elements
def randomized_selection(arr, e):
    n = len(arr)-1
    if n <= 1: return

    p = partition(arr, 0, n)

def partition(arr, lo, hi):
