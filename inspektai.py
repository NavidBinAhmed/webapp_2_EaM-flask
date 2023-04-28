import streamlit as st
import pandas as pd
import numpy as np
import plost
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu

# inspection and our data points tutorial
# https://www.youtube.com/watch?v=VZ_tS4F6P2A

# Page header setting
st.set_page_config(page_title="InspektAI , Making Built World Safer!", page_icon=":Gear:", layout="wide")

# Subheader
#st.header("InspektAI") 
#st.write("Advanced building inspection using AI and drone technologies. [Click](https://inspektai.com) to learn more")


# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
# stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
stocks = pd.read_csv('https://raw.githubusercontent.com/NavidBinAhmed/data/main/data_building.csv')
# building data
#building = pd.read_csv('https://raw.githubusercontent.com/RWTH-EBC/BUDO/master/Database/BUDO_vocabulary.csv')     
df = px.data.gapminder()

#----navigation bar----
# https://icons.getbootstrap.com/
#with st.sidebar:
selected = option_menu(
        menu_title="",
        options=["Self Inspection", "Dashboard", "Contact"],
        icons=["search", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )    

#----top image----
#with st.container():
#    st.image(Image.open(''))
#    st.write("##")

#----title----
with st.container():
    #st.write("---")
    st.write("##")
    st.subheader("Make a Self Inspection of Your Property")
    st.write("Provide your building information to inspect tentative status from our existing database")
    st.write("##")

#data showcasing and graph
#st.write(df)
option_year = df['year'].unique().tolist()
year = st.selectbox('Select the age of your building: ', option_year, 0)
df = df[df['year']==year]

option_material = df['iso_alpha'].unique().tolist()
material = st.selectbox('Select the material of your building: ', option_material, 1)
df = df[df['iso_alpha']==material]

option_country = df['country'].unique().tolist()
country = st.selectbox('Select the country of your building: ', option_country, 0)
df = df[df['country']==country]


fig = px.scatter(df, x="year", y="lifeExp",
                 size="pop", 
                 color="continent", hover_name="continent",
                 log_x=True, size_max=55, 
                 range_x=[100,100000], range_y=[25,90])
fig.update_layout(width=800)
st.write(fig)

#video
with open('video.html', 'r') as f:
    html_string = f.read()

#---- Dashboard----
with st.container():
    #st.write("---")
    st.write("##")
    st.subheader("Dashboard Analytics")
    st.write("##")
    
# Row A
a1, a2 = st.columns(2)
a1.image(Image.open('Logoname.png'))
a2.metric("Welcome, Navid!", "XYZ Building", "33, Soi 62, Sukhumbhit, BKK")

# Row B
b1, b2, b3 = st.columns(3)
b1.metric(" ", "Building Information")
b2.metric(" ", "Inspekt AI Analytics", "No Cracks Found")
b3.image(Image.open('building.jpg'))

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Pie chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')

# ---- contact form ---- 
with st.container():
    #st.write("---")
    st.subheader("Get in Touch")
    st.write("our team will follow-up with you")
    

    contact_form = """
    <form action="https://formsubmit.co/navid@inspektai.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="Client's name" placeholder = "Your name" required>
     <input type="email" name="Client's email" placeholder = "Your email" required>
     <input type="text" name="Building materials" placeholder="Building materials, i.e. bricks, stones" required>
     <input type="text" name="Building purpose" placeholder="Building purpose, i.e. office, residential" required>
     <input type="text" name="Building height" placeholder="Building height in ft" required>
     <input type="text" name="Number of units" placeholder="Number of units" required>
     <input type="text" name="Client's location" placeholder="Your location" required>
     <textarea name="Message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    st.write("##")


# Styling
with open('style_st.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}/style>",unsafe_allow_html=True)
local_css("formstyle.css")

st.write("copyright@freebuildinginspection 2023")
st.write("Powered by: InspectAI")