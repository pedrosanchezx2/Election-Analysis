print("Hello, World")
counties = ["Arapahoe","Denver", "Jefferson"]

#Conditional

if counties [1] == "Denver":
    print(counties[1])
if counties [2] != "Jefferson":
    print(counties[2])
else :
    print(counties[0:2])

if "Arapahoe" in counties:
    print ("True")
else :
    print ("False")

if "El Paso" not in counties :
    print ("El paso is not in the list of counties")
else:
    print ("El paso is in the list of counties")

x = 5
y = 5

if not (x>y) :
    print ("True")
else :
    print ("False")

if "Arapahoe" in counties or "El Paso" in counties :
    print("Aparahoe and Denver are in the counties")
else:
    print("Aparahoe and Denver are not in the counties")


#LIST LOOP PRACTICE -  FOR
#numbers = [ 0 , 1 , 2 , 3 , 4 ]

#numbers = [0,1,2,3,4]
#for num in range(5) :
 #   print (num)
    
#for county in range(len(counties)):
 #   print (counties[county])


#TUPLE LOOP PRACTICE
#counties_tuple = ("Arapahoe", "Denver", "Jefferson")

#for county_tuple in range(len(counties_tuple)):
 #   print (counties_tuple[county_tuple])


#DICTIONARY LOOP PRACTICE
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Getting the values of the keys Method 1
#for county in counties_dict:
 #   print (counties_dict[county])


#Getting the values of the Keys Method 2
#for county in counties_dict:
 #   print(counties_dict.get(county))

#GET THE KEY - VALUE PAIRS OF A DICT - LOOP
#for county_votes in counties_dict.items():
 #   print (county_votes)

#GET THE KEY - VALUE PAIRS OF A DICT - LOOP 2  (NO COMA SEPARATING KEYS AND VALUES)
#for county, votes in counties_dict.items():
 #   print(county , votes)


#EXCERSICE HAVING A COMPLETE SENTENCE 
#for county, votes in counties_dict.items():
 #   print((county + " county has " + str(votes) + " registered votes "))


#Getting each dictionary in a list of dictionaries
voting_data = [{"county" : "Arapahoe", "registered_votes" : 422829}, 
                {"county" :  "Denver" , "registered_votes" : 463353},
                {"county" : "Jefferson" , "registered_votes" : 432438}]

#Printing the whole list
#for county_dict in voting_data:
 #   print(county_dict)


#Getting the keys 
#for i in range(len(voting_data)):
   # print(voting_data[i]["county"])

#getting the value on a nested loop
for county_dict in voting_data:
    for value in county_dict.values():
        print (value)


#Only the values as of registered_votes
#for county_dict in voting_data:
 #    print(county_dict["registered_votes"])

#Only the values as of counties
#for county_dict in voting_data:
 #   print(county_dict["county"])

##Printing Styles  -  print ()
print("Hello, World!")
#interes = 3
#print("Your interes for the year is $" + str(interest))

#f-string printing

#my_votes = int(input("How many votes did you get in the election?"))
#total_votes= int(input("What is the total votes in the election?"))
#percentage_votes = (my_votes / total_votes) * 100

#print("I received " + str(percentage_votes)+"% of the total votes")

#print(f" I received {percentage_votes}% of the total votes")


#f-string with dictionaries

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county , voters in counties_dict.items():
 #   print(county + " county has " + str(voters) + " registered voters.")

#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters} registered votes.")


#candidate_votes = int(input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes."
  #  f" The total number of votes in the election was {total_votes}."
   # f" You received {candidate_votes / total_votes * 100}% of the total votes"
#)

#print(message_to_candidate)

#Printing Values with decimal and coma format
#message_to_candidate = (
    #f"You received {candidate_votes:,} number of votes."
    #f" The total number of votes in the election was {total_votes:,}."
    #f" You received {candidate_votes / total_votes * 100:.2f}% of the total votes"
#)

#print(message_to_candidate)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters:,} registered votes.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data.items():
    for i in counties_dict:
    print(f"["i"] county has ["i:,"] registered votes")
        