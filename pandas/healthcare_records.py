import pandas as pd
import numpy as np

# bringing in a healthcare dataset (if not in current directory we can add the path to the csv)
df = pd.read_csv('healthcare_dataset.csv')

# displaying the first ten rows of the dataset
dfHead = df.head(10)

# shows some descriptive statistics about the health care dataset
dfDescribe = df.describe()

# shows types of each column
dfType = df.dtypes
print(dfType)

# returns a tuple that can show dimensions of dataset (attribute not a method)
dfShape = df.shape

# shows the columns and how many NaN values are in each column 
catNull = df.isnull().sum()
totalNull = df.isnull().sum().sum() #(or how many NaN values are in the entire dataset)

# show the complete rows of the dataset with the missing values
print(df[df.isnull().any(axis=1)])

# output shows 32 total missing values
# depending on the project we can either drop the rows with missing values, fill with mean/median/mode of the column, fill with 0, or interpolate

# Example of dropping na rows
df = df.dropna(subset='Blood Type') 
catNullDrop = df.isnull().sum()
totalNullDrop = df.isnull().sum().sum()

# Example of filling na values with mean for a specific column
mean_age = np.round(df['Age'].mean())
df = df.fillna({'Age':mean_age}) # use of inplace=True would avoid making a copy of the object and instead updates the original df
catNullMean = df.isnull().sum()
totalNullMean = df.isnull().sum().sum()

# Example of filling na values with zero for specific column 
df = df.fillna({'Billing Amount': 0}) 
catNullZero = df.isnull().sum()
totalNullZero = df.isnull().sum().sum()

# Example of interpolating for specific column 
df['Room Number'] = df['Room Number'].interpolate() # note we could use combo foward fill and back fill to ensure that the first and last values are interpolated as well 
catNullInterpolate = df.isnull().sum()
totalNullInterpolate = df.isnull().sum().sum()

# fix values in the Name column to be appropriate case
df['Name'] = df['Name'].str.title()

# make use of memory and changed Room Number to int16 since values are integers between 100 and 1000
df['Room Number'] = df['Room Number'].astype('int16')
dfTypeNew = df.dtypes

# for visualization later have billing amounts in the form of currency which have two decimal places
df['Billing Amount'] = np.round(df['Billing Amount'],2)

# creating a dataframe of just the male patients
dfMale = df.loc[df['Gender']=='Male']
dfMale = dfMale.reset_index(drop=True)

billingGender = df.groupby('Gender').agg(count=('Name','size'),totalBillAmt = ('Billing Amount','sum'))


print(billingGender)
print(type(billingGender))
print(df.isnull().sum().sum())
