import numpy as np

#------ Utils ----------
def getT33Matrix(x,y):
    T = np.array(((1,0,x),(0,1,y),(0,0,1)))
    return T

def getS33Matrix(x,y):
    S = [[x,0,0],[0,y,0],[0,0,1]]
    S= np.array(S)
    return S


def getR33Matrix(theta, inGrad = True):
    if inGrad==True:
        theta = np.radians(theta)
    return np.array(( (np.cos(theta), -np.sin(theta),0),
               (np.sin(theta), np.cos(theta),0),
               (0,0,1)))




def vtrans(self, v):
        vt = np.transpose(v)
        self.vtt = vt[:,0:2]
        return self.vtt[0]
   





def get_2d_vectors(v):
    d2v =[]
    for i in range(0, len(v)):
        d2v.append([v[i][0], v[i][1]])
    return d2v
    
def vektor_delta(v1, v2):
    return [v1[0]- v2[0], v1[1]- v2[1]]

def get_tail_of_vectors(v):
    tail = []
    for i in range(0, len(v)):
        if i == len(v)-1:
            d = vektor_delta(v[0], v[i])         
        else:
            d = vektor_delta(v[i+1], v[i])
        tail.append(d)
    return (tail)

def get_vector_transformed(T, v):
    xT= []
    for item in v:
        xT.append(T.dot(item))
    return xT
        
        
#---------------------------    
    
