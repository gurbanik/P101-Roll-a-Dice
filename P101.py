import random
response = "y"
while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[ 0   ]")
        print("[ 0   ]")
        print("[    0]")
        print("[-----]")
    response = input("press y to roll dice and n exit")

    

