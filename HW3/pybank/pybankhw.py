# import dependencies
import pandas as pd

# set variable to first raw CSV file path
file1 = "/Users/marksquier/desktop/learnpython/hw_resources/budget_data_1.csv"

# convert CSV to data frame
df1 = pd.read_csv(file1)

# return total months
total_months = len(df1["Date"].unique())

# return total revenue
total_revenue = df1["Revenue"].sum()

# return average change (b/w months)
# NOTE: data frame is already organized in chronological order
average_change = round(((df1.loc[40, "Revenue"] - df1.loc[0, "Revenue"])/len(df1)), 2)

# create new column with rev diff b/w months
df1["Diff"] = df1["Revenue"] - df1["Revenue"].shift(1)

# return greatest rev inc b/w any two months
rev_inc = df1["Diff"].max()

# date of greatest revenue increase
inc_row = df1["Diff"].idxmax()
date_inc = df1.loc[inc_row, "Date"]

# return greatest rev dec b/w any two months
rev_dec = df1["Diff"].min()

# date of greatest revenue decrease
dec_row = df1["Diff"].idxmin()
date_dec = df1.loc[dec_row, "Date"]

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
summary1 = pd.DataFrame({'Total months': int(total_months),
                        'Total revenue': int(total_revenue),
                        'Average revenue change': int(average_change),
                        'Greatest increase in revenue': [str(date_inc) + ' $' + str(rev_inc)],
                        'Greatest decrease in revenue': [str(date_dec) + ' $' + str(rev_dec)]
                        
    
})


# set variable to second raw CSV file path
file2 = "/Users/marksquier/desktop/learnpython/hw_resources/budget_data_2.csv"

# convert CSV to data frame
df2 = pd.read_csv(file2)

# return total months
total_months2 = len(df2["Date"].unique())

# return total revenue
total_revenue2 = df2["Revenue"].sum()

# return average change (b/w months)
average_change2 = round(((df2.loc[40, "Revenue"] - df2.loc[0, "Revenue"])/len(df2)), 2)

# create new column with rev diff b/w months
df2["Diff"] = df2["Revenue"] - df2["Revenue"].shift(1)
df2.head()

# return greatest rev inc b/w any two months
rev_inc2 = df2["Diff"].max()

# date of greatest revenue increase
inc_row2 = df2["Diff"].idxmax()
date_inc2 = df2.loc[inc_row, "Date"]

# return greatest rev dec b/w any two months
rev_dec2 = df2["Diff"].min()

# date of greatest revenue decrease
dec_row2 = df2["Diff"].idxmin()
date_dec2 = df2.loc[dec_row, "Date"]

# print second analysis to terminal
print()
print('Financial Analysis 2')
print('--------------------------------')
print('Total months: ' + str(total_months2))
print('Total revenue: $' + str(total_revenue2))
print('Average revenue change: $' + str(average_change2))
print('Greatest increase in revenue: ' + str(date_inc2) + ' $' + str(rev_inc2))
print('Greatest decrease in revenue: ' + str(date_dec2) + ' $' + str(rev_dec2))

# create new data frame with summary of second report
summary2 = pd.DataFrame({'Total months': int(total_months2),
                        'Total revenue': int(total_revenue2),
                        'Average revenue change': int(average_change2),
                        'Greatest increase in revenue': [str(date_inc2) + ' $' + str(rev_inc2)],
                        'Greatest decrease in revenue': [str(date_dec2) + ' $' + str(rev_dec2)]
})

# merge both report summaries
combined_df = pd.merge(summary1, summary2, 
						how = 'outer')

# print combined summary to terminal
print()
print('Combined reports:')
print(combined_df)

# export merged summary to CSV
combined_df.to_csv("/Output/Combined Financial Analysis.csv", encoding='UTF-8', index=False, header=True)