import pandas as pd
from scipy.stats import shapiro

data = pd.read_csv("D:/desktop/Ethereum_compiled_data.csv", low_memory=False)

returns = data['Low']

stat, p = shapiro(returns)

print('Statistics=%.3f, p=%.3f' % (stat, p))

