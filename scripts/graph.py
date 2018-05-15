
class Vertex(object):
    #TODO: docstring class
    def __init__(self, key):
        self._name = key
        self._connections = {}
        self._color = 'white'
        self._distance = 0
        self._predecessors = None
        self._discovery_time = 0
        self._finish_time = 0
        
    def add_neighbour(self, vertex, weight=0):
        self._connections[vertex] = weight
    
    def __str__(self):
        return 'This vertex has the key name: {0} is connected to verticies: {1}'.format(self._name, self._connections.items())
    
    def get_connections(self):
        return self._connections.keys()
    
    @property
    def discovery_time(self):
        return self._discovery_time
    
    @discovery_time.setter
    def discovery_time(self, time):
        self._discovery_time = time
    
    @property
    def finish_time(self):
        return self._finish_time
    
    @finish_time.setter
    def finish_time(self, time):
        self._finish_time = time
    
    @property
    def predecessors(self):
        return self._predecessors
    
    @predecessors.setter
    def predecessors(self, pre):
        self._predecessors = pre
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if color not in ['white', 'black', 'gray']:
            raise ValueError("The vertix color can only be: ['white', 'black', 'gray'].")
        self._color = color
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, distance):
        self._distance = distance
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, key):
        self._name = key
            
    @property
    def connections(self):
        return self._connections.keys()
    
    def get_weight(self, nbr):
        if nbr in self._connections:
            return self._connections[nbr]
        else:
            raise KeyError('Key of neighbour does not exist.')

class Graph(object):
    #TODO: docstring class
    def __init__(self):
        self.verticies_list = {}
        self.verticies_num = 0
    
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.verticies_num += 1
        self.verticies_list[key] = new_vertex
        return new_vertex
    
    def get_vertex(self, key):
        if key in self.verticies_list:
            return self.verticies_list[key]
        else:
            return None
    
    def __contains__(self, key):
        return key in self.verticies_list
    
    def add_edge(self, source, destination, weight=0):
        if source not in self.verticies_list:
            tmp = self.add_vertex(source)
        if destination not in self.verticies_list:
            tmp = self.add_vertex(destination)
        self.verticies_list[source].add_neighbour(self.verticies_list[destination], weight)
    
    def get_verticies(self):
        return self.verticies_list.keys()
    
    def __iter__(self):
        return iter(self.verticies_list.values())
    
    def toplogical_sort(self, start_vertex):
        #init
        distances = [float('Inf')] * self.verticies_num
        distances[start_vertex] = 0
        stack = []
        #reset all verticies to color white
        for vertex in self.verticies_list:
            self.get_vertex(vertex).color = 'white'
        #store topoligical sort starting from source vertix
        for neighour in self.get_vertex(start_vertex).connections:
            if neighour is not None and neighour.color == 'white':
                self._toplogical_sort(start_vertex, stack)
        #process in toplogical order
        while stack:
            # the next toplogical vertex
            current_vertex = stack.pop()
            for neighour in self.get_vertex(current_vertex).connections:
                w = get_weight(neighour)
                if distances[neighour] > distances[current_vertex] + w:
                    distances[neighour] = distances[current_vertex] + w
            
    
    def _toplogical_sort(self, vertex, stack):
        print(self.get_vertex(vertex))
        self.get_vertex(vertex).color = 'black'
        if vertex in self.get_verticies():
            for neighbour in self.get_vertex(vertex).connections:
                if neighbour is not None and neighbour.color == 'white':
                    self._toplogical_sort(neighbour, stack)
        stack.append(vertex)
    
    def bfs(self, start_vertex, end_vertex):
        self.get_vertex(start_vertex).color = 'white'
        self.get_vertex(start_vertex).predecessors = [None]
        verticies_queue = []
        verticies_queue.insert(0, start_vertex)
        while verticies_queue:
            current_vertex = verticies_queue.pop()
            for neighour in self.get_vertex(current_vertex).connections:
                if neighour.color == 'white':
                    neighour.color = 'gray'
                    neighour.distance += 1
                    neighour.predecessors = current_vertex
                    verticies_queue.insert(0, neighour.name)
            self.get_vertex(current_vertex).color = 'black'
        return self._traverse(start_vertex, end_vertex)
    
    def dfs(self):
        time = 0
        for vertex in self.verticies_list:
            self.get_vertex(vertex).color = 'white'
            self.get_vertex(vertex).predecessors = None
        for vertex in self.verticies_list:
            if self.get_vertex(vertex).color == 'white':
                self._dfs(vertex, time)
                
    def _dfs(self, vertex, time):
        self.get_vertex(vertex).color = 'gray'
        time += 1
        self.get_vertex(vertex).discovery_time = time
        for neighbour_vertex in self.get_vertex(vertex).connections:
            if self.get_vertex(neighbour_vertex).color == 'white':
                self.get_vertex(neighbour_vertex).predecessors = vertex
                self._dfs(neighbour_vertex, time)
        self.get_vertex(vertex).color = 'black'
        time += 1
        self.get_vertex(vertex).finish_time = time
        
    def _traverse(self,start_vertex, end_vertex):
        _path = []
        while self.get_vertex(end_vertex).predecessors:
            _path.insert(0, self.get_vertex(end_vertex).name)
            end_vertex = self.get_vertex(end_vertex).predecessors
            if self.get_vertex(end_vertex).name == start_vertex:
                _path.insert(0, self.get_vertex(end_vertex).name)
                break
        return _path