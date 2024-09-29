import streamlit as st
import plotly.express as px
from backend import get_data

 # Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
if days == 1:
    day = "day"
else:
    day = "days"

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {day} in {place}")

if place:
     # Get the temperature / sky data
    filtered_data = get_data(place, days)
    if filtered_data == "none":
         st.write("Error. Please enter a city name.")

    elif option == "Temperature":
        # Filter the data
        temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data] # List comprehension
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    elif option == "Sky":
        # Filter the data
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                  "Rain":"images/rain.png", "Snow":"images/snow.png"}
        # Translation
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)