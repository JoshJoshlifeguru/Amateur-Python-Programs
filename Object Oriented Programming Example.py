import time

# set the mold or qualities of your object
class Robots:
    def __init__ (self, name, type, build_year, purpose, status):
        self.name = name
        self.type = type
        self.build_year = build_year
        self.purpose = purpose
        self.status = status

  # a function your finished object can execute
    def introduce_self(self):
        print(f"Name: {self.name}. Built: {self.build_year}. Purpose: {self.purpose}. Status: {self.status}.")

# here we're going to let the user build their own robot
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
    
