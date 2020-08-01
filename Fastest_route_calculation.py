import numpy 
import random

class Routing:
    '''
    Class to compute total_distance of particular set of edges
    fastest route using simulated annealing
    '''
    def __init__(self,graph,edges):
        self.graph=graph
        self.edges=edges

    def get_total_distance(self,list_val):
        '''Calculate total distance for the given edges in the list
        '''
        dist=0
        for first,second in zip(list_val[:-1],list_val[1:]):
            if self.graph[first][second]==0: # Assigning large value if no connection exist between two nodes
                dist+=1000000
            else:
                dist+=self.graph[first][second]
        if self.graph[list_val[-1]][list_val[0]]==0: # Assigning large value if no connection exist between two nodes
            dist+=1000000
        else:
            dist+=self.graph[list_val[-1]][list_val[0]]
        return dist

    def simulated_annealing(self):
        ''' Find the fastest route using simulated annealing procedure
        '''
        list_val=self.edges.copy() # Copying the edges to a list
        list_val=list(list_val)
        cost0=self.get_total_distance(list_val) # Calculate initial cost
        best_cost=cost0  # Assign best cost as initial cost
        best_route=list_val.copy() # Assign best route as inital list
        early_stop_counter=0 
        # Simulated Annealing parameters
        T=30
        factor=0.99
        T_init=T
        for i in range(500): # 500 can be set to low or high value based on number of nodes

            T=T*factor
            
            # Procedure to come out of the loop if best_cost does-not change for 20 iterations
            if best_cost<cost0:
                early_stop_counter=0
            else:
                early_stop_counter+=1
            
            if early_stop_counter==20:
                break
                

            for j in range(250): # 500 can be set to low or high value based on number of nodes
                
                r1,r2=random.sample(range(1,len(list_val)),2) # Exchange two coordinates and get a new distance
                list_val[r1],list_val[r2]=list_val[r2],list_val[r1]
                cost1=self.get_total_distance(list_val=list_val) # Calculate the cost of swapped edges
                
                if cost1<cost0:
                    cost0=cost1
                    best_cost=cost1
                    best_route=list_val.copy()
                else:
                    x=numpy.random.uniform()
                    if x < numpy.exp((cost0-cost1)/T):
                        cost0=cost1
                    else:
                        list_val[r1],list_val[r2]=list_val[r2],list_val[r1]
        return best_cost,best_route    

    
    

if __name__=='__main__':
    # The values of the graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],  
             [15, 35, 0, 30], [20, 25, 30, 0]]
    
       
    list_val=numpy.arange(0,len(graph))
    list_val=set(list_val)
    #print(list_val)

    #check_graph =  [val.pop(2) for val in check_graph.copy()]

    #print(check_graph)

    #print(graph)
    # Simulated annealing algorithm
    
    '''cost0=Graph.get_total_distance(list_val=list_val)
    #print(cost0)
    best_cost=cost0
    best_route=list_val.copy()
    early_stop_counter=0
    T=30
    factor=0.99
    T_init=T
    for i in range(150):
        print(i,'cost=',cost0)

        T=T*factor

        if best_cost<cost0:
            early_stop_counter=0
        else:
            early_stop_counter+=1
        
        if early_stop_counter==10:
            break
            

        for j in range(25):
            # Exchange two coordinates and get a new distance
            r1,r2=random.sample(range(1,len(list_val)),2)
            list_val[r1],list_val[r2]=list_val[r2],list_val[r1]
            #print(list_val)
            cost1=Graph.get_total_distance(list_val=list_val)
            
            if cost1<cost0:
                cost0=cost1
                best_cost=cost1
                best_route=list_val.copy()
            else:
                x=numpy.random.uniform()
                if x < numpy.exp((cost0-cost1)/T):
                    cost0=cost1
                else:
                    list_val[r1],list_val[r2]=list_val[r2],list_val[r1]'''
    


