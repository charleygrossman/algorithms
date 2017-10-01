def main():
    print("Enter [q] to quit")
    print("This uses an adjaceny-list representation of a graph")

    while True:
        sets = input("Build your graph by entering a list of vertices separated" +
        " by space to denote edges from the first in the list to the rest," +
        " and separate multiple lists by commas: ").split(",")
        if sets[0] == "q": break

        # Build the graph G as an adjaceny-list
        G = [0] * len(sets)
        for s in sets:
            tmp = s.split()
            tmp = [int(x) for x in tmp]
            G[tmp[0]] = tmp[1:]

if __name__ == "__main__":
    main()
