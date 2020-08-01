class Graph:
    '''
    Class to create graph, add or remove node from the existing graph
    '''
    def __init__(self,graph,edges):
        self.graph=graph
        self.edges=edges
    def create_graph(self,list_values):
        ''' Create a graph for the given input
        '''
        for i, v in enumerate(list_values, 1):
            self.edges.add(i) 
            self.graph[i]={}
            for j, u in enumerate(v, 1):
               self.graph[i][j]=u
    def add_node(self,list_values):
        ''' Add a node to existing graph
        '''
        max_edge_value=max(self.edges) # find max_edge_value of existing graph
        key_values=self.graph.keys() 
        self.edges.add(1+max_edge_value) # Add the new_edge created to existing edge_set
        self.graph[max_edge_value+1]={}  # Create a new graph 
        for i, v in zip(key_values,list_values):
            self.graph[max_edge_value+1][i]= v
            self.graph[i][max_edge_value+1]=v
        self.graph[max_edge_value+1][max_edge_value+1]= 0.0
        print('The node {} has been added successfully to the graph'.format(max_edge_value+1))
    def remove_node(self,node_value):
        ''' Remove a node from the existing graph'''
        self.edges.remove(node_value) # Remove node_value specified from set
        self.graph.pop(node_value)    # Remove the connections corresponding to the node value
        for key,_ in self.graph.items():
            self.graph[key].pop(node_value)








