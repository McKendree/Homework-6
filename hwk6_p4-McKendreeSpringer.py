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

def point_in_sphere(x,y,z, radius=None):
    ''' x y z are coordinates of a point that is
        tested as to whether it is inside a sphere
        with radius = radius'''
    if (x**2+y**2+z**2)**(1/2) <= radius:
        return True
    else:
        return False

if __name__ == "__main__":
    #for flat earth
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
    flat_northpole_grav_mag = []

    #flat earth north pole gravity magnitude at height 1
    point_northpole = np.array([0, 0, 4751*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 1.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 10
    point_northpole = np.array([0, 0, 4760*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 10.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 100
    point_northpole = np.array([0, 0, 4850*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 100.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 10e3
    point_northpole = np.array([0, 0, 5750*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 10e3.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 10e4
    point_northpole = np.array([0, 0, 14750*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 10e4.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 10e5
    point_northpole = np.array([0, 0, 104750*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 10e5.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #flat earth north pole gravity magnitude at height 10e6
    point_northpole = np.array([0, 0, 1004750*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for flat earth north pole at height 10e6.")
        for yy in y:
            for zz in z:
                if point_in_cylinder(xx,yy,zz,radius=radius,length=width):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    flat_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #for spherical earth
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 6378*km #radius of globe Earth
    h = 200.0*km #step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h;print(dx)
    #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-7000*km, 7000*km, dx);print(x)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    sphere_northpole_grav_mag = []

    #spherical earth north pole gravity magnitude at height 1
    point_northpole = np.array([0, 0, 6379*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 10
    point_northpole = np.array([0, 0, 6388*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 100
    point_northpole = np.array([0, 0, 6478*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 100.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 10e3
    point_northpole = np.array([0, 0, 7378*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10e3.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 10e4
    point_northpole = np.array([0, 0, 16378*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10e4.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 10e5
    point_northpole = np.array([0, 0, 106378*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10e5.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #spherical earth north pole gravity magnitude at height 10e6
    point_northpole = np.array([0, 0, 1006378*km])
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        print(idx, " of ", len_x, "x steps for spherical earth north pole at height 10e6.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=r_earth):
                    m = rho*h*h*h
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    sphere_northpole_grav_mag.append(abs(grav_vec_northpole[2]))

    #plots magnitude of gravity at north pole vs height
    height = [1, 10, 100, 10e3, 10e4, 10e5, 10e6]
    plt.plot(height, flat_northpole_grav_mag)
    plt.plot(height, sphere_northpole_grav_mag)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Flat Earth vs. Spherical Earth gravity above North pole')
    plt.xlabel('Height above North pole (km)')
    plt.ylabel('Acceleration of gravity (m/s^2)')
    plt.legend(['Flat Earth','Spherical Earth'])
    plt.savefig('Different_Earth_Gravities.png')
    plt.show()
