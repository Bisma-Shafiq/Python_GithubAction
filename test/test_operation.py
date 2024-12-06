from src.maths_operation import add, sub

def addition_test():
    assert add(2,3)==5
    assert add(3,9)==12
    assert add(0,1)==1
    assert add(2,9)==11


def subtraction_test():
    assert sub(2,3)==-1
    assert sub(3,9)==-6
    assert sub(0,1)==-1
    assert sub(2,9)==-7
    