import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as ticker
from pickle import TRUE
from datetime import date

import seaborn as sns 
# Read in bikes.csv into a pandas dataframe
bc=pd.read_csv('bikes.csv',index_col="bike_id") #index_col="bike_id", bc= bikes.csv
# Read in DOX.csv into a pandas dataframe
  #dc=doc.csv
# Be sure to parse the 'Date' column as a datetime
### Your code here ###
df = pd.read_csv("DOX.csv", index_col="Date", parse_dates=True)


fig, axs = plt.subplots(3, 2, figsize=(16, 20))


# Make a pie chart

### Your code here
#axs[0,0].set_title("Current Bike Status")
# bc["status"].value_counts().plot(kind="pie",ax=axs[0,0],autopct='%1.1f%%')


axs[0,0].set_title("Current Bike Status",fontsize=18,color="black")
axs[0,0].yaxis.set_visible(False)
patches, texts, pcts = axs[0,0].pie(
    bc["status"].value_counts(), labels=bc["status"].value_counts().index, autopct='%.1f%%',
    wedgeprops={ 'edgecolor': 'white'},
    textprops={'size': 'x-large'})
for i, patch in enumerate(patches):
  texts[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='white')
# Make a histogram with quartile lines
# There should be 20 bins
### Your code here


bc["purchase_price"].plot(kind="hist",bins=20,ax=axs[0,1],color="teal",histtype="step",)
axs[0,1].set_title("Price Histogram",fontsize=18,color="black")
axs[0,1].set_ylabel("Number of Bikes",color="black")
axs[0,1].set_xlabel("US Dollars",color="black")
axs[0,1].axvline(bc["purchase_price"].quantile(0.5), color='k', linestyle='dashed', linewidth=1)
axs[0,1].text(bc["purchase_price"].quantile(0.5)+10, 10, f'50%=${bc["purchase_price"].quantile(0.5):.0f}', rotation=90)
axs[0,1].axvline(bc["purchase_price"].quantile(0.25), color='k', linestyle='dashed', linewidth=1)
axs[0,1].text(bc["purchase_price"].quantile(0.25)+10, 10, f'25%=${bc["purchase_price"].quantile(0.25):.0f}', rotation=90)
axs[0,1].axvline(bc["purchase_price"].quantile(0.75), color='k', linestyle='dashed', linewidth=1)
axs[0,1].text(bc["purchase_price"].quantile(0.75)+10, 10, f'75%=${bc["purchase_price"].quantile(0.75):.0f}', rotation=90)
axs[0,1].axvline(bc["purchase_price"].min(), color='k', linestyle='dashed', linewidth=1)
axs[0,1].text(bc["purchase_price"].min()+10, 10, f'Min=${bc["purchase_price"].min():.0f}', rotation=90)
axs[0,1].axvline(bc["purchase_price"].max(), color='k', linestyle='dashed', linewidth=1)
axs[0,1].text(bc["purchase_price"].max()+10, 10, f'Max=${bc["purchase_price"].max():.0f}', rotation=90)
axs[0,1].xaxis.set_major_formatter(ticker.FormatStrFormatter(' $%d'))

# Make a scatter plot with a trend line
### Your code here
axs[1,0].scatter("purchase_price","weight",data=bc,s=1,color="red")
axs[1,0].set_title("Price vs Weight",fontsize=18,color="black")
axs[1,0].set_xlabel("Price",color="black",size = 14)
axs[1,0].set_ylabel("Weight",color="black",size = 14)
axs[1,0].xaxis.set_major_formatter(ticker.FormatStrFormatter('$%d'))
axs[1,0].yaxis.set_major_formatter(ticker.FormatStrFormatter('%d kg'))

# axs[1,0].xaxis.set_units('$')
# axs[1,0].yaxis.set_units('kg')



z=np.polyfit(bc["purchase_price"],bc["weight"],1)
p=np.poly1d(z)
axs[1,0].plot(bc["purchase_price"],p(bc["purchase_price"]))

#



axs[1,1].plot(df.index,df["Close"],color="green")
axs[1,1].xaxis.grid(True)
axs[1,1].yaxis.grid(True)
axs[1,1].set_title("DOX Closing Price",fontsize=18,color="black")


# Make a boxplot sorted so mean values are increasingss
# Hide outliers
### Your code here

def box_plot_sorted(df, by, column):
  df2 = pd.DataFrame({col:vals[column] for col, vals in df.groupby(by)})
  means = df2.mean().sort_values()
  df2[means.index].boxplot(ax=axs[2,0],showfliers=False)
  

df2 = pd.DataFrame({col:vals['purchase_price'] for col, vals in bc.groupby('brand')})
means = df2.mean().sort_values()


box_plot_sorted(bc, by='brand', column="purchase_price")

# bc.boxplot(column = "purchase_price",by='brand',ax = axs[2,0],showfliers=False)

# sns.boxplot(x="brand", y="purchase_price", data=bc,ax=axs[2,0],showfliers=False,showmeans=True,order=["Giant","GT","Canyon","Trek","BMC","Cdale"],color='teal')
# axs[2,0].grid(True)
axs[2,0].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%d'))
axs[2,0].set_title("Price vs Brand",fontsize=18,color="black")







# Make a violin plot
# bc.violinplot(column = "purchase_price",by='brand',ax = axs[2,1],showfliers=False)

sns.violinplot(x="brand", y="purchase_price", data=bc,ax=axs[2,1],order=means.index,color='teal',)

#["Giant","GT","Canyon","Trek","BMC","Cdale"]

axs[2,1].grid(False)
axs[2,1].set_title("Price vs Brand",fontsize=18,color="black")

# axs[2,1].violinplot(bc["purchase_price"])
# axs[2,1].set_title("Price Vs Brand",fontsize=18,color="black")



#bc.violinplot(column="purchase_price",by="brand",ax=axs[2,1],showfliers=False)
# axs[2,1].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%d'))
# axs[2,1].set_title("Price vs Brand",fontsize=18,color="black")


# Create some space between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

# Write out the plots as an image
plt.savefig('plots.png')
