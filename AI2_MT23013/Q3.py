import pandas as pd
import networkx as nx
import random
import math
df = pd.read_csv('road_csv.csv')

#These coordinates have been created using the OpenCageGeocode library
#These are the actual latitude and longitude of these locations, generated using OpenCageGeocode
coordinates = {
    "Ranchi": {"Latitude": 23.3700501, "Longitude": 85.3250387},
    "Jaipur": {"Latitude": 26.9154576, "Longitude": 75.8189817},
    "Trivandrum": {"Latitude": 8.4882267, "Longitude": 76.947551},
    "Bombay": {"Latitude": 19.0815772, "Longitude": 72.8866275},
    "Kanpur": {"Latitude": 26.4609135, "Longitude": 80.3217588},
    "Calicut": {"Latitude": 11.2450558, "Longitude": 75.7754716},
    "Coimbatore": {"Latitude": 11.0018115, "Longitude": 76.9628425},
    "Vishakapatnam": {"Latitude": 17.7214822, "Longitude": 83.2900989},
    "Indore": {"Latitude": 22.7203616, "Longitude": 75.8681996},
    "Lucknow": {"Latitude": 26.8381, "Longitude": 80.9346001},
    "Madras": {"Latitude": 13.0836939, "Longitude": 80.270186},
    "Vijayawada": {"Latitude": 16.5087573, "Longitude": 80.6185089},
    "Allahabad": {"Latitude": 25.4381302, "Longitude": 81.8338005},
    "Delhi": {"Latitude": 28.6273928, "Longitude": 77.1716954},
    "Shillong": {"Latitude": 25.5760446, "Longitude": 91.8825282},
    "Hubli": {"Latitude": 15.3518378, "Longitude": 75.1379848},
    "Ludhiana": {"Latitude": 30.9090157, "Longitude": 75.851601},
    "Bhopal": {"Latitude": 23.2584857, "Longitude": 77.401989},
    "Agartala": {"Latitude": 23.8312377, "Longitude": 91.2823821},
    "Panjim": {"Latitude": 15.4989946, "Longitude": 73.8282141},
    "Varanasi": {"Latitude": 25.3356491, "Longitude": 83.0076292},
    "Hyderabad": {"Latitude": 17.360589, "Longitude": 78.4740613},
    "Baroda": {"Latitude": 22.2973142, "Longitude": 73.1942567},
    "Pune": {"Latitude": 18.521428, "Longitude": 73.8544541},
    "Jabalpur": {"Latitude": 23.1608938, "Longitude": 79.9497702},
    "Kolhapur": {"Latitude": 16.7028412, "Longitude": 74.2405329},
    "Calcutta": {"Latitude": 22.5726459, "Longitude": 88.3638953},
    "Jamshedpur": {"Latitude": 22.8015194, "Longitude": 86.2029579},
    "Jullundur": {"Latitude": 31.416667, "Longitude": 75.616667},
    "Patna": {"Latitude": 25.6093239, "Longitude": 85.1235252},
    "Meerut": {"Latitude": 28.9826533, "Longitude": 77.7081013},
    "Surat": {"Latitude": 45.9383, "Longitude": 3.2553},
    "Madurai": {"Latitude": 9.9261153, "Longitude": 78.1140983},
    "Shimla": {"Latitude": 31.1041526, "Longitude": 77.1709729},
    "Ahmedabad": {"Latitude": 23.0216238, "Longitude": 72.5797068},
    "Imphal": {"Latitude": 24.7991162, "Longitude": 93.9364419},
    "Pondicherry": {"Latitude": 10.9156489, "Longitude": 79.8069488},
    "Nagpur": {"Latitude": 21.1498134, "Longitude": 79.0820556},
    "Nasik": {"Latitude": 20.0112475, "Longitude": 73.7902364},
    "Amritsar": {"Latitude": 31.6343083, "Longitude": 74.8736788},
    "Chandigarh": {"Latitude": 30.7298439, "Longitude": 76.7841457},
    "Bangalore": {"Latitude": 12.9767936, "Longitude": 77.590082},
    "Asansol": {"Latitude": 23.6871297, "Longitude": 86.9746587},
    "Distance in Kilometres": {"Latitude": None, "Longitude": None},
    "Bhubaneshwar": {"Latitude": 20.2602964, "Longitude": 85.8394521},
    "Gwalior": {"Latitude": 26.2037247, "Longitude": 78.1573628},
    "Agra": {"Latitude": 27.1752554, "Longitude": 78.0098161},
    "Cochin": {"Latitude": 9.9674277, "Longitude": 76.2454436}
}

#Haversine distance is the angular distance between two points on the surface of a sphere.
#Used to calculate the distance between two points based on their latitude and longitude
#For the formula chatgpt and internet was used

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371

    #Converting the latitudes and longitudes into radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

#Uniform cost search
def uniform_cost_search(graph, start, end):
    visited = set()
    queue = [(0, [start])]  
    
    while queue:
        cost, path = queue.pop(0)
        node = path[-1]
        
        #If last node found
        if node == end:
            print("UCS Search:")
            print(path)
            print("\n")
            return cost

        #Incase current node is not visited
        if node not in visited:
            visited.add(node)
            #For all the neighbours in the neighbour(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    distance = graph[node][neighbor]['distance']
                    new_cost = cost + distance
                    new_path = path + [neighbor]
                    queue.append((new_cost, new_path))
                    #sorting the queue on the basis of the new_cost value
                    queue.sort()  
    return 0

def A_star_admissible(graph,start,end):
    
    visited=set()
    node_queue=[(0,0,[start])]

    while(node_queue):
        heursitic_cost,cost,path=node_queue.pop(0)
        last_node=path[-1]

        if(last_node==end):
            print("A* Admissible:")
            print(path)
            print("\n")
            return cost

        if last_node not in visited:
            visited.add(last_node)
            neighbours=graph.neighbors(last_node)
            for neighbour in neighbours:
                n_path=path+[neighbour]
                n_cost=cost+graph[last_node][neighbour]['distance']

                #Finding the coordinates latitude and longitude
                x1=coordinates[neighbour]['Latitude']
                y1=coordinates[neighbour]['Longitude']

                x2=coordinates[end]['Latitude']
                y2=coordinates[end]['Longitude']

                #Finding the distance - haversine
                heuristic=haversine_distance(x1,y1,x2,y2)
                #print(last_node+" -> "+neighbour+" : "+str(n_cost+heuristic))
                node_queue.append((n_cost+heuristic,n_cost,n_path))
                node_queue.sort()


    return 0
                
def A_star_inadmissible(graph, start, end):
   
    visited=set()
    node_queue=[(0,0,[start])]

    while(node_queue):
        heursitic_cost,cost,path=node_queue.pop(0)
        last_node=path[-1]

        if(last_node==end):
            print("A* Inadmissible :")
            print(path)
            print("\n")
            return cost

        if last_node not in visited:
            visited.add(last_node)
            neighbours=graph.neighbors(last_node)
            for neighbour in neighbours:
                n_path=path+[neighbour]
                n_cost=cost+graph[last_node][neighbour]['distance']

                x1=coordinates[neighbour]['Latitude']
                y1=coordinates[neighbour]['Longitude']

                x2=coordinates[end]['Latitude']
                y2=coordinates[end]['Longitude']

                heuristic=haversine_distance(x1,y1,x2,y2)
                weight=10

                #Similar to the admissible function but here we multiply the straight line distance multiplied by weight
                node_queue.append((n_cost+weight*heuristic,n_cost,n_path))
                node_queue.sort()

    return 0

def main():

    #using the networkx package, we create the graph
    G = nx.Graph()
    for index, rows in df.iterrows():
        start = rows['Distance in Kilometres']
        for end, distance in rows.iteritems():
            if end != 'Distance in Kilometres':
                if(distance=="-"):
                    distance=0
                else:
                    G.add_edge(start, end, distance=float(distance))
                

   
    while(True):
        flag=0
        start=input("Enter the starting place : ")
        end=input("Enter the ending place : ")

        start = start.replace(" ", "")
        if start not in coordinates.keys():
            flag=flag+1
        end = end.replace(" ", "")
        if end not in coordinates.keys():
            flag=flag+1
        #Delhi -> Nasik is an example which shows differnce in path in admissible and non admissible heuristics
        #Imphal -> Bombay

        if(flag==0):
            val1=uniform_cost_search(G,start,end)
            val2=A_star_admissible(G,start,end)
            val3=A_star_inadmissible(G,start,end)
            val_list=[val1,val2,val3]
            val_string=["UCS","A* admissible","A* Inadmissible"]

            for val in range(len(val_list)):
                if(val_list[val]!=0):
                    print("Cost for "+val_string[val]+" is : "+str(val_list[val]))
                else:
                    print("No path exists")   

            response=input("Do you wish to check for other places (Y/N): ")
            if(response=="N"):
                break 
            
        else:
            print("Places not found")

main()



