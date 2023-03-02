#Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# import dataset of plotly (plotly has it own dataset) 

st.title('Combination of Plotly and Streamlit' )
df =px.data.gapminder()
st.write(df)

 # st.write(df.head())
st.write(df.columns )

# Summary stats
st.write(df.describe())
# Data mangement through plotly

year_option = df['year'].unique().tolist()
year = st.selectbox('Which year should we plot?', year_option, 0)
# df =df[df['year'] == year]
# plotting

fig =px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color ='continent', hover_name='continent', 
                log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90], animation_frame='year', animation_group='country')
fig.update_layout( width= 1000, height= 500) 
st.write(fig)


