'''
Created on Dec. 17, 2020

@author: Alex
'''
import time

class PocketDimension:
    def __init__(self, level0):
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.min_z = 0
        self.max_z = 0
        self.min_w = 0
        self.max_w = 0
        
        self._grid = {}
        
        z = 0
        w = 0
        for y, row in enumerate(level0):
            for x, cell in enumerate(row):
                self.update((x,y,z, w), cell)
                
    def update(self, (x,y,z,w), cell):
        if (x,y,z,w) not in self._grid:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)
            self.min_z = min(self.min_z, z)
            self.max_z = max(self.max_z, z)
            self.min_w = min(self.min_w, w)
            self.max_w = max(self.max_w, w)
        self._grid[(x,y,z,w)] = cell
        
    def get(self, (x,y,z,w)):
        if (x,y,z,w) not in self._grid:
            return '.'
        return self._grid[(x,y,z,w)]
    
    def copy(self):
        result = PocketDimension([])
        
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                for z in range(self.min_z, self.max_z+1):
                    for w in range(self.min_w, self.max_w+1):
                        result.update((x,y,z,w), self.get((x,y,z,w)))
        
        return result
    
    def count_neighbours(self, (x,y,z,w)):
        count = 0
        
        for i in (-1,0,1):
            for j in (-1,0,1):
                for k in (-1,0,1):
                    for l in (-1,0,1):
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        neighbour = self.get((x+i, y+j, z+k, w+l))
                        if neighbour == '#':
                            count += 1
        
        return count
    
    def perform_iteration(self):
        next_gen = self.copy()
        
        for x in range(self.min_x-1, self.max_x+2):
            for y in range(self.min_y-1, self.max_y+2):
                for z in range(self.min_z-1, self.max_z+2):
                    for w in range(self.min_w-1, self.max_w+2):
                        cell = self.get((x,y,z,w))
                        neighbours = self.count_neighbours((x,y,z,w))
                        
                        if cell == '#' and neighbours not in (2,3):
                            next_gen.update((x,y,z,w), '.')
                        elif cell == '.' and neighbours == 3:
                            next_gen.update((x,y,z,w), '#')
                    
        return next_gen
    
    def print_pd(self):
        for w in range(self.min_w, self.max_w+1):
            for z in range(self.min_z, self.max_z+1):
                print 'z=%d, w=%d' % (z,w)
                for y in range(self.min_y, self.max_y+1):
                    print ''.join([self.get((x,y,z,w)) for x in range(self.min_x, self.max_x+1)])
                print ''
    
    def count_active_cells(self):
        return self._grid.values().count('#')

start = time.time()

with open('day17.in', 'r') as input_file:
    level0 = [list(line.strip()) for line in input_file]
    
    pd = PocketDimension(level0)

    for iteration in range(6):
        print 'starting iteration', iteration+1
        pd = pd.perform_iteration()
        
    print pd.count_active_cells(), 'active cells'
    
print time.time() - start, 'seconds'