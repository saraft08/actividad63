from random import randint
def faren_cel (f):
    return (f - 32)* 5.0/9.0
print(faren_cel(randint(1,100)))