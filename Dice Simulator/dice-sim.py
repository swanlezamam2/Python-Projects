def dice_sim(value = None):
    import random

    again = 'y'
    while again:
        print(f"The dice rolled {random.randint(1,6)}")
        again = input("Want to continue? (y/n):\t")
        
        if again == 'y': continue 
        else: break

dice_sim()
