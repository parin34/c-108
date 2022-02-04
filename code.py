import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff


df = pd.read_csv('data.csv')

fd = ff.create_distplot([df["Avg Rating"].tolist()],["the avrage rating"])

fd.show()
