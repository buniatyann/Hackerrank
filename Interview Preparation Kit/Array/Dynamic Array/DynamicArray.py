# Time Complexity: O(q)
# Space Complexity: O(n + q)
# Where q is the number of queries
def dynamicArray(n, queries):
    l = [[] for _ in range(n)]  # Initialize n empty lists
    result = []  # Stores results of type 2 queries
    last_answer = 0  # Keeps track of the last retrieved answer

    for query in queries:
        a = (last_answer ^ query[1]) % n  # Compute index

        if query[0] == 1:
            # Type 1: Append query[2] to the corresponding list
            l[a].append(query[2])
        elif query[0] == 2:
            # Type 2: Retrieve value using modular indexing
            last_answer = l[a][query[2] % len(l[a])]
            result.append(last_answer)

    return result
