import plotly.express as px
import pandas as pd

# Sample Data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 180, 150, 220, 300]
}

df = pd.DataFrame(data)

# Create Line Chart
fig = px.line(
    df,
    x="Month",
    y="Sales",
    title="Monthly Sales Report"
)

fig.show()