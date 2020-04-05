import pandas as pd
import re

def doPrint(data, action=""):
    print(f"::{action}:::::::::::::::::::::::::")
    print(data)
    print(f"----------------------------------")
    print("")

poke:pd.DataFrame = pd.read_csv('pokemon_data.csv')
for index, row in poke.iterrows():
    pass#print(index, row['Name'])
doPrint(poke.head(5))

#-- Filter by any column's data
filteredPoke = poke.loc[poke['Type 1'] == "Fire"]
doPrint(filteredPoke.head(5), "Filter Data")

#-- Sort Values
sorted_poke = poke.sort_values('Name', ascending=True)
doPrint(sorted_poke.head(5), "Sorting Columns")

#-- Add a new column, "Total" to the DataFrame, using values already in the DataFrame
poke["Total"] = poke["HP"] + poke["Attack"] + poke["Defense"] + poke["Sp. Atk"] + poke["Sp. Def"] +  poke["Speed"]
doPrint(poke.head(5), "Add Column")

#-- Drop column
#poke = poke.drop(columns=["Total"])

#-- Add column, Method-2
poke["Total"] = poke.iloc[:, 4:10].sum(axis=1)
doPrint(poke.head(5), "Add Column, Method-2")

#--Set Multiple Column's data
copyPoke = poke.copy(deep=True)
poke.loc[poke['Total'] > 500, ['Generation', 'Legendary']] = ["-NEW GNERATION-", "-NEW LEGENDARY-"]
doPrint(poke.head(5), "Set multiple column's data")
poke = copyPoke.copy(deep=True)

#-- Rearrange columns
cols = list(poke.columns.values)
poke = poke[cols[0:4] + [cols[-1]] + cols[4:12]] #Surround cols[-1] with [] because it's just a str (one column)
doPrint(poke.head(5), "Rearrange Columns")

#-- More Filtering and Conditions
poke: pd.DataFrame = pd.read_csv('pokemon_data.csv')
filteredPoke = poke.loc[(poke["Type 1"] == "Grass") & (
    poke["Speed"] > 50)]  # Each term within parens
filteredPoke = poke.reset_index(drop=True)
doPrint(filteredPoke.head(5), "Filtering, Conditions and Re-Index")

#-- Remove Names without 'Mega' in name
noMega = poke.loc[~poke['Name'].str.contains('Mega')] #Squiggly line indicates "Not"
doPrint(noMega.head(5), "Don't show Pokemon with <Mega>")

#-- Remove based on RegEx, Ingnoring Case
FireAndGrass = poke.loc[poke['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]  # Squiggly line indicates "Not"
doPrint(FireAndGrass.head(5), "Only show Pokemon Fire and Grass in 'Type 1'")


#-- Show Pokemon with names starting with "Pi"
PiPoke = poke.loc[poke['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]  # Squiggly line indicates "Not"
doPrint(PiPoke.head(5), "Only show Pokemon with names starting with 'Pi'")

#-- Use condition to set a column's data
poke.loc[poke['Type 1'] == "Fire", "Type 1"] = 'Flamer'
doPrint(poke.head(5), "Use condition to set a column's data")
poke.loc[poke['Type 1'] == "Flamer", "Type 1"] = 'Fire'  #Reset us back

#Group By Functionality
#doPrint(poke.groupby(['Type 1']).mean().head(5), "Group By")
doPrint(poke.groupby(['Type 1']).mean().sort_values('HP', ascending=False).head(5), "Group By")

#GroupBy Count
poke['count'] = 1 #'First add a temp column, and set it to a value'
doPrint(poke.groupby(['Type 1', 'Type 2']).count()['count'], "Group By")
#doPrint(poke.groupby(['Type 1']).count(), "Group By")

#Read DataFrame in chuncks
new_df = pd.DataFrame(columns = poke.columns)
count =0
for poke in pd.read_csv('pokemon_data.csv', chunksize=100):
    count += 1
doPrint(count, "Read dataset in chuncks")


#-- Save to csv,tsv and excel files
poke.to_csv('updated_pokemon_data.csv', index=False)
poke.to_csv('updated_pokemon_data.tsv', index=False, sep="\t")
poke.to_excel('updated_pokemon_data.xlsx', index=False)
