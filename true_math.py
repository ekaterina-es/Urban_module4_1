from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        result = first / second
        if result == 0:
            return inf
    return result
