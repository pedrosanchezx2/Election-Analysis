#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote



# Assign a variable for the file to load and the path.

#file_to_load = 'Resources\election_results.csv'
#Open the file
#election_data = open(file_to_load,'r')
#To do: perform analysis
#print(election_data)
#Close the file
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:

    # To Do: perform analysis.
 #   print(election_data)

#import csv
#import os

# Assign a variable for the file to load and the path.

#file_data = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.

#with open(file_data) as election_data:
 #   print(election_data)

# Create a filename variable to a direct or indirect path to the file.

#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# Use the open statement to open the file as a text file.

#outfile = open(file_to_save,"w")

# Write some data to the file.
#outfile.write("Hello, World!")

#Close the file
#outfile.close()

# Using the with statement open the file as a text file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")


#with open(file_to_save, "w") as txt_file:

        # Write some data to the file. Method 1
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson.")
        # Write some data to the file. Method 2
#    txt_file.write("Arapahoe, Denver, Jefferson")

     # Write three counties to the file. Method 3
 #   txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")


# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
#total_votes = 0


# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #file_reader = csv.reader(election_data)

    #Print each row in the cvs file.
#for row in file_reader:
  # Print the header row.
    #file_reader = csv.reader(election_data)
    
    #headers = next(file_reader)
    #for row in file_reader:
     #   total_votes += 1
#Print the total votes
    
    #    print(total_votes)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.


        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
            #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)    

# Initialize a total vote counter.
total_votesa = 0
# Candidate options and candidate votes
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votesa += 1
        # Get the candidate name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if county_name not in county_options:
            # Add the candidate name to the candidate list.
            county_options.append(county_name)
            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count
        county_votes[county_name] += 1
        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    county_election_results = (
        f"\nElection County Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votesa:,}\n"
        f"-------------------------\n")
    print(county_election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for county_name in county_votes:
        # Retrieve vote count and percentage.
        votesa = county_votes[county_name]
        vote_percentage_county = float(votesa) / float(total_votesa) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.


        county_results = (f"{county_name}: {vote_percentage_county:.1f}% ({votesa:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
            #  Save the candidate results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votesa > winning_count_county) and (vote_percentage_county > winning_percentage_county):
            winning_count_county = votesa
            winning_county = county_name
            winning_percentage_county = vote_percentage_county
    # Print the winning candidates' results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"County with more votes: {winning_county}\n"
        f"Counts in the county: {winning_count_county:,}\n"
        f"Total percentage of votes in the county: {winning_percentage_county:.1f}%\n"
        f"-------------------------\n")

    print(winning_county_summary)
    # Save the final vote count to the text file.
    txt_file.write(winning_county_summary)  

            # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.


    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.


    # Print the candidate list.
    #Print the total votes
            #print(total_votes)
    #print(candidate_options)
    # Print the candidate vote dictionary.
    #print(candidate_votes)