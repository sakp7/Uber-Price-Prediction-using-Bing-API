# Uber-Price-Prediction-using-Binge-Maps-API
### Uber Price Prediction Project

#### Project Description

This project aims to create a web application using Streamlit that predicts the costs of using Uber services for different modes of transportation (Uber Go, Uber Premium, Uber Auto, and Uber Bike) based on the distance and duration of the trip. The application uses the Microsoft Virtual Earth API to retrieve the distance and travel time between the start and end addresses, and then calculates the fare based on the base prices, cost per kilometer, and cost per minute for each mode of transportation.

#### Required Libraries

* Streamlit (streamlit as st)
* Streamlit-Option-Menu (from streamlit_option_menu import option_menu)
* Requests (requests)
* Streamlit-Lottie (from streamlit_lottie import st_lottie)
* Streamlit-Extras (from streamlit_extras.colored_header import colored_header)
* Pillow (from PIL import Image)

#### Steps to Run

1. Install the required libraries by running `pip install streamlit streamlit-option-menu requests streamlit-lottie streamlit-extras pillow`.
2. Run the script using `streamlit run script.py`.
3. Go to the Streamlit app in your web browser and click on the sidebar menu to select either "Home" or "Price Breakdown".
4. If you select "Home", enter the start and end addresses and click the "Submit" button to retrieve the distance and travel time.
5. The app will display the predicted cost for each mode of transportation based on the distance and travel time.

#### Detailed Explanation

The script uses the Streamlit library to create a web application with a sidebar menu that allows users to select either "Home" or "Price Breakdown". If the user selects "Home", the app will display a form to enter the start and end addresses. When the user clicks the "Submit" button, the app will retrieve the distance and travel time using the Microsoft Virtual Earth API, and then calculate the predicted cost for each mode of transportation using the base prices, cost per kilometer, and cost per minute.

The app also uses the Streamlit-Lottie library to display a loading animation while the data is being retrieved. If the user selects "Price Breakdown", the app will display a breakdown of the costs for each mode of transportation, including the base price, cost per kilometer, and cost per minute.****
