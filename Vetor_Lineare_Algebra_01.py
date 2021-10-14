# https://www.youtube.com/watch?v=4-P0gptDT40&t=131s



import numpy
from numpy.random import randint
from matplotlib import pyplot
pyplot.rc('font', family='serif', size=5)

import sys
sys.path.append('../scripts/')

# Our helper
from plot_helper import *


#-----------------

beispiel_flag = 13

#----------------

def b1():
    vectors = [(2,2)]
    tails = [(-3,-2), (-3,1), (0,0), (1,-3)]
    plot_vector(vectors, tails)
    pyplot.title("The same vector, with its tail at four locations.")
    
a = numpy.array((-2,1))
b = numpy.array((1,-3))
c = numpy.array((2,1))

i = numpy.array((1,0))
j = numpy.array((0,1))


M = [[1,2], [2,1]]
M = numpy.array(M)

def b2():
    # vector addition
    
    origin = numpy.array((0,0))

    vectors = [a, b, a+b]
    tails   = [origin, a, origin]
    plot_vector(vectors, tails)
    pyplot.title("Adding vectors with coordinates $(-2, 1)$ and $(1,-3)$.\n");
    

def b3():
    # vector scaling
    
    vectors = [c, 2*c]
    plot_vector(vectors)
    pyplot.title("Scaling of the vector $(2,1)$ by the scalar $2$.");
    

def b4():
    # basis vector
    
    vec = 3*i + 2*j
    vectors = [i, j, 3*i, 2*j, vec]
    plot_vector(vectors)
    pyplot.title("The vector $(3,2)$ as a linear combination of the basis vectors.");
    
def b5():
    # span
    vectors = []
    i = numpy.array((1,0))
    j = numpy.array((0,1))

    for _ in range(30):
        m = randint(-10,10)
        n = randint(-10,10)
        vectors.append(m*i + n*j)
    
    plot_vector(vectors)
    pyplot.title("Thirty random vectors, created from the basis vectors");

def b6():
    vectors = []
    for _ in range(30):
        m = randint(-10,10)
        n = randint(-10,10)
        vectors.append(m*a + n*b)
    
    plot_vector(vectors)
    pyplot.title("Thirty random vectors, created as linear combinations of a and b")
    
    
    
    
def b7():
    d = numpy.array((-1,0.5))
    vectors = []
    for _ in range(30):
        m = randint(-10,10)
        n = randint(-10,10)
        vectors.append(m*a + n*d)
    
    plot_vector(vectors)
    pyplot.title("Thirty linear combinations of the vectors a and d");

def b8():
    A = [[-2,1], [1,-3]]
    A = numpy.array(A)
    print(A)
    print(A.dot(c))
    print(A.dot(i))
    print(A.dot(j))
    plot_linear_transformation(A)

def b9():
    
    print(M)
    print(M.dot(i))
    print(M.dot(j))
    plot_linear_transformation(M)

def b10():    
    print('M =', M)
    x = numpy.array((0.5,1))
    vectors = [x, M.dot(x)]
    plot_vector(vectors)
    pass
    
def b11():    
    N = numpy.array([[1,2],[-3,2]])
    print(N)
    plot_linear_transformation(N)
    pass

def b12():    
    rotation = numpy.array([[0,-1], [1,0]])
    print(rotation)
    shear = numpy.array([[1,1], [0,1]])
    print(shear)
    print('rotations')
    plot_linear_transformation(rotation)
    pyplot.show()
    print('shear')
    plot_linear_transformation(shear)
    pyplot.show()
    print('scaling')
    scale = numpy.array([[2,0], [0,0.5]])
    print(scale)
    plot_linear_transformation(scale)
    shear_rotation = shear@rotation
    return shear_rotation
    
    
def b13():    
    shear_rotation= b12()
    plot_linear_transformation(shear_rotation) 
    pass

def b14():   
    pass

def b15():    
    pass



    
#--------------------------
if __name__ == "__main__":
    

    if beispiel_flag ==1: b1()
    elif beispiel_flag ==2: b2()
    elif beispiel_flag ==3: b3()
    elif beispiel_flag ==4: b4()
    elif beispiel_flag ==5: b5()
    elif beispiel_flag ==6: b6()
    elif beispiel_flag ==7: b7()
    elif beispiel_flag ==8: b8()
    elif beispiel_flag ==9: b9()
    elif beispiel_flag ==10: b10()
    elif beispiel_flag ==11: b11()
    elif beispiel_flag ==12: b12()
    elif beispiel_flag ==13: b13()
    elif beispiel_flag ==14: b14()
    elif beispiel_flag ==15: b15()
    
    
    pyplot.show()
