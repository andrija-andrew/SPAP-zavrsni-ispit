import pandas as pd

# Zadatak 01

dry1 = pd.read_csv('dry-braking-part1.csv')
dry2 = pd.read_csv('dry-braking-part2.csv')
wet1 = pd.read_csv('wet-braking-part1.csv')
wet2 = pd.read_csv('wet-braking-part2.csv')

# Zadatak 02

dry = pd.concat([dry1, dry2], ignore_index=True)
wet = pd.concat([wet1, wet2], ignore_index=True)

# Zadatak 03

try:
    pd.concat([dry1.set_index('tire'), dry2.set_index('tire')], verify_integrity=True)
    print("dry tire concatenation OK")
except ValueError as e_dry:
    print("ValueError:", e_dry)

try:
    pd.concat([wet1.set_index('tire model'), wet2.set_index('tire model')], verify_integrity=True)
    print("wet tire model concatenation OK")
except ValueError as e_wet:
    print("ValueError:", e_wet)

# Zadatak 04

all1 = pd.merge(dry, wet, left_on="tire", right_on="tire model").drop('tire model', axis=1).dropna()

# Zadatak 05

all1['average'] = (all1['dry braking'] + all1['wet braking']) * 0.5
all1['difference'] = 100.0 * abs((all1['wet braking'] - all1['average']) / all1['average'])

# Zadatak 06

all1p = all1.set_index('tire')
average = all1p['average'].sort_values()

# Zadatak 07

mean = all1['average'].mean()

def filter_func(x):
    return x['average'] < mean

all1 = all1.groupby('tire').filter(filter_func)

# Zadatak 08

all2 = pd.merge(dry, wet.dropna(), left_on="tire", right_on="tire model").drop('tire model', axis=1)

# Zadatak 09

print(all2.isnull().any())

#'''
all2['dry braking'] = all2['dry braking'].fillna(all2['wet braking'])
'''
all2.loc[all2[all2['dry braking'].isnull()].index, 'dry braking'] = all2.loc[all2[all2['dry braking'].isnull()].index, 'wet braking']
#'''

# Zadatak 10

all2['average'] = (all2['dry braking'] + all2['wet braking']) * 0.5
