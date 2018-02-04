
# coding: utf-8
import pandas as pd

# set csv path
csv_path1 = "/Users/marksquier/desktop/election_data_1.csv"

# convert csv to data frame
df1 = pd.read_csv(csv_path1)
df1.head()

# count total votes
total_votes = len(df1["Voter ID"].unique())
#print(total_votes)

# build list of candidates
candidates_list = []
for i in df1["Candidate"].unique():
    candidates_list.append(i)
#print(candidates_list)

# get percentage of total votes for each candidate
# cand 1
can1_count = df1["Candidate"].loc[df1["Candidate"] == str(candidates_list[0])].count()
can1_perc = (can1_count/total_votes) * 100
# cand 2
can2_count = df1["Candidate"].loc[df1["Candidate"] == str(candidates_list[1])].count()
can2_perc = (can2_count/total_votes) * 100
# cand 2
can3_count = df1["Candidate"].loc[df1["Candidate"] == str(candidates_list[2])].count()
can3_perc = (can3_count/total_votes) * 100
# can 4
can4_count = df1["Candidate"].loc[df1["Candidate"] == str(candidates_list[3])].count()
can4_perc = (can4_count/total_votes) * 100

# make new data frame with candidate percentages
perc_df = pd.DataFrame({"Candidate":[str(candidates_list[0]), str(candidates_list[1]), 
                                     str(candidates_list[2]), str(candidates_list[3])],
                       "Vote %" : [can1_perc, can2_perc, can3_perc, can4_perc]})

perc_df.head()
winner = perc_df.loc[perc_df["Vote %"] == perc_df["Vote %"].max(), :]
#print(winner)

# print results
print()
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------------")
print(str(candidates_list[0]) + ": " + str(can1_perc) + "% (" + str(can1_count) + ")")
print(str(candidates_list[1]) + ": " + str(can2_perc) + "% (" + str(can2_count) + ")")
print(str(candidates_list[2]) + ": " + str(can3_perc) + "% (" + str(can3_count) + ")")
print(str(candidates_list[3]) + ": " + str(can4_perc) + "% (" + str(can4_count) + ")")
print("--------------------------------")
print("Winner:")
print(winner)
print()