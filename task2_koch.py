import turtle


def koch_curve(length, level):
    """Draw one side of the Koch snowflake."""

    if level == 0:
        turtle.forward(length)
        return

    koch_curve(length / 3, level - 1)

    turtle.left(60)

    koch_curve(length / 3, level - 1)

    turtle.right(120)

    koch_curve(length / 3, level - 1)

    turtle.left(60)

    koch_curve(length / 3, level - 1)



def koch_snowflake(length, level):
    """Draw the complete Koch snowflake."""

    koch_curve(length, level)

    turtle.right(120)

    koch_curve(length, level)

    turtle.right(120)

    koch_curve(length, level)


def main():

    print("=" * 40)
    print("          Koch Snowflake")
    print("=" * 40)

    while True:

        try:
            level = int(
                input("Enter recursion level (0-6): ")
            )

            if 0 <= level <= 6:
                break

            print("Please enter a number between 0 and 6.")

        except ValueError:
            print("Please enter an integer.")

    while True:

        try:
            print("\nEnter snowflake size:")
            print("(Recommended: 100–500 for better visibility)")

            length = float(input("> "))

            if length <= 0:
                print("Snowflake size must be greater than 0.")
                continue

            if length > 1000:
                print("Warning: A very large snowflake may not fit in the window.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print("\nPlease wait while the snowflake is being drawn...")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.setheading(0)
    turtle.pendown()
    koch_snowflake(length, level)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()