import time

class Elevator :

    # Constructor  of Elevator class
    def __init__(self, capacity, num_floors):
        self.capacity = capacity
        self.floor = 0
        # List of people on the elevator
        self.passengers = []
        self.total_floors = num_floors
        self.direction = "up"
    
    # get_people(): The idea here is to take people as long as they want to move in elevator's direction
    # and as long as they fit in the capacity
    # In any other case people don't get aboard - false is returned
    def get_people(self, wanted_floor):

        if int(wanted_floor) > self.floor:
          person_dir = "up"
        else:
          person_dir = "down"
        if len(self.passengers) < self.capacity and self.direction == person_dir:
          self.passengers.append(wanted_floor)
          return True
        elif len(self.passengers) >= self.capacity :
        
          return False
        else:

          return False
    
    # remove_people(): This function leaves people to their floor, so the basic check is if the
    # current floor of the elevator is equal to the passengers', remove() is used then
    def remove_people(self):
        count = 0
        for p in self.passengers.copy():
            if self.floor == p:
                self.passengers.remove(p)
                count = count + 1     
        print(f"{count} passengers left the elevator in floor {self.floor}")
        print(self.passengers)
 
    # move(): This function is the most critical since it contains the logic of this project
    # If the elevator has a direction to "up" the idea is to calculate the maximum floor that someone wants to go
    # So every time the elevator moves, and possibly gets passengers, the max floor is calculated 
    # While the elevator hasn't reached the max floor it goes on in this direction
    # The idea is to change the direction, to "down" when the max floor has been reached 
    # since there is no one that wants to go "up" anymore
    # The same goes on for the minimum floor when the direction of the elevator is "down"
    # In both cases there are checks about not getting to minus floors or bigger than the top floor
    # and these checks are needed because when the elevator is empty there is not min and max to calculate

    def move(self):
        if self.direction == "up":
            if len(self.passengers) > 0:
                maximum = max(self.passengers)
                if self.floor == maximum or self.floor == self.total_floors:
                    self.direction = "down"
                    self.floor -= 1
                else:
                    self.floor += 1
            else:
                if self.floor < self.total_floors:
                    self.floor += 1
                else:
                    self.change_dir()
        else:
            if len(self.passengers) > 0:
                minimum = min(self.passengers)
                if self.floor == minimum or self.floor==0:
                    self.direction = "up"
                    self.floor += 1
                else:
                    self.floor -= 1
            else:
                if self.floor > 0:
                    self.floor -= 1
                else:
                    self.change_dir()
        return self.floor
          
    # print_report: Prints the situation of the elevator - current floor and number of passengers
    def print_report(self):
        print(f"We are at floor {self.floor} with {len(self.passengers)} passengers")
        print(self.passengers)
        # You can uncomment the command below to see in a more humanlike way how the program is executed in real time
        # time.sleep(0.5)
    
    # change_dir: This function assists in changing the direction of the elevator
    def change_dir(self):
        if self.direction == "up":
            self.direction = "down"
        else:
            self.direction = "up"