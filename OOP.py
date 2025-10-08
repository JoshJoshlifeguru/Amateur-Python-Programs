import time
class Robots:

    # define the qualities and traits "a mold" for how you object is to be constructed
    def __init__ (self, name, type, build_year, purpose, status):
        self.name = name
        self.type = type
        self.build_year = build_year
        self.purpose = purpose
        self.status = status

    # define a function your finished object can do
    def introduce_self(self):
        print(f"Hello, I am {self.name}. I was built in {self.build_year}. My purpose is {self.purpose}. My current status is {self.status}.")

# with this function, we can allow the user to build their own object in realtime
def build_robot():
    try:
        Name = input("Enter a name for your robot: ")
        Type = input("Enter the type of your robot (e.g., Autonomous, Humanoid): ")
        Build_year = int(input("Enter the year your robot was built: "))
    except ValueError:
            print("Invalid input for build year. Please enter a valid year.")
            return None
    Purpose = input("Enter the purpose of your robot (e.g., Household chores, Security): ")
    Status = input("Enter the current status of your robot (e.g., Active, Inactive): ")
    finished_robot = Robots(Name, Type, Build_year, Purpose, Status)
    print("building robot...")
    time.sleep(4)
    print("Robot successfully built!")
    def greet():
        try:
            ask = input("Would you like your robot to introduce itself? (yes/no): ")
            if ask.lower() == 'yes':  
                finished_robot.introduce_self()
            elif ask.lower() == 'no':
                print("Okay, your robot will remain silent.")
        except ValueError:
                    print("Invalid input. Please respond with 'yes' or 'no'.")
        return
    greet()
    
build_robot()

    
