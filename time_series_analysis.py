
# NOTE: To run this file, you'll need to have statsmodels and related libraries installed.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Generating a simple time series with trend and seasonality
time = np.arange(100)
time_series = 5 * time + 10 * np.sin(0.1 * time) + np.random.normal(size=100)

plt.plot(time, time_series)
plt.title("Generated Time Series")
plt.show()

# ARIMA model
model = ARIMA(time_series, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# Forecast
forecast = model_fit.forecast(steps=10)
print(f"10-step forecast: {forecast}")
