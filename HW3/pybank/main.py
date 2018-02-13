# import dependencies
import pandas as pd
import os

# set variable to first raw CSV file path
file1 = os.path.join("Raw Data", "budget_data_1.csv")

# convert CSV to data frame
bank_df = pd.read_csv(file1)

# return total months
total_months = len(bank_df["Date"].unique())

# return total revenue
total_revenue = bank_df["Revenue"].sum()

# return average change (b/w months)
# NOTE: data frame is already organized in chronological order
average_change = round(((bank_df.loc[(total_months - 1), "Revenue"] - bank_df.loc[0, "Revenue"])/len(bank_df)), 2)

# create new column with rev diff b/w months
bank_df["Diff"] = bank_df["Revenue"] - bank_df["Revenue"].shift(1)

# return greatest rev inc b/w any two months
rev_inc = bank_df["Diff"].max()

# date of greatest revenue increase
inc_row = bank_df["Diff"].idxmax()
date_inc = bank_df.loc[inc_row, "Date"]

# return greatest rev dec b/w any two months
rev_dec = bank_df["Diff"].min()

# date of greatest revenue decrease
dec_row = bank_df["Diff"].idxmin()
date_dec = bank_df.loc[dec_row, "Date"]

# print first analysis to terminal
print()
print('Financial Analysis 1')
print('--------------------------------')
print('Total months: ' + str(total_months))
print('Total revenue: $' + str(total_revenue))
print('Average revenue change: $' + str(average_change))
print('Greatest increase in revenue: ' + str(date_inc) + ' $' + str(rev_inc))
print('Greatest decrease in revenue: ' + str(date_dec) + ' $' + str(rev_dec))


# create new data frame with summary of first report
summary = pd.DataFrame({'Total months': int(total_months),
                        'Total revenue': int(total_revenue),
                        'Average revenue change': int(average_change),
                        'Greatest increase in revenue': [str(date_inc) + ' $' + str(rev_inc)],
                        'Greatest decrease in revenue': [str(date_dec) + ' $' + str(rev_dec)]
                        
    
})

# export summary to CSV
summary.to_csv("/Output/First Financial Analysis.csv", encoding='UTF-8', index=False, header=True)

# REPEAT FOR SECOND DATA SET

# set variable to second raw CSV file path
file = os.path.join("Raw Data", "budget_data_2.csv")

# convert CSV to data frame
bank_df = pd.read_csv(file)

# return total months
total_months = len(bank_df["Date"].unique())

# return total revenue
total_revenue = bank_df["Revenue"].sum()

# return average change (b/w months)
average_change = round(((bank_df.loc[(total_months -1), "Revenue"] - bank_df.loc[0, "Revenue"])/len(bank_df)), 2)

# create new column with rev diff b/w months
bank_df["Diff"] = bank_df["Revenue"] - bank_df["Revenue"].shift(1)
bank_df.head()

# return greatest rev inc b/w any two months
rev_inc = bank_df["Diff"].max()

# date of greatest revenue increase
inc_row = bank_df["Diff"].idxmax()
date_inc = bank_df.loc[inc_row, "Date"]

# return greatest rev dec b/w any two months
rev_dec = bank_df["Diff"].min()

# date of greatest revenue decrease
dec_row = bank_df["Diff"].idxmin()
date_dec = bank_df.loc[dec_row, "Date"]

# print second analysis to terminal
print()
print('Financial Analysis 2')
print('--------------------------------')
print('Total months: ' + str(total_months))
print('Total revenue: $' + str(total_revenue))
print('Average revenue change: $' + str(average_change))
print('Greatest increase in revenue: ' + str(date_inc) + ' $' + str(rev_inc))
print('Greatest decrease in revenue: ' + str(date_dec) + ' $' + str(rev_dec))

# create new data frame with summary of second report
summary = pd.DataFrame({'Total months': int(total_months),
                        'Total revenue': int(total_revenue),
                        'Average revenue change': int(average_change),
                        'Greatest increase in revenue': [str(date_inc) + ' $' + str(rev_inc)],
                        'Greatest decrease in revenue': [str(date_dec) + ' $' + str(rev_dec)]
})

# export merged summary to CSV
summary.to_csv("/Output/Second Financial Analysis.csv", encoding='UTF-8', index=False, header=True)