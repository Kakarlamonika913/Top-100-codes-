def print_pyramid_pattern(n):
        for i in range(1, n + 1):
            for j in range(n - i):
                print(" ", end=" ")
            for j in range(i):
                print(chr(65 + j), end=" ")
            for j in range(i - 2, -1, -1):
                 print(chr(65 + j), end=" ")

            print()


    n = 4
    print_pyramid_pattern(n)
