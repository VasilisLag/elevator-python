from Elevator import Elevator
from Generator import Generator

# Checks if all people have been served - true/false
def finished():
  passengers = 0
  for i in header:
    for k in i:
      passengers = passengers + 1
  if passengers > 0:
    return False
  else:
    return True

# Returns total(int) number of passengers that are waiting in the queue 
def count_passengers():
  passengers = 0
  for i in header:
    for k in i:
      passengers = passengers + 1
  return passengers

# Print status of people waiting in each floor for visualization purposes
def print_status():
  for i in header:
    print(i)

# Initialization of values - elevator starts from 0
floor = 0
num_of_floors = -1
elevator_capacity = -1

# Initialization of generator for the creation of the queues - text files
generator = Generator()



# Get number of floors - validate
print("Type the number of floors(>1): ")
num_of_floors = int(input())
while num_of_floors < 2:
    print("Number of floors must be over 1, please type again: ")
    num_of_floors = int(input())


generator.create_sample(num_of_floors)

# Get elevator capacity - validate
print("Type the capacity of the elevator(>0): ")
elevator_capacity = int(input())
while elevator_capacity < 1:
    print("The capacity of the elevator must be over 0, please type again: ")
    elevator_capacity = int(input())

# Simple print for informational purposes
print("The number of floors is:" , num_of_floors)
print("The capacity of the elevator is: " , elevator_capacity)

# Creating a variable number of lists, based on user's input
header_count = num_of_floors + 1
header = []
for i in range(header_count):
  header.append([])

# Reading the generated file as 2-dimensional list
with open(f"./queues{num_of_floors}.txt", "r") as file:
  count = 0
  k = file.readlines()
  for i in k:
    # Reading the line with split in order to get values seperated by comma .split(",")
    # and "throwing" the change of line char .strip("\n")
    header[count] = [*i.strip("\n").split(',')]
    count = count + 1

# Initializing the elevator object using Elevator class 
elevator = Elevator(elevator_capacity, num_of_floors)


# General idea of elevator is that while there are passengers to serve
# 1. The elevator gets people who are willing to move to its direction as long as they fit in elevator's capacity
# When people get on the elevator they are removed from the waiting queue
# 2. The elevator moves, floor by floor, in the direction it should (see Generator.py for the checks made and the logic)
# 3. The elevator leaves people to their wanted floor and then the iteration begins again 
# 4. Print report is used for visualization purposes after getting and leaving people
while(not finished()):
    for p in header[floor].copy():
        if(elevator.get_people(int(p))):
          header[floor].remove(p)
    elevator.print_report()
    floor = elevator.move()
    elevator.print_report()
    elevator.remove_people()
    print("---------------------------------------------------------------------------")
    print(f"Number of people to be served {count_passengers()}")
    print_status()
    print("---------------------------------------------------------------------------")
  
print("Everyone was served!")

  
