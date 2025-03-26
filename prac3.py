import random
def sim_event(machine_ID):
    state=random.choice(["broken","starting","maitainence"])
    print(f"{machine_ID}  {state}")
def sim(step,num):
    for step in range(step):
        print(f"\nTime Step {step + 1}")
        for num in range(1, num + 1):
            sim_event(num)
sim(5,5)