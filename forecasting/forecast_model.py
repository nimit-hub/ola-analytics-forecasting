import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Load cleaned rides data
file_path = r"C:\Users\Nimit\OneDrive\Desktop\Ola Project\data\rides.csv"
df = pd.read_csv(file_path)

# 2. Convert date
df['booking_date'] = pd.to_datetime(df['booking_date'])

# 3. Monthly aggregation
monthly = (
    df
    .groupby(pd.Grouper(key='booking_date', freq='M'))
    .agg(
        total_rides=('booking_id', 'count'),
        total_revenue=('booking_value', 'sum')
    )
    .reset_index()
)

# 4. Create time index
monthly['t'] = np.arange(len(monthly))

# 5. Train models
X = monthly[['t']]
rides_model = LinearRegression()
revenue_model = LinearRegression()

rides_model.fit(X, monthly['total_rides'])
revenue_model.fit(X, monthly['total_revenue'])

# 6. Forecast next 6 months
future_t = np.arange(len(monthly), len(monthly) + 6).reshape(-1, 1)

forecast = pd.DataFrame({
    'booking_date': pd.date_range(
        start=monthly['booking_date'].max() + pd.offsets.MonthEnd(1),
        periods=6,
        freq='M'
    ),
    'forecast_rides': rides_model.predict(future_t).astype(int),
    'forecast_revenue': revenue_model.predict(future_t)
})

# 7. Save forecast
output_path = r"C:\Users\Nimit\OneDrive\Desktop\Ola Project\forecasting\forecast_output.csv"
forecast.to_csv(output_path, index=False)

print("Forecast generated and saved successfully.")
