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
    


v = (((2),(3),(1)),
     ((4),(3),(1)),
     ((3),(6),(1)))


rp =[3],[4],[1]


tails =[]
vectors =[] 

tails.extend(ut.get_2d_vectors(ut.get_tail_of_vectors(v)))
vectors.extend(ut.get_2d_vectors(v))

T1= ut.getT33Matrix(-1*rp[0][0],-1*rp[1][0])
#print(T1)
R = ut.getR33Matrix(90)
S = ut.getS33Matrix(2, 0.5)
T2= ut.getT33Matrix(rp[0][0],rp[1][0])

C = S@T2@R@T1

vT1 = ut.get_vector_transformed(C,v)

tails.extend(ut.get_2d_vectors(ut.get_tail_of_vectors(vT1)))
vectors.extend(ut.get_2d_vectors(vT1))
plot_vector(tails, vectors)
pyplot.title("transform and rotated")

pyplot.show()

