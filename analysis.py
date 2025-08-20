# Author: 23f1000267@ds.study.iitm.ac.in
# Marimo notebook demonstrating variable relationships with interactive widgets.
# Data flow:
#   Cell 1 -> defines sliders (a, noise, n) and a UI stack
#   Cell 2 -> generates x, y using (a, noise, n)  [depends on Cell 1]
#   Cell 3 -> builds DataFrame and computes correlation corr  [depends on Cell 2]
#   Cell 4 -> dynamic markdown reflecting corr and showing sliders UI  [depends on Cells 1 & 3]
#   Cell 5 -> plot and interactive dataframe of the simulated data  [depends on Cell 3]
#
# Run with:  marimo run analysis.py

import marimo as mo

app = mo.App()

# --- Cell 1: Widgets (sources) ---
@app.cell
def _(mo):
    # Sliders control the simulated relationship
    a = mo.ui.slider(0, 10, 1, value=3, label="Slope a")
    noise = mo.ui.slider(0.0, 5.0, 0.1, value=1.0, label="Noise std dev")
    n = mo.ui.slider(50, 1000, 50, value=200, label="Sample size (n)")

    # Combine controls for convenient display
    controls = mo.vstack([a, noise, n], gap=8)

    return a, noise, n, controls

# --- Cell 2: Generate data (depends on sliders) ---
@app.cell
def _(np, a, noise, n):
    # Uses slider values from Cell 1 to simulate data
    rng = np.random.default_rng(42)
    x = rng.normal(0, 1, n.value)
    y = a.value * x + rng.normal(0, noise.value, n.value)
    return x, y

# --- Cell 3: Assemble DataFrame and compute correlation ---
@app.cell
def _(pd, x, y):
    # Downstream consumers (markdown, plot, table) depend on df and corr
    df = pd.DataFrame({"x": x, "y": y})
    corr = df.corr(numeric_only=True).loc["x", "y"]
    return df, corr

# --- Cell 4: Dynamic markdown based on widget state ---
@app.cell
def _(mo, controls, a, noise, n, corr):
    mo.md(f"""
# Interactive Relationship Explorer

**Live settings**
- Slope **a**: `{a.value}`  
- Noise **σ**: `{noise.value:.2f}`  
- Sample size **n**: `{n.value}`  

**Current Pearson correlation** between `x` and `y`: **{corr:.3f}**

> Increase **a** to strengthen the linear relationship. Increase **noise** to weaken it.
""")
    # Show controls alongside the markdown
    controls
    return

# --- Cell 5: Visualization and interactive table ---
@app.cell
def _(mo, plt, df):
    # Scatter plot to visualize the relationship
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Scatter of y vs x")

    # Show the figure
    mo.mpl.figure(fig)

    # Interactive table (filter/sort in UI)
    mo.ui.dataframe(df)
    return

# --- Imports (provided as separate cells so they can be cached) ---
@app.cell
def _():
    import numpy as np
    return np,

@app.cell
def _():
    import pandas as pd
    return pd,

@app.cell
def _():
    import matplotlib.pyplot as plt
    return plt,

if __name__ == "__main__":
    app.run()
