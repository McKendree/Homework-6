import numpy as np

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    r = ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)**(1/2)
    rhat = np.array([(p2[0]-p1[0])/r,(p2[1]-p1[1])/r,(p2[2]-p1[2])/r])
    return -1*G*m/r**2*rhat

def point_in_sphere(x,y,z, radius=None):
    ''' x y z are coordinates of a point that is
        tested as to whether it is inside a sphere
        with radius = radius'''
    if (x**2+y**2+z**2)**(1/2) <= radius:
        return True
    else:
        return False

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 6378*km #radius of globe Earth
    h = 200.0*km #step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h
    #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-7000*km, 7000*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    #define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 6378*km])
    point_equator   = np.array([0, 6378*km, 0])
    point_southpole = np.array([0, 0, -6378*km])
    
    #North Pole calc
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps for north pole.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    
    #Equator calc
    grav_vec_equator = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps for equator.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_equator += grav_accel(point, point_equator, m)

    #South Pole calc
    grav_vec_southpole = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps for south pole.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_southpole += grav_accel(point, point_southpole, m)

    #print gravity vectors at each point
    print("\nThe gravity vector at the north pole is...", grav_vec_northpole)
    print("Should be something like [0,0,-9.8] m/s^2")
    print("\nThe gravity vector at the equator is...", grav_vec_equator)
    print("Should be something like [0,-9.8,0] m/s^2")
    print("\nThe gravity vector at the south pole is...", grav_vec_southpole)
    print("Should be something like [0,0,9.8] m/s^2")
