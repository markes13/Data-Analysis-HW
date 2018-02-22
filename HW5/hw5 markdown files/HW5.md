

```python
# Import dependencies
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
```


```python
# Set file paths
city_path = 'raw_data/city_data.csv'
ride_path = 'raw_data/ride_data.csv'

# Read CSVs into data frames
city_df = pd.read_csv(city_path)
ride_df = pd.read_csv(ride_path)
```


```python
# Average fare per city
rides_group = ride_df.groupby("city", as_index=False)
avg_fare_city = round(rides_group["fare"].mean(), 2)

# Total number of rides per city
tot_rides_city = rides_group.count()
tot_rides_city = tot_rides_city.drop(["date", "ride_id"], axis=1)
tot_rides_city = tot_rides_city.rename(columns={"fare":"Count of Rides"})

# Total number of drivers per city
cities_group = city_df.groupby("city", as_index=False)
drivers_per_city = cities_group["driver_count"].sum()
```


```python
# Combine fields into data frames

# first drop driver count from groupby object
city_type = city_df.drop(["driver_count"], axis=1)

# df1
plot_df1 = pd.merge(avg_fare_city, tot_rides_city, how='outer')

#df2
plot_df2 = pd.merge(drivers_per_city, city_type, how='outer')

# Combined df
plot_df = pd.merge(plot_df1, plot_df2, how='outer', on='city')

# rename column
plot_df = plot_df.rename(columns={"type": "City Type"})

plot_df.head()
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
      <th>city</th>
      <th>fare</th>
      <th>Count of Rides</th>
      <th>driver_count</th>
      <th>City Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>23.93</td>
      <td>31</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>20.61</td>
      <td>26</td>
      <td>67</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anitamouth</td>
      <td>37.32</td>
      <td>9</td>
      <td>16</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antoniomouth</td>
      <td>23.62</td>
      <td>22</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aprilchester</td>
      <td>21.98</td>
      <td>19</td>
      <td>49</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# categorize data into new data frames by city type

# Urban
urban_df = plot_df.loc[plot_df["City Type"]=='Urban', :]

# Suburban
suburban_df = plot_df.loc[plot_df["City Type"]=='Suburban', :]

# Rural
rural_df = plot_df.loc[plot_df["City Type"]=='Rural', :]
```


```python
fig, ax = plt.subplots()
plt.scatter(x=urban_df['Count of Rides'], y=urban_df['fare'], c='gold', alpha=0.75, s=urban_df['driver_count'],label='Urban', linewidths=2)
plt.scatter(x=rural_df['Count of Rides'], y=rural_df['fare'], c='lightskyblue', alpha=1, s=rural_df['driver_count'], label='Rural')
plt.scatter(x=suburban_df['Count of Rides'], y=suburban_df['fare'], c='lightcoral', alpha=1, s=suburban_df['driver_count'], label='Suburban')
plt.legend(loc='best')
plt.xlabel("Total Rides per City")
plt.ylabel("Average Fare per City")
plt.title("Pyber Data by City Type")
plt.xlim(-0.5, 37)
plt.ylim(15, 55)
plt.text(40, 40, '*Circle size corresponds to total number of drivers in city.')
plt.grid()
plt.show()
```


![png](output_5_0.png)



```python
# Pie charts

# % of Total Rides by City Type
labels = ['Urban', 'Rural', 'Suburban']
sizes = [len(urban_df), len(rural_df), len(suburban_df)]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = [0.1, 0.1, 0.1]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.title("% of Total Rides by City Type")
plt.show()
```


![png](output_6_0.png)



```python
# % of Fare by City Type

labels = ['Urban', 'Rural', 'Suburban']
sizes = [urban_df["fare"].sum(), rural_df["fare"].sum(), suburban_df["fare"].sum()]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = [0.1, 0.1, 0.1]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.title("% of Total Fare by City Type")
plt.show()
```


![png](output_7_0.png)



```python
# % of Fare by City Type

labels = ['Urban', 'Rural', 'Suburban']
sizes = [urban_df["driver_count"].sum(), rural_df["driver_count"].sum(), suburban_df["driver_count"].sum()]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = [0.1, 0.1, 0.1]
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.title("% of Total Drivers by City Type")
plt.show()
```


![png](output_8_0.png)

