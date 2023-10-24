import numpy as np	#导入numpy模块，并创建别名np
import pandas as pd

# 整型变量
year0 = 1990
year1 = 2023


years = list(range(year0, year1)) # years 序列变量

years = np.array(years)	# np.array()

population = years * 1000 + np.random.randint(-100, 100) * 100

# dictionary 映射/字典类型
data = {
	'year': years,
	'population': population
}

pdf = pd.DataFrame(data = data)

pdf.to_csv('张德培-人口.csv', index=False)