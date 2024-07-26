import pandas as pd
df = pd.read_csv('e-commerce-data-origin.csv', encoding='ISO-8859-1', engine='python')

# Description(Name of the product)
# Quantity
# UnitPrice

selected_columns = ['Description', 'Quantity', 'UnitPrice']
df = df[selected_columns]
print(pd.isna(df).sum(), '\n')

df = df.dropna()
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset='Description',inplace=True)

# Rename Description to Name
df.rename(columns={'Description':'Name'}, inplace=True)


# Save the csv file with only Description, Quantity, UnitPrice row
df.to_csv("e-commerce-data.csv", sep=',', index=False)