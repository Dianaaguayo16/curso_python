import plotly.express as px

rw = RandomWalk()
rw.fill_walk()

fig = px.line(x=rw.x_values, y=rw.y_values, title="Plotly Random Walk")
fig.show()
