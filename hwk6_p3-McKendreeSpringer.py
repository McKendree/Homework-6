import numpy as np
import math
import matplotlib.pyplot as plt

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point at which gravity is measured
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    r = ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)**(1/2)
    rhat = np.array([(p2[0]-p1[0])/r,(p2[1]-p1[1])/r,(p2[2]-p1[2])/r])
    return -1*G*m/r**2*rhat

def point_in_cylinder(x,y,z, radius, length):
    ''' x y z are coordinates of a point that is
        tested as to whether it is inside a cylinder
        with radius = radius and length = length'''
    if (x**2+y**2)**(1/2) <= radius and z >= 0 and z <= length:
        return True
    else:
        return False

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    radius = 20037*km #radius of flat Earth
    width = 4750*km #width of flat Earth
    h = 200.0*km #step size
    #sets grid size same in x,y,z
    dx, dy, dz = h, h, h
    #x, y, z defines boundaries of grid, here 7000 km
    x = np.arange(-20600*km, 20600*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = np.arange(0, 5000*km, dz)
    #defines points on the north pole, equator, and edge
    point_northpole = np.array([0, 0, 4750*km])
    point_equator   = np.array([0, 10018.5*km, 4750*km])
    point_edge = np.array([0, 20037*km, 4750*km])
    
    #north pole calc
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for north pole.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    
    #equator calc
    grav_vec_equator = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for equator.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_equator += grav_accel(point, point_equator, m)

    #edge point calc
    grav_vec_edge = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for edge point.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_edge += grav_accel(point, point_edge, m)

    #print gravity vectors at each point
    print("\nThe gravity vector at the north pole is...", grav_vec_northpole)
    print("\nThe gravity vector at the equator is...", grav_vec_equator)
    print("\nThe gravity vector at the edge is...", grav_vec_edge)
