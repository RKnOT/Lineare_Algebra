# https://www.youtube.com/watch?v=CKNjZ1mM7gc&t=1815s


import numpy
import numpy as np
from numpy.random import randint
from matplotlib import pyplot
pyplot.rc('font', family='serif', size=5)

import sys
sys.path.append('../scripts/')

# Our helper
from plot_helper import *
import Utils as ut
    


v = (((2),(6),(1)),
      ((2),(10),(1)),
      ((6),(8),(1)))


T1 = ut.getT33Matrix(4, -3)

tails =[]
vectors =[] 
for i in range(90, 180, 90):
    C1 = ut.getR33Matrix(i)@T1

    vT1 = ut.get_vector_transformed(C1,v)
    #print(v)
    T_tails = ut.get_tail_of_vectors(vT1)

    
    tails.extend(ut.get_tail_of_vectors(v))
    vectors.extend(ut.get_2d_vectors(v))

    tails.extend(T_tails)
    vectors.extend(ut.get_2d_vectors(vT1))
    

plot_vector(tails, vectors)
pyplot.title("transform and rotated")

pyplot.show()
    

