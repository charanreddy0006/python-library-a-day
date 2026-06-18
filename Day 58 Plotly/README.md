# Day 58 - Plotly Library

# 📌 Overview

On Day 58, I explored Python's powerful **Plotly library**, which is used for creating interactive and professional data visualizations.

Unlike Matplotlib, Plotly charts are interactive.

Users can:

- Zoom
- Pan
- Hover
- Explore Data
- Download Charts

Plotly is widely used in:

- Data Science
- Data Analytics
- Business Intelligence
- Machine Learning
- Dashboard Development

---

# 📦 Installation

Install Plotly:

```bash
pip install plotly
```

---

# 🧠 Importing Plotly

```python
import plotly.express as px
```

Plotly Express is the easiest way to create charts.

---

# 📊 What is Data Visualization?

Data Visualization is the process of representing data graphically.

Examples:

- Line Charts
- Bar Charts
- Pie Charts
- Scatter Plots

Visualization helps users understand trends and patterns.

---

# 🚀 Creating a Line Chart

Example:

```python
fig = px.line(
    df,
    x="Month",
    y="Sales"
)
```

This creates a line graph.

---

# 📊 Creating a Bar Chart

Example:

```python
fig = px.bar(
    df,
    x="Month",
    y="Sales"
)
```

Used for comparisons.

---

# 🥧 Creating a Pie Chart

Example:

```python
fig = px.pie(
    df,
    names="Month",
    values="Sales"
)
```

Displays percentage distribution.

---

# 🔵 Creating a Scatter Plot

Example:

```python
fig = px.scatter(
    df,
    x="Month",
    y="Sales"
)
```

Used to identify patterns.

---

# 👆 Interactive Features

Plotly charts support:

- Hover Information
- Zooming
- Panning
- Download as Image
- Dynamic Exploration

These features make Plotly powerful for dashboards.

---

# 💻 Complete Example

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [100, 200, 300]
})

fig = px.bar(
    df,
    x="Month",
    y="Sales"
)

fig.show()
```

---

# 🚀 Real-World Uses

## Business Dashboards

Display company reports.

---

## Data Analytics

Analyze trends and patterns.

---

## Machine Learning

Visualize model results.

---

## Financial Reports

Track revenue and expenses.

---

## Data Science Projects

Present findings visually.

---

# ⚡ Advantages of Plotly

- Interactive charts
- Professional appearance
- Easy to learn
- Dashboard friendly
- Works with Pandas

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What data visualization is
- How Plotly creates charts
- How interactive graphs work
- How dashboards display information
- How business reports are visualized

---

# 🚀 Conclusion

The Plotly library is one of the most powerful visualization libraries in Python.

It helps developers:

- Create interactive charts
- Build dashboards
- Analyze data visually
- Present information professionally

Learning Plotly is useful for:

- Data Science
- Data Analytics
- Machine Learning
- Business Intelligence
- Dashboard Development

It is an essential library for anyone working with data.