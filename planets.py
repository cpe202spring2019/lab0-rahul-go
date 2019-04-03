def weight_on_planets():
    try:
        # Weight on earth (pounds)
        weight = int(input("What do you weigh on earth? "))
    except ValueError:
        print("Invalid input!")
    else:
        print("\nOn Mars you would weigh", weight * 0.38, "pounds."             # Weight on Mars (pounds)
              "\nOn Jupiter you would weigh", weight * 2.34, "pounds.")         # Weight on Jupiter (pounds)



if __name__ == '__main__':
    weight_on_planets()