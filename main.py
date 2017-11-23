
import math
import argparse
import json

G = 4*math.pi**2/(365.25*265.25)       # m^3*kg^(-1)*s^(-2)

days = 10000

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
        ax = G * other.mass * dx / (d**3)
        ay = G * other.mass * dy / (d**3)
        az = G * other.mass * dz / (d**3)
                
        #Find force
        fx = self.mass * ax
        fy = self.mass * ay    
        fz = self.mass * az
        
        return fx, fy, fz
    
def update(step, bodies):
    for body in bodies:
           s = '{} {:<8} {:>6.2f} {:>6.2f} {:>6.2f}'.format(step, body.name, body.x, body.y, body.z)
           print(s)
            
def loop(bodies):
    """
    timestep is 1 day
    """

    timestep = 1
    step = 1
    while step <= days:
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
            body.vx += (fx / body.mass) * timestep
            body.vy += (fy / body.mass) * timestep
            body.vz += (fz / body.mass) * timestep
            #update positions
            body.x += body.vx * timestep
            body.y += body.vy * timestep
            body.z += body.vz * timestep
            
def main():
    
    bods = []
    
    data = json.load(open('planets.json'))
    
    for i in data:
        bod = Body()
        bod.name = i['name']
        bod.mass = i['mass']
        bod.x = i['pos'][0]
        bod.y = i['pos'][1]
        bod.z = i['pos'][2]
        bod.vx = i['vel'][0]
        bod.vy = i['vel'][1]
        bod.vz = i['vel'][2]
        bods.append(bod)
    
    loop(bods)

if __name__ == '__main__':
    main()
