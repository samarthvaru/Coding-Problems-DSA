def star(rows):
    for i in range(1, rows + 1):
        # Print spaces before the stars
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        # Move to the next line
        print()

star(9)