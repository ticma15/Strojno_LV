import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

print(len(mtcars))
print(mtcars)
print(mtcars.head(5))
print(mtcars.tail(3))
print(mtcars.info())
print(mtcars.describe())

print(mtcars['car'])
print(mtcars.cyl)
print(mtcars.cyl > 6)
print(mtcars[mtcars.cyl > 6])
print(mtcars[(mtcars.cyl == 4) & (mtcars.hp > 100)].car)
print(mtcars[['car','cyl']])
print(mtcars.cyl[2:4])
print(mtcars[5:12])
print(mtcars.mpg[3:5])
mtcars['jedinice'] = np.ones(len(mtcars))
mtcars['heavy'] = mtcars.wt > 4.5
print(mtcars[['car','heavy']])
print(mtcars.query('cyl == [4,6]').car)
print(mtcars.iloc[1:3, 5:10])
print(mtcars.iloc[:, 3:5])
print(mtcars.iloc[:, [0,4,7]])
print(mtcars.iloc[[1,29], :])