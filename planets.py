def weight_on_planets():
	while(True):
	    try:
	        # Weight on earth (pounds)
	        weight = int(input("What do you weigh on earth? "))
	    except ValueError:
	        print("Invalid input, try again!")
	    else:
	        print("\nOn Mars you would weigh", weight * 0.38, "pounds."             # Weight on Mars (pounds)
	              "\nOn Jupiter you would weigh", weight * 2.34, "pounds.")         # Weight on Jupiter (pounds)
	        break



if __name__ == '__main__':
    weight_on_planets()