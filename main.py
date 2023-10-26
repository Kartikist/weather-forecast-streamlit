import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next 5 Days")

place = st.text_input("Enter place: ")

days = st.slider("Forecast Days", min_value=0, max_value=5, help="Select number of forecasted days")

option = st.selectbox("Select data to view:", ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place,days) 
        

        if option == "Temperature":
            temperatures = [temp["main"]["temp"]/10 for temp in filtered_data]
            dates = [temp["dt_txt"] for temp in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temp (C)"} )
            st.plotly_chart(figure)
            
        if option == "Sky":
            image = {"Clear": "images/clear.png","Clouds": "images/cloud.png","Rain": "images/rain.png","Snow": "images/snow.png"}
            sky_condition = [temp["weather"][0]["main"] for temp in filtered_data]
            image_paths = [image[condition] for condition in sky_condition]
            st.image(image_paths, width=115)
            
    except:
        st.subheader(f"{place} does not exist.")
