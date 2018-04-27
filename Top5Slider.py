import plotly.plotly as py
from ipywidgets import widgets
from plotly.graph_objs import *
from IPython.display import Image, display, clear_output
from plotly.tools import FigureFactory as FF
from plotly.widgets import GraphWidget


g = GraphWidget('https://plot.ly/~jkrejci/10')

display(g)