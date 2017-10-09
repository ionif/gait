
import math

# The gravitational constant
G = 1
#astronomical unit
AU = 149597871 #km

class Body():
    
    mass = 0.0
    vx = vy = vz = 0.0
    x = y = z = 0.0
    
    def attraction(self, other):
        if self is other:
            raise ValueError("Finding attraction to itself")
    
        sx, sy, sz = self.x, self.y, self.z
        ox, oy, oz = other.x, other.y, other.z
        
        dx = ox - sx
        dy = oy - sy
        dz = oz - sz
        #Find distance
        d = math.sqrt(dx**2 + dy**2 + dz**2)
        
        if d == 0:
            raise ValueError("Distance is zero")
        
        #Find acceleration of force 
        ax = -G * other.mass * -dx / (d**3)
        ay = -G * other.mass * -dy / (d**3)
        az = -G * other.mass * -dz / (d**3)
        
        #Find force
        fx = self.mass * ax
        fy = self.mass * ay    
        fz = self.mass * az
        
        return fx, fy, fz
    
def update(step, bodies):
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f} {:>10.3f}'.format(body.name, body.x, body.y, body.z, body.vx, body.vy, body.vz)
        print(s)
    print()
            
def loop(bodies):
    """
    timestep is 1 day or 86400 seconds
    """
    timestep = 1
    step = 1
    while True:
        update(step, bodies)
        step += 1
        
        force = {}
        for body in bodies:
            total_fx = total_fy = total_fz = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy, fz = body.attraction(other)
                
                total_fx += fx
                total_fy += fy
                total_fz += fz
            #total force    
            force[body] = (total_fx, total_fy, total_fz)
            
        for body in bodies:
            fx, fy, fz = force[body]
            #update velocities
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
            body.vz += fz / body.mass * timestep
            #update positions
            body.x += body.vx * timestep
            body.y += body.vy * timestep
            body.z += body.vz * timestep
            
def main():
    """
    mass = kg
    positions = AU
    velocities = AU/day
    """
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.988544 * 10**30
    sun.x = -7.139143380212697E-03
    sun.y = -2.792019770161695E-03
    sun.z = 2.061838852554664E-04
    sun.vx = 5.374260940168566E-06
    sun.vy = -7.410965396701423E-06
    sun.vz = -9.422862838391440E-08
    
    mercury = Body()
    mercury.name = 'Mercury'
    mercury.mass = 3.302 * 10**23
    mercury.x = -1.478672233442572E-01 
    mercury.y = -4.466929775364947E-01
    mercury.z = -2.313937582786785E-02
    mercury.vx = 2.117424563261189E-02
    mercury.vy = -7.105386404267509E-03
    mercury.vz = -2.522925180072137E-03
    
    venus = Body()
    venus.name = 'Venus'
    venus.mass = 48.685 * 10**23
    venus.x = -7.257693602841776E-01 
    venus.y = -2.529582082587794E-02 
    venus.z = 4.137802526208009E-02 
    venus.vx = 5.189070188671265E-04
    venus.vy = -2.031355258779472E-02
    venus.vz = -3.072687386494688E-04
    
    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.97219 * 10**24
    earth.x = -1.756637922977122E-01
    earth.y = 9.659912850526895E-01
    earth.z = 2.020629118443605E-04 
    earth.vx = -1.722857156974862E-02
    earth.vy = -3.015071224668472E-03
    earth.vz = -5.859931223618532E-08
    
    mars = Body()
    mars.name = 'Mars'
    mars.mass = 6.4185 * 10**23
    mars.x = 1.383221922520998E+00
    mars.y = -2.380174081741852E-02
    mars.z = -3.441183028447500E-02
    mars.vx = 7.533013850513376E-04
    mars.vy = 1.517888771209419E-02
    mars.vz = 2.996589710207392E-04
    
    jupiter = Body()
    jupiter.name = 'Jupiter'
    jupiter.mass = 1898.13 * 10**24
    jupiter.x = 3.996321310086093E+00
    jupiter.y = 2.932561197358908E+00
    jupiter.z = -1.016170544300634E-01
    jupiter.vx = -4.558376590671486E-03
    jupiter.vy = 6.439863246141724E-03
    jupiter.vz = 7.537593486203765E-05
    
    saturn = Body()
    saturn.name = 'Saturn'
    saturn.mass = 5.68319 * 10**26
    saturn.x = 6.401416890663500E+00
    saturn.y = 6.565250734685104E+00
    saturn.z = -3.689211141720000E-01
    saturn.vx = -4.285166238539475E-03
    saturn.vy = 3.884579926659154E-03
    saturn.vz = 1.025155282571916E-04
    
    
    loop([sun, mercury, venus, earth, mars, jupiter, saturn])

if __name__ == '__main__':
    main()
