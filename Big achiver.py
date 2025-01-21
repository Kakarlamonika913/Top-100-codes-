def is_happy(test_cases):

    results = []

    for t in test_cases:

        N, A = t

        max_so_far = A[0]

        happy = [1]

        for i in range(1, N):

            if A[i] > max_so_far:

                happy.append(1)

                max_so_far = A[i]

            else:

                happy.append(0)

        results.append(' '.join(map(str, happy)))

    return results



T = int(input())

test_cases = []

for _ in range(T):

    N = int(input())

    A = list(map(int, input().split()))

    test_cases.append((N, A))





results = is_happy(test_cases)





for result in results:

    print(result)
