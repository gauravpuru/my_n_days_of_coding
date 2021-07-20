# This code file contains the code for Advance Data visualization using Seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style = 'ticks')
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips,row='smoker', col='time', margin_titles=True)
g.map(sns.regplot,'size','total_bill',color='0.3',fit_reg=False, x_jitter=0.1)
g.add_legend()
plt.show()
