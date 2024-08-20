def print_right_angle_triangle():
    for i in range(1, 6):
        sequence = "1" * i if i % 2 != 0 else "0" * (i // 2) + "1" * (i // 2)
        print(sequence)
print_right_angle_triangle()
