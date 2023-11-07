#!/usr/bin/env python
# coding: utf-8

# In[10]:


import plotly.express as px


# Creating the Figure instance
fig = px.line(x=[1, 2], y=[3, 4])

# printing the figure instance
print(fig)

fig.show()


# In[2]:


# using the iris dataset
df = px.data.iris()
 
# plotting the line chart
fig = px.line(df, y="sepal_width",)
 
# showing the plot
fig.show()


# In[3]:


# using the iris dataset
df = px.data.iris()
 
# plotting the line chart
fig = px.line(df, y="sepal_width", line_dash='species',
              color='species')
 
# showing the plot
fig.show()


# In[ ]:





# In[6]:


# Loading the data
df = px.data.tips()
 
# Creating the bar chart
fig = px.bar(df, x='day', y="total_bill", color='sex',
             facet_row='time', facet_col='sex')
 
fig.show()


# In[7]:


# using the dataset
df1 = px.data.tips()
 
# plotting the scatter chart
fig = px.scatter(df1, x='total_bill', y="tip", color='time',
                 symbol='sex', size='size', facet_row='day',
                 facet_col='time')
 
# showing the plot
fig.show()


# In[8]:


# using the dataset
df = px.data.tips()
 
# plotting the histogram
fig = px.histogram(df, x="total_bill", color='sex',
                   nbins=50, histnorm='percent',
                   barmode='overlay')
 
# showing the plot
fig.show()


# In[9]:


# using the dataset
df = px.data.tips()
 
# plotting the boxplot
fig = px.box(df, x="day", y="tip", color='sex',
             facet_row='time', boxmode='group',
             notched=True)
 
# showing the plot
fig.show()


# In[11]:


# using the dataset
df = px.data.tips()
 
# plotting the violin plot
fig = px.violin(df, x="day", y="tip", color='sex',
                facet_row='time', box=True)
 
# showing the plot
fig.show()


# In[12]:


# data to be plotted
df = px.data.tips()
 
# plotting the figure
fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip", color='day', 
                    size='total_bill', symbol='time')
 
fig.show()


# In[22]:


import plotly.graph_objects as px
import numpy as np
import pandas as pd
 
df = pd.read_csv('C:/Users/siddh/Downloads/archive (2)/tips.csv')
 
plot = px.Figure(data=[px.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])
 
# Add dropdown
plot.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(
                args=["type", "scatter"],
                label="Scatter Plot",
                method="restyle"
            ),
            dict(
                args=["type", "bar"],
                label="Bar Chart",
                method="restyle"
            )
        ]),
            direction="down",
        ),
    ]
)
 
plot.show()


# In[23]:


import plotly.graph_objects as px
import plotly.express as go
import numpy as np
 
df = go.data.tips()
 
x = df['total_bill']
y = df['tip']
 
plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='markers',)
])
 
plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
 
plot.show()


# In[ ]:





# In[25]:


pip install chart-studio


# In[27]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot

# Initialize notebook mode for offline plotting
init_notebook_mode(connected=True)

# Sample data: You can replace this with your own dataset
data = pd.DataFrame({
    'State': ['Arizona', 'California', 'New York'],
    'Value': [1.0, 2.0, 3.0]
})

# Create a choropleth map
choropleth_map = go.Figure(data=go.Choropleth(
    locations=['AZ', 'CA', 'NY'],  # Use the state abbreviations
    locationmode='USA-states',
    z=data['Value'],  # Color values based on data
    colorscale='Viridis',  # Choose a different color scale
    text=data['State'],  # Display state names on hover
    colorbar={'title': 'Values'},
))

# Customize layout
layout = go.Layout(
    geo={'scope': 'usa'},
    title='Choropleth Map Example',  # Customize the title
)

choropleth_map.update_layout(layout)

# Plot the graph
iplot(choropleth_map)


# In[ ]:





# In[ ]:





# In[ ]:




