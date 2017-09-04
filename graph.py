# NOTE: WIP (Currently just an adjaceny list maker)

def main():
    print("Enter [q] to quit")

    while True:
        sets = input("Enter a list of vertices separated by space to " +
        "denote edges from the first in the list to the rest, and separate " +
        "multiple lists by commas: ").split(",")
        if sets[0] == "q": break

        adjList = [0] * len(sets)
        for s in sets:
            tmp = s.split()
            tmp = [int(x) for x in tmp]
            adjList[tmp[0]] = tmp[1:]



if __name__ == "__main__":
    main()
