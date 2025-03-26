import random
def nor(PT_ID):
    event=random.choice(["ad","dai","treat","dis","emergency",])
    print(f"{PT_ID}  {event}")
def emt(PT_ID):
    con=random.choice(["ser","critical","not well"])
    print(f"{PT_ID}  {con}")
def sim(PT_NUM,step):
    for step in range(step):
     print(f"run no {step+1}")
     for PT_ID in range(1,PT_NUM+1):
        event=random.choice(["nora","EMT"])
        if event=='nora':
           nor(PT_ID)
        else:
           emt(PT_ID)
           nor(PT_ID)
sim(5,10)