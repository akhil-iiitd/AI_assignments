'''
ReadME

The dictionary KB contains the place name and also the various properties of each of the places. 

The functions would be update_KB_from_travel_KB(), recommend_destination(), add_new_destination(), add_feedback(), see_feedback()

We will be taking inputs from the user that asks the user to enter the weather, topography, number of people, budget, whether children present,
whether sports needed or not etc. Based on these inputs , we would calculate a score value that would give the best recommmendations out of the places
already in the database 

'''

KB = {
    "Munnar": {"weather": "cool","topography": "hilly","budget": "4000","cusines": ["South Indian", "North Indian"],"activities": {"trekking", "sightseeing", "tea plantation tour"},"adventure_sports": "yes","safety_rating": 9.5,"feedback": ["Breathtaking hill station with cool weather, fantastic trekking, and delicious South Indian cuisine.", "Stunning tea plantations and excellent safety standards."],"average_rating": 0},

    "Goa": {"weather": "tropical","topography": "beach","budget": "6000","cusines": ["Goan", "Seafood"],"activities": {"beach activities", "water sports", "nightlife"},"adventure_sports": "yes","safety_rating": 8.7,"feedback": [],"average_rating": 0},

    "Jaipur": {"weather": "hot","topography": "desert","budget": "3800","cusines": ["Rajasthani", "Indian"],"activities": {"historical sites", "shopping", "camel safari"}, "adventure_sports": "no","safety_rating": 8.9,"feedback": [],"average_rating": 0},

    "Paris": {"weather": "temperate","topography": "urban","budget": "30000","cusines": ["French", "European"],"activities": {"museums", "sightseeing", "cuisine tasting"},"adventure_sports": "no","safety_rating": 9.4,"feedback": [],"average_rating": 0},

    "Tokyo": {"weather": "mild","topography": "urban","budget": "18000","cusines": ["Japanese", "Asian"],"activities": {"cultural experiences", "sightseeing", "shopping"},"adventure_sports": "no","safety_rating": 9.2,"feedback": [],"average_rating": 0},
        
    "New York City": {"weather": "temperate","topography": "urban","budget": "31000","cusines": ["American", "International"],"activities": {"museums", "sightseeing", "Broadway shows"},"adventure_sports": "no","safety_rating": 9.1,"feedback": [],"average_rating": 0},
    
    "Bangkok": {"weather": "tropical","topography": "urban","budget": "12000","cusines": ["Thai", "Asian"],"activities": {"temples", "street food", "shopping"},"adventure_sports": "no","safety_rating": 8.8,"feedback": [],"average_rating": 0},
    
    "Sydney": {"weather": "temperate", "topography": "coastal","budget": "18500","cusines": ["Australian", "Seafood"], "activities": {"Opera House", "beaches", "wildlife encounters"},"adventure_sports": "yes","safety_rating": 9.3,"feedback": [],"average_rating": 0},
    
    "Cairo": {"weather": "hot","topography": "urban","budget": "13000","cusines": ["Egyptian", "Middle Eastern"],"activities": {"pyramids", "Nile cruises", "historic sites"},"adventure_sports": "no","safety_rating": 8.5,"feedback": [],"average_rating": 0},
    
    "Rio de Janeiro": {"weather": "tropical","topography": "beach","budget": "1400","cusines": ["Brazilian", "South American"],"activities": {"Carnival", "Christ the Redeemer", "beach parties"},"adventure_sports": "yes","safety_rating": 8.9,"feedback": [],"average_rating": 0},
    
    "Kolkata": {"weather": "tropical","topography": "urban","budget": "6000","cusines": ["Bengali", "Indian"],"activities": {"historical sites", "street food", "cultural events"},"adventure_sports": "no","safety_rating": 8.7,"feedback": [],"average_rating": 0},

    "Agra": {"weather": "hot","topography": "urban","budget": "4500","cusines": ["North Indian", "Mughlai"],"activities": {"Taj Mahal", "Agra Fort", "local markets"},"adventure_sports": "no","safety_rating": 8.8,"feedback": [],"average_rating": 0},

    "Kochi": {"weather": "tropical","topography": "coastal","budget": "5000","cusines": ["Kerala", "Seafood"],"activities": {"backwaters", "forts", "cultural performances"},"adventure_sports": "no","safety_rating": 9.0,"feedback": [],"average_rating": 0},

    "Amritsar": {"weather": "temperate","topography": "urban","budget": "3800","cusines": ["Punjabi", "Indian"],"activities": {"Golden Temple", "Wagah Border", "local food stalls"},"adventure_sports": "no","safety_rating": 8.6,"feedback": [],"average_rating": 0},

    "Shimla": {"weather": "cool","topography": "hilly","budget": "6200","cusines": ["Himachali", "Indian"],"activities": {"hill stations", "Mall Road", "nature walks"},"adventure_sports": "no","safety_rating": 8.9,"feedback": [],"average_rating": 0},

    "Phuket": {"weather": "tropical", "topography": "beach", "budget": "7500", "cusines": ["Thai", "Seafood"], "activities": {"beaches", "water sports", "island hopping"}, "adventure_sports": "yes", "safety_rating": 8.7, "feedback": [], "average_rating": 0},

    "Chiang Mai": {"weather": "temperate", "topography": "hilly", "budget": "6000", "cusines": ["Thai", "Northern Thai"], "activities": {"temples", "jungle trekking", "night markets"}, "adventure_sports": "yes", "safety_rating": 9.0, "feedback": [], "average_rating": 0},
    
    "Krabi": {"weather": "tropical", "topography": "beach", "budget": "6800", "cusines": ["Thai", "Seafood"], "activities": {"beaches", "rock climbing", "island hopping"}, "adventure_sports": "yes", "safety_rating": 8.8, "feedback": [], "average_rating": 0},
    
    "Pattaya": {"weather": "tropical", "topography": "beach", "budget": "7000", "cusines": ["Thai", "International"], "activities": {"beaches", "water sports", "theme parks"}, "adventure_sports": "yes", "safety_rating": 8.6, "feedback": [], "average_rating": 0},
    
    "Nice": {"weather": "temperate", "topography": "beach", "budget": "17500", "cusines": ["French", "Mediterranean"], "activities": {"beaches", "old town", "Mediterranean cuisine"}, "adventure_sports": "no", "safety_rating": 8.8, "feedback": [], "average_rating": 0},
    
    "Marseille": {"weather": "temperate", "topography": "coastal", "budget": "27000", "cusines": ["French", "Mediterranean"], "activities": {"historic sites", "Calanques", "seafood dining"}, "adventure_sports": "no", "safety_rating": 8.6, "feedback": [], "average_rating": 0},
    
    "Lyon": {"weather": "temperate", "topography": "urban", "budget": "19500", "cusines": ["French", "International"], "activities": {"Basilica of Notre-Dame de Fourvière", "culinary tours", "shopping"}, "adventure_sports": "no", "safety_rating": 8.9, "feedback": [], "average_rating": 0},
    
    "Bordeaux": {"weather": "temperate", "topography": "urban", "budget": "27300", "cusines": ["French", "Wine and Cheese"], "activities": {"vineyard tours", "historic architecture", "wine tasting"}, "adventure_sports": "no", "safety_rating": 8.7, "feedback": [], "average_rating": 0},

    "Brussels": {"weather": "temperate", "topography": "urban", "budget": "27000", "cusines": ["Belgian", "International"], "activities": {"Grand Place", "Atomium", "chocolate shops"}, "adventure_sports": "no", "safety_rating": 8.5, "feedback": [], "average_rating": 0},
    
    "Bruges": {"weather": "temperate", "topography": "urban", "budget": "17500", "cusines": ["Belgian", "Chocolates"], "activities": {"canal cruises", "historic town center", "chocolate tasting"}, "adventure_sports": "no", "safety_rating": 8.8, "feedback": [], "average_rating": 0},
    
    "Antwerp": {"weather": "temperate", "topography": "urban", "budget": "12200", "cusines": ["Belgian", "Seafood"], "activities": {"Cathedral of Our Lady", "diamond district", "harbor views"}, "adventure_sports": "no", "safety_rating": 8.6, "feedback": [], "average_rating": 0},
    
    "Ghent": {"weather": "temperate", "topography": "urban", "budget": "17300", "cusines": ["Belgian", "European"], "activities": {"Gravensteen Castle", "canal-side dining", "cultural events"}, "adventure_sports": "no", "safety_rating": 8.7, "feedback": [], "average_rating": 0},
    
    "Liege": {"weather": "temperate", "topography": "urban", "budget": "11100", "cusines": ["Belgian", "French"], "activities": {"Prince-Bishops' Palace", "Montagne de Bueren", "local cuisine"}, "adventure_sports": "no", "safety_rating": 8.5, "feedback": [], "average_rating": 0},

    "Kovalam": {"weather": "tropical", "topography": "beach", "budget": "6500", "cusines": ["Kerala", "Seafood"], "activities": {"beaches", "water sports", "lighthouses"}, "adventure_sports": "yes", "safety_rating": 8.7, "feedback": [], "average_rating": 0},
    
    "Wayanad": {"weather": "temperate", "topography": "hilly", "budget": "6200", "cusines": ["Kerala", "Indian"], "activities": {"wildlife sanctuaries", "trekking", "tea estates"}, "adventure_sports": "no", "safety_rating": 9.0, "feedback": [], "average_rating": 0},
    
    "Kozhikode": {"weather": "tropical", "topography": "urban", "budget": "4800", "cusines": ["Kerala", "Malabar"], "activities": {"beaches", "historic sites", "local cuisine"}, "adventure_sports": "no", "safety_rating": 8.6, "feedback": [], "average_rating": 0},
    
    "Thekkady": {"weather": "temperate", "topography": "hilly", "budget": "6300", "cusines": ["Kerala", "Indian"], "activities": {"Periyar Wildlife Sanctuary", "elephant rides", "spice gardens"}, "adventure_sports": "no", "safety_rating": 8.8, "feedback": [], "average_rating": 0}, 

    "Mysore": {"weather": "temperate", "topography": "urban", "budget": "3500", "cusines": ["South Indian", "Mysorean"], "activities": {"Mysore Palace", "Chamundi Hill", "yoga retreats"}, "adventure_sports": "no", "safety_rating": 8.8, "feedback": [], "average_rating": 0},

    "Coorg (Kodagu)": {"weather": "temperate", "topography": "hill station", "budget": "4500", "cusines": ["Coorgi", "South Indian"], "activities": {"coffee plantations", "trekking", "Abbey Falls"}, "adventure_sports": "no", "safety_rating": 8.7, "feedback": [], "average_rating": 0},

    "Hampi": {"weather": "hot", "topography": "hilly", "budget": "3000", "cusines": ["South Indian", "local"], "activities": {"ruins", "temples", "bouldering"}, "adventure_sports": "yes", "safety_rating": 8.6, "feedback": [], "average_rating": 0},

    "Gokarna": {"weather": "tropical", "topography": "beach", "budget": "2500", "cusines": ["South Indian", "Seafood"], "activities": {"beaches", "temple visits", "beach trekking"}, "adventure_sports": "yes", "safety_rating": 8.5, "feedback": [], "average_rating": 0},

    "Udupi": {"weather": "tropical", "topography": "coastal", "budget": "2800", "cusines": ["South Indian", "Udupi"], "activities": {"beaches", "temples", "vegetarian cuisine"}, "adventure_sports": "no", "safety_rating": 8.7, "feedback": [], "average_rating": 0}

}


def update_KB_from_travel_KB():
    try:
        #Trying to open the file that simply contained some reviews.. You may add new reviews, wont affect the functioning of the code
        travel_obj=open("Assignment-1/travel_KB.txt","r")
        data=travel_obj.read().split("|")
        for i in data:
            place_data=i.split(":")
            place=place_data[0].split("\n")[1]
            if place_data[0].split("\n")[1] in KB:
                KB[place]["average_rating"]=float(KB[place]["average_rating"])+float(place_data[1])/2
                reviews=place_data[2].split(",")
                for r in reviews:
                    KB[place_data[0].split("\n")[1]]["feedback"].append(r)
    except:
        print("No more data available")
    

def recommend_destination(weather,topography,budget,people,children,adventure):
    Score={}
    for i in KB:
        Score[i]=0
    
    for i in KB:
        if KB[i]["weather"]==weather:
            Score[i]+=5
        
        if KB[i]["topography"]==topography:
            Score[i]+=5
        

        if KB[i]["adventure_sports"]==adventure:
            Score[i]+=3

        if int(people)>3 and children=="yes":
            if KB[i]["safety_rating"]>7.5:
                Score[i]+=1

        if children=="no":
            if KB[i]["safety_rating"]>6.5:
                Score[i]+=2
        
        if int(KB[i]["budget"])<int(budget):
            Score[i]-=(int(KB[i]["budget"])/int(budget))
        
        
        sorted_dict = dict(sorted(Score.items(), key=lambda item: item[1]))
        #print(sorted_dict)
        recommended=[]
        for i in sorted_dict:
            recommended.append(i)
    return recommended


def add_new_destination(place):
    if place not in KB:
        print("Enter the details for "+place+"  :   ")
        weather=input("Weather for "+place+"  :   ")
        topography=input("Enter the topography for "+place+"  :   ")
        budget=input("Budget for "+place+"  :   ")

        n_cusines=input("Enter the number of cusines :  ")
        cusines=[]
        for i in range(int(n_cusines)):
            input(cusines[i])

        activities=[]
        n_activities=input("Enter the number of activities you want to enter    :   ")
        for i in range(int(n_activities)):
            input(activities[i])

        adv_sports=input("Adventure sports (Yes/No) :   ").lower()
        safety_rating=input("Enter the safety rating (1-10) :   ").lower()
        KB[place]={"weather":weather,"topography":topography,"budget": budget,"cusines":cusines,"adventure_sports":adv_sports,"activities":activities,"safety_rating":safety_rating,"feedback":[],"average_rating":0}
        
    else:
        print("Place already exists!")

def add_feedback(place):
    if place in KB:
        feedback=input("Enter the feedback for "+place)
        KB[place]["feedback"].append(feedback)
        rating=input("Enter rating for "+place)
        KB[place]["average_rating"]=(int(rating)+KB[place]["average_rating"])/2

def see_feedback(place):
    if KB[place]["feedback"]==[]:
        print("Feedback not found\n")
    if place in KB:
        for i in KB[place]["feedback"]:
            print(i)
    else:
        print("Place not found in the knowledge base")

def main():
    update_KB_from_travel_KB()

    weather_list=[]
    for i in KB:
        weather_list.append(KB[i]["weather"])

    topography_list=[]
    for i in KB:
        topography_list.append(KB[i]["topography"])

    while True:

        print("WEATHER \n"+"Available options for weather => ")
        for i in set(weather_list):
            print(i,end=", ")
        print("")
        weather=input("Enter the preferred weather condition for the place  :   ")
        print("\n")

        budget=input("Enter your budget :   ")
        print("\n")
        
        print("TOPOGRAPHY \n"+"Available options for topography => ")
        for i in set(topography_list):
            print(i,end=", ")
        print("")
        topography=input("What kind of topographical place are you looking for  :   ")
        print("\n")
        
        print("TRAVELLER DETAILS")
        people=input("How many people would be travelling   :   ")
        children=input("Any children in the group [yes/no]:   ").lower
        print("\n")

        print("SPORTS")
        adventure=input("Would you prefer adventure sports  [yes/no]:   ").lower

        print("\n")
        recommendations=(recommend_destination(weather,topography,budget,people,children,adventure))

        print("\nTop 3 recommendations are : \n")
        for i in range(3):
            print(i+1,end=" : ")
            print(recommendations[-1-i])
            print("The weather is "+KB[recommendations[-1-i]]["weather"])
            print("The topography is "+KB[recommendations[-1-i]]["topography"])

            print("Activities you could do : ",end=" : ")
            for act in KB[recommendations[-1-i]]["activities"]:
                print(act,end=",")

            print("\nCusines you could try : ",end=" : ")
            for cusine in KB[recommendations[-1-i]]["cusines"]:
                print(cusine,end=",")
            print("\n")

        feedback_check_val=input("Would you like to check feedback for a particular place ?(yes/no) : ")

        if(feedback_check_val.lower()=="yes"):
            location=input("Enter the place you want to check feedack of : ")
            see_feedback(location)
            
        user_destination=input("Would you like to add new destinations? : ")
        if(user_destination.lower()=="yes"):
            dest=input("Enter new destination name : ")
            add_new_destination(dest)

        feedback_add_val=input("Would you like to give feedback on the place? : ")
        if(feedback_add_val.lower()=="yes"):
            location=input("Enter the place you want to write feedack to : ")
            add_feedback(location)
        
        another=input("Would you like to get another recommendation ? (yes/no)")
        if(another=="no"):
            break
        else:
            pass

main()

