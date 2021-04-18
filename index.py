%matplotlib notebook
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader
%matplotlib inline
from pylab import rcParams
rcParams['figure.figsize'] = 20,10

bank = ["MFG","PYPL"]
banks = web.DataReader(bank,'yahoo')
price = banks["Adj Close"]
price.plot(title='mizuho vs. PYPL', grid=True)
plt.show()
