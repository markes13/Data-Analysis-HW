

```python
import pandas as pd
import numpy as np
import os
```


```python
json_path = os.path.join("Resources", "purchase_data.json")
```


```python
df = pd.read_json(json_path)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Player Count

# determine total number of players
total_players = len(df["SN"].unique())
total_players
```




    573




```python
# Purchasing Analysis

# number of unique items
unique_item_count = len(df["Item Name"].unique())

# average purchase price
avg_purchase_price = round(df["Price"].mean(), 2)

# total number of purchases
total_purchases = len(df)

# total revenue
total_revenue = df["Price"].sum()

total_purchases
```




    780




```python
# build dfs for males and females

males = df.loc[df["Gender"]=="Male", :]
females = df.loc[df["Gender"]=="Female", :]
```


```python
# Gender Demographics

# % and count of male players
count_males = len(males["SN"].unique())
percent_males = round((count_males/total_players)*100, 2)

# % and count of female players
count_females = len(females["SN"].unique())
percent_females = round((count_females/total_players)*100, 2)

# % and count of other
count_other = total_players - count_males - count_females
percent_other = round((count_other/total_players)*100, 2)
```


```python
# Purchasing Analysis (Gender)

# purchase count by gender
# males
male_purchase_count = len(males)
average_male_purchase_price = round(males["Price"].mean(), 2)
total_male_purchase_value = males["Price"].sum()
males_normalized = round(total_male_purchase_value/count_males, 2)

# females
female_purchase_count = len(females)
average_female_purchase_price = round(females["Price"].mean(), 2)
total_female_purchase_value = females["Price"].sum()
females_normalized = round(total_female_purchase_value/count_females, 2)
```


```python
# Age Demographics

# make bins and labels
bins = [(df["Age"].min()-1), 17, 26, 35, (df["Age"].max()+1)]
group_names = ["Child", "Young Adult", "Adult", "Parent"]

# add new bin column to df
df["Age Category"] = pd.cut(df["Age"], bins, labels=group_names)

# get purchase count
child_purchase_count = len(df.loc[df["Age Category"] == "Child", :])
young_adult_purchase_count = len(df.loc[df["Age Category"]=="Young Adult", :])
adult_purchase_count = len(df.loc[df["Age Category"]=="Adult", :])
parent_purchase_count = len(df.loc[df["Age Category"]=="Parent", :])

# get avg. purchase price
child = df.loc[df["Age Category"] == "Child", :]
child_purchase_price_ = round(child["Price"].mean(), 2)
young_adult = df.loc[df["Age Category"]=="Young Adult", :]
young_adult_purchase_price_avg = round(young_adult["Price"].mean(), 2)
adult = df.loc[df["Age Category"]=="Adult", :]
adult_purchase_price_avg = round(adult["Price"].mean(), 2)
parent = df.loc[df["Age Category"]=="Parent", :]
parent_purchase_price_avg = round(parent["Price"].mean(), 2)

# get total purchase value
child_purchase_tot = child["Price"].sum()
young_adult_purchase_tot = young_adult["Price"].sum()
adult_purchase_tot = adult["Price"].sum()
parent_purchase_tot = parent["Price"].sum()

# normalized totals

# get count for each age group first
child_count = len(child["SN"].unique())
young_adult_count = len(young_adult["SN"].unique())
adult_count = len(adult["SN"].unique())
parent_count = len(parent["SN"].unique())

# now get normalized totals
child_normalized = round(child_purchase_tot/child_count, 2)
young_adult_normalized = round(young_adult_purchase_tot/young_adult_count, 2)
adult_normalized = round(adult_purchase_tot/adult_count, 2)
parent_normalized = round(parent_purchase_tot/parent_count, 2)

age_group = df.groupby("Age Category")
age_group["SN"].count()
```




    Age Category
    Child          150
    Young Adult    462
    Adult          121
    Parent          47
    Name: SN, dtype: int64




```python
# Top Spenders

# group by SN
spenders = df.groupby("SN")
spenders = spenders.sum()

# sort by highest price total
spenders = spenders.nlargest(5, ["Price"])
spenders = spenders.reset_index()

# gather all rows for top 5 spenders
spender1_table = df.loc[df["SN"]==spenders["SN"][0], :]
spender2_table = df.loc[df["SN"]==spenders["SN"][1], :]
spender3_table = df.loc[df["SN"]==spenders["SN"][2], :]
spender4_table = df.loc[df["SN"]==spenders["SN"][3], :]
spender5_table = df.loc[df["SN"]==spenders["SN"][4], :]

# sn for each spender
spender1_sn = spenders["SN"][0]
spender2_sn = spenders["SN"][1]
spender3_sn = spenders["SN"][2]
spender4_sn = spenders["SN"][3]
spender5_sn = spenders["SN"][4]

# purchase count for each spender
spender1_count = len(spender1_table)
spender2_count = len(spender2_table)
spender3_count = len(spender3_table)
spender4_count = len(spender4_table)
spender5_count = len(spender5_table)

# average purchase price for each spender
spender1_avg = round(spender1_table["Price"].mean(), 2)
spender2_avg = round(spender2_table["Price"].mean(), 2)
spender3_avg = round(spender3_table["Price"].mean(), 2)
spender4_avg = round(spender4_table["Price"].mean(), 2)
spender5_avg = round(spender5_table["Price"].mean(), 2)

# total purchase value for each spender
spender1_tot = spender1_table["Price"].sum()
spender2_tot = spender2_table["Price"].sum()
spender3_tot = spender3_table["Price"].sum()
spender4_tot = spender4_table["Price"].sum()
spender5_tot = spender5_table["Price"].sum()

# create top 5 spenders df
top_spenders_df = pd.DataFrame({"SN":[spender1_sn, spender2_sn, spender3_sn, spender4_sn, spender5_sn],
                                "Total Purchases":[spender1_count, spender2_count, spender3_count,
                                                   spender4_count, spender5_count],
                                "Average Purchase Price":[spender1_avg, spender2_avg, spender3_avg,
                                                          spender4_avg, spender5_avg],
                                "Total Purchase Value":[spender1_tot, spender2_tot, spender3_tot,
                                                        spender4_tot, spender5_tot]})
top_spenders_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>SN</th>
      <th>Total Purchase Value</th>
      <th>Total Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.41</td>
      <td>Undirrala66</td>
      <td>17.06</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.39</td>
      <td>Saedue76</td>
      <td>13.56</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.18</td>
      <td>Mindimnya67</td>
      <td>12.74</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.24</td>
      <td>Haellysu29</td>
      <td>12.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.86</td>
      <td>Eoda93</td>
      <td>11.58</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items

# group by item ID
items = df.groupby("Item ID")
items = items.count()

# sort by count
items = items.nlargest(5, "Price")
items = items.reset_index()

# gather all rows for top 5 items
item1_table = df.loc[df["Item ID"]==items["Item ID"][0], :]
item2_table = df.loc[df["Item ID"]==items["Item ID"][1], :]
item3_table = df.loc[df["Item ID"]==items["Item ID"][2], :]
item4_table = df.loc[df["Item ID"]==items["Item ID"][3], :]
item5_table = df.loc[df["Item ID"]==items["Item ID"][4], :]

# gather item IDs
item1_id = items["Item ID"][0]
item2_id = items["Item ID"][1]
item3_id = items["Item ID"][2]
item4_id = items["Item ID"][3]
item5_id = items["Item ID"][4]

# gather item names
item1_name = item1_table["Item Name"].unique()[0]
item2_name = item2_table["Item Name"].unique()[0]
item3_name = item3_table["Item Name"].unique()[0]
item4_name = item4_table["Item Name"].unique()[0]
item5_name = item5_table["Item Name"].unique()[0]

# gather item purchase counts
item1_count = len(item1_table)
item2_count = len(item2_table)
item3_count = len(item3_table)
item4_count = len(item4_table)
item5_count = len(item5_table)

# gather item prices
item1_price = item1_table["Price"].unique()[0]
item2_price = item2_table["Price"].unique()[0]
item3_price = item3_table["Price"].unique()[0]
item4_price = item4_table["Price"].unique()[0]
item5_price = item5_table["Price"].unique()[0]

# gather total purchase value
item1_tot = round(item1_table["Price"].sum(), 2)
item2_tot = round(item2_table["Price"].sum(), 2)
item3_tot = round(item3_table["Price"].sum(), 2)
item4_tot = round(item4_table["Price"].sum(), 2)
item5_tot = round(item5_table["Price"].sum(), 2)

# create top 5 most popular items df
most_popular_items_df = pd.DataFrame({"Item ID":[item1_id, item2_id, item3_id, item4_id, item5_id],
                                      "Item Name":[item1_name, item2_name, item3_name, item4_name, item5_name],
                                      "Total Purchases":[item1_count, item2_count, item3_count, item4_count, item5_count],
                                      "Price":[item1_price, item2_price, item3_price, item4_price, item5_price],
                                      "Total Purchase Value":[item1_tot, item2_tot, item3_tot, item4_tot, item5_tot]})

most_popular_items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
      <th>Total Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>25.85</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>24.53</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>13.41</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>18.63</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>37.26</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items

# group by item ID
items2 = df.groupby("Item ID")
items2 = items2.sum()

# sort by total profit
items2 = items2.nlargest(5, "Price")
items2 = items2.reset_index()

# gather all rows for top 5 most profitable items
prof1_table = df.loc[df["Item ID"]==items2["Item ID"][0]]
prof2_table = df.loc[df["Item ID"]==items2["Item ID"][1]]
prof3_table = df.loc[df["Item ID"]==items2["Item ID"][2]]
prof4_table = df.loc[df["Item ID"]==items2["Item ID"][3]]
prof5_table = df.loc[df["Item ID"]==items2["Item ID"][4]]

# gather item IDs
prof1_id = items2["Item ID"][0]
prof2_id = items2["Item ID"][1]
prof3_id = items2["Item ID"][2]
prof4_id = items2["Item ID"][3]
prof5_id = items2["Item ID"][4]

# gather item names
prof1_name = prof1_table["Item Name"].unique()[0]
prof2_name = prof2_table["Item Name"].unique()[0]
prof3_name = prof3_table["Item Name"].unique()[0]
prof4_name = prof4_table["Item Name"].unique()[0]
prof5_name = prof5_table["Item Name"].unique()[0]

# gather purchase counts
prof1_count = len(prof1_table)
prof2_count = len(prof2_table)
prof3_count = len(prof3_table)
prof4_count = len(prof4_table)
prof5_count = len(prof5_table)

# gather item prices
prof1_price = prof1_table["Price"].unique()[0]
prof2_price = prof2_table["Price"].unique()[0]
prof3_price = prof3_table["Price"].unique()[0]
prof4_price = prof4_table["Price"].unique()[0]
prof5_price = prof5_table["Price"].unique()[0]

# gather total item purchase values
prof1_tot = round(prof1_table["Price"].sum(), 2)
prof2_tot = round(prof2_table["Price"].sum(), 2)
prof3_tot = round(prof3_table["Price"].sum(), 2)
prof4_tot = round(prof4_table["Price"].sum(), 2)
prof5_tot = round(prof5_table["Price"].sum(), 2)

# create most profitable items df
most_profitable_items_df = pd.DataFrame({"Item ID":[prof1_id, prof2_id, prof3_id, prof4_id, prof5_id],
                                         "Item Name":[prof1_name, prof2_name, prof3_name, prof4_name, prof5_name],
                                         "Total Purchases":[prof1_count, prof2_count, prof3_count,
                                                            prof4_count, prof5_count],
                                         "Price":[prof1_price, prof2_price, prof3_price, prof4_price, prof5_price],
                                         "Total Profit":[prof1_tot, prof2_tot, prof3_tot, prof4_tot, prof5_tot]})
most_profitable_items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Profit</th>
      <th>Total Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>37.26</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>29.75</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>29.70</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
      <td>29.22</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>28.88</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Summary
summary_df = pd.DataFrame({"Total Players":[total_players], "Unique Items":[unique_item_count], 
                           "Average Purchase Price":[avg_purchase_price], "Total Purchases":[total_purchases],
                           "Total Revenue":[total_revenue], "Male Players":[count_males], "Percent Male":[percent_males],
                           "Female Players":[count_females], "Percent Female":[percent_females], 
                           "Gender N/A Players":[count_other], "Percent Gender N/A":[percent_other],
                           })
summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Female Players</th>
      <th>Gender N/A Players</th>
      <th>Male Players</th>
      <th>Percent Female</th>
      <th>Percent Gender N/A</th>
      <th>Percent Male</th>
      <th>Total Players</th>
      <th>Total Purchases</th>
      <th>Total Revenue</th>
      <th>Unique Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>100</td>
      <td>8</td>
      <td>465</td>
      <td>17.45</td>
      <td>1.4</td>
      <td>81.15</td>
      <td>573</td>
      <td>780</td>
      <td>2286.33</td>
      <td>179</td>
    </tr>
  </tbody>
</table>
</div>


