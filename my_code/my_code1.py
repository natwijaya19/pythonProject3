import numpy as np
import matplotlib.pyplot as plt

# Create daily stock return using random integer numpy
low = -30
high = 36
num_days = 1000
num_symbols = 20
np_size = (num_days, num_symbols)
daily_return = np.random.randint(low, high, np_size) / 1000

# Calculate cumulative return of the daily return using numpy
cumulative_return = (1 + daily_return).cumprod(axis=0)

# plot the cumulative return by using matplotlib.pyplot
plt.plot(cumulative_return)
plt.show()

#%%============================================================================
# plot the cumulative return by using pandas
import pandas as pd
df = pd.DataFrame(cumulative_return)
df.plot()
plt.show()

#%%============================================================================
# plot the cumulative return by using seaborn
import seaborn as sns
sns.set()
df.plot()
plt.show()

#%%============================================================================
# plot the cumulative return by using plotly
import plotly.graph_objects as go
fig = go.Figure()
for i in range(num_symbols):
    fig.add_trace(go.Scatter(x=df.index, y=df[i], name=f"Symbol{i}"))
fig.show()

#%%============================================================================
# plot by using smilogy scale of matplotlib.pyplot
plt.semilogy(cumulative_return)
plt.show()
