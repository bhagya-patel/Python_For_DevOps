# Get the Environment from the User and print it


for i in range(5):
    env = input("Please enter the environment you are working in: ")

    print(f"The user inputted environment is: {env}")

    if env == "production":
        print("Don't Deploy On Friday")
    elif env == "staging":
        print("Take backup and test well before deploying")
    else:
        print("This is a non production environment, you can deploy without worry")

