from bokeh.plotting import figure
from bokeh.models import HoverTool

def create_scatter_plot(df):
    """
    Creates an interactive Bokeh scatter plot using t-SNE coordinates.
    """
    hover = HoverTool(tooltips=[
        ("Product", "@product"),
        ("Brand", "@brand"),
        ("Price", "@price"),
        ("Ingredients", "@ingredients")
    ])

    p = figure(title="Cosmetic Product Similarity (t-SNE)",
               tools=[hover, "pan", "wheel_zoom", "reset"])

    p.circle("x", "y", source=df, size=8, alpha=0.6)
    return p
