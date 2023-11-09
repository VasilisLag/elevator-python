import random

# Generator's role is to create sample text files that represent the queues of people waiting 
# Even if a txt file has been created, you can run the main with the same num of floors and it will be overwritten
class Generator:
    
    def create_sample(self, floors):
        # Create from scratch the text file if already created, because later I use append
        with open(f"./queues{floors}.txt", "w") as file:
            file.close()

        # The text file is writen character by character so I use "a" - append
        with open(f"./queues{floors}.txt", "a") as file:
            for i in range(floors + 1):
                # I set here a limit of 30 person waiting per queue, it can be modified though
                num_of_people = random.randint(1,30)
                for p in range(num_of_people):
                    number = random.randint(0, floors)
                    while number == i:
                        number = random.randint(0, floors)
                    file.write(str(number))
                    if p != (num_of_people-1):
                        file.write(",")
                if i != floors:
                    file.write('\n')
                    
                