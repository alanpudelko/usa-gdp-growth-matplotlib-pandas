from matplotlib import pyplot as plt
import pandas as pd
import pyarrow

usa_gdp_data = pd.read_csv('year_csv.csv')

years = usa_gdp_data.date
changes = usa_gdp_data.change

years_list = [year for year in years]
changes_list = [change for change in changes]

plt.plot(years_list, changes_list, linewidth=2, color="red")

plt.title("GDP Growth in the US 1930-2015")
plt.xlabel("Years")
plt.ylabel("GDP Growth in %")


plt.show()
