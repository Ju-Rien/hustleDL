def elementwise_multiplication(a, b):
    assert(len(a) == len(b))
    
    output = [None]*len(a)
    
    for i in range(len(a)):
        output[i] = a[i]*b[i]
        
    return output


def elementwise_addition(a, b):
    assert(len(a) == len(b))
    
    output = [None]*len(a)
    
    for i in range(len(a)):
        output[i] = a[i]+b[i]
        
    return output


def vector_sum(a):
    output = 0
    
    for i in range(len(a)):
        output += a[i]
    
    return output


def vector_average(a):
    output = 0
    
    for i in range(len(a)):
        output += a[i]
    
    output /= len(a)
    
    return output


def dot_product(a, b):
    return vector_sum( elementwise_multiplication( a, b))
