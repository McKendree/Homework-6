import numpy as np
import math

#exact area of ellipse function
def exact_area_of_ellipse(a,b):
    return math.pi*a*b

#trapezoidal rule area of ellipse with 1/2 step size
def trapezoidal_area_of_ellipse(a,b):
    yValues = []
    for i in range(a*2+1):
        yValues.append(math.sqrt(b**2*(1-(((i/2)**2)/a**2))))
    yValues = np.array(yValues)
    return np.trapz(yValues)*2

#masked area of ellipse with 0.1x0.1 resolution
def masked_area_of_ellipse(a,b):
    xArr = np.arange(-a,a+0.1,0.1)
    yArr = np.arange(-b,b+0.1,0.1) 
    mValues = []
    for y in yArr:
        for x in xArr:
            if (x**2/a**2)+(y**2/b**2) <= 1:
                m = 1
            else:
                m = 0
            mValues.append(m)
    mValues = np.array(mValues)
    area = mValues.sum()*0.01
    return area
    

#printed outputs
print('exact area:', exact_area_of_ellipse(2,4))
print('trapezoidal area:', trapezoidal_area_of_ellipse(2,4))
print('masked area:', masked_area_of_ellipse(2,4))
