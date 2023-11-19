import random
def block():
    global Flag
    block_percent = random.randint(1,100)
    print(block_percent)
    if block_percent > 70:
        Flag = True
        print(Flag)
    else:
        Flag = False
        print(Flag)

print(block)

print(block())