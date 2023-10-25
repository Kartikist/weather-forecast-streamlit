import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next 5 Days")

place = st.text_input("Enter place: ")

days = st.slider("Forecast Days", min_value=0, max_value=5, help="Select number of forecasted days")

option = st.selectbox("Select data to view:", ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}")



data = get_data(place,days,kind)  

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temp (C)"} )
st.plotly_chart(figure)