from collections import defaultdict
from Graph_creation import Graph
from Fastest_route_calculation import Routing
import logging
from pathlib import Path

def helper_function():
    print(''' For adding a node to a graph
      Specify the distance to all the existing nodes with space in between
      For Example If we have existing nodes in a graph as {1,2,3,4}
      In order to add a node Specify the user input distance to all the nodes as shown below
      5 2 3 10
      Here consider the new node as 5
      distance(1,5)=5
      distance(2,5)=2
      distance(3,5)=3
      distance(4,5)=10
      If there are no connection between any existing nodes to the node to be added then specify the distance as 0.0
    ''')
    print(''' Deleting a node to a graph
        Specify the node name from the existing nodes
        For example If we have existing nodes in a graph as {1,2,3,4}
        In order to delete a node say 4 just specify the node-number 4 when asked for the user input
        ''')
if __name__=='__main__':
    # Steps for logging to a particular file
    formatLOG=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    Path("Logs").mkdir(parents=True, exist_ok=True)
    file_name="Logs/log.log"
    infoLog = logging.FileHandler(file_name)
    infoLog.setFormatter(formatLOG)
    level=logging.INFO
    logger = logging.getLogger(__name__)
    logger.addHandler(infoLog)
    logger.setLevel(level)

    '''Initial_cost =[[  0.,  15.,   0.,   7.,  10.,   0.],
    [ 15.,   0.,   9.,  11.,   0.,   9.],
    [  0.,   9.,   0.,   0.,  12.,   7.],
    [  7.,  11.,   0.,   0.,   8.,  14.],
    [ 10.,   0.,  12.,   8.,   0.,   8.],
    [  0.,   9.,   7.,  14.,   8.,   0.]] '''
    Initial_cost = [[0, 10, 15, 20], [10, 0, 35, 25],  
             [15, 35, 0, 30], [20, 25, 30, 0]]   

    graph = defaultdict(list) # Create a empty graph
    edges = set() # Create a empty set for storing edges
    G=Graph(graph,edges) # Create a graph object
    G.create_graph(Initial_cost) # Create a initial graph
    routing_obj=Routing(G.graph,G.edges) # Create a object for find the best route
    best_cost,best_route=routing_obj.simulated_annealing() # Find best route and cost using simulated annealing
    print('The best-route of initial graph is {}'.format(best_route))            
    print('The best-cost  of initial graph is {}\n'.format(best_cost))
    logger.info('The best-route of initial graph is {}'.format(best_route))
    logger.info('The best-cost  of initial graph is {}\n'.format(best_cost))
    helper_function()
    while True:
        print ('''Enter
a or A or add or ADD: To add a node to existing graph
d or D or delete or DELETE: To remove a node from existing graph
q or Q or quit or QUIT : To quit 
        ''')
        user_input=input("Enter your input: ")
        user_input=user_input.lower()
        if user_input=='a' or user_input=='add':
              print('Please input the distances to the existing node {}'.format(G.edges))
              while True:
                user_input_1 = list(map(int, input("Enter the list numbers for {} nodes separated by space ".format(len(G.edges))).strip().split()))[:len(G.edges)]
                if len(user_input_1)<len(G.edges):
                    print('Please enter values for all the edges again')
                else:
                    break
              G.add_node(user_input_1)
              best_cost,best_route=routing_obj.simulated_annealing()
              print('The best-route after adding node {} is {}'.format(len(G.edges),best_route))            
              print('The best-cost  after adding node {} is {} \n'.format(len(G.edges),best_cost))
              logger.info('The best-route after adding node {} is {}'.format(len(G.edges),best_route))
              logger.info('The best-cost  after adding node {} is {} \n'.format(len(G.edges),best_cost))
        elif user_input=='d' or user_input=='delete':
            while True:
              print('Existing nodes are {}'.format(G.edges))
              if not G.edges:
                  print('No node in the graph')
                  break
              try:
                user_input_2=int(input('Enter the node to be deleted: '))
              
                if int(user_input_2) not in G.edges:
                        print('Enter the valid node to be deleted from the graph')
                else:
                        G.remove_node(int(user_input_2))
                        print('The node {} is succesfully removed'.format(user_input_2))
                        best_cost,best_route=routing_obj.simulated_annealing()
                        print('The best-route after deleting node {} is {}'.format(user_input_2,best_route))            
                        print('The best cost  after deleting node {} is {}\n'.format(user_input_2,best_cost))
                        logger.info('The best-route after deleting node {} is {}'.format(user_input_2,best_route))
                        logger.info('The best cost  after deleting node {} is {}\n'.format(user_input_2,best_cost))
                        print ('''Enter
c or C or continue or CONTdINUE: To continue delete another node
q or Q or quit or QUIT: To quit deleting this process
''')
                        user_input_3=input("Enter your input: ")
                        user_input_3=user_input_3.lower()
                        if user_input_3=='q' or user_input_3=='quit':
                            break
                        elif user_input_3 =='c' or user_input_3=='continue':
                            continue
              except:
                 print('Enter the valid node to be deleted from the graph') 
                


        elif user_input=='q' or user_input =='quit':
            break
        else:
            print('Please enter a valid input: ')
            print (''' Enter
a or A or add or ADD: To add a node to existing graph
d or D or delete or DELETE: To remove a node from existing graph
q or Q or quit or QUIT: To quit 
        ''')
    
    logger.info('The best-route of final graph is {}'.format(best_route))
    logger.info('The best-cost  of final graph is {}\n'.format(best_cost))

    # Close logger and remove handler
    infoLog.close()
    logger.removeHandler(infoLog)

