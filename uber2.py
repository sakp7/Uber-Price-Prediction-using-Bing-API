
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import time
from PIL import Image

# Add a marker to the map
# img=Image.open("h11.jpg")
base_go=28.25
base_bike=11
base_auto=20
base_pre=42
cost_go=12
cost_pre=15
cost_auto=11
cost_bike=5.5

Go_pic=Image.open("Ubergo.jpg")
Pre_pic=Image.open("UberPre.jpg")
Auto_pic=Image.open("Uberauto.jpg")
Bike_pic=Image.open("Uberbike.jpg")
with st.sidebar:
    selec=option_menu(
        menu_title="UBER",
        options=["Home","Price Breakdown"]
        )
    

if selec=="Home":
    b1,b2,b3=st.columns([1,2,3])
    a = st.empty()
    b=st.empty()
    c=st.empty()
    d=st.empty()
    a.header("Uber Price Prediction")
    start_address = b.text_input('start address')
    end_address = c.text_input('end address')

    if d.button("Submit"):
            
        url = 'https://assets6.lottiefiles.com/packages/lf20_fsyj0fzz.json'
        res = requests.get(url)
        animation = res.json()

        def long_running_task():
            with st.empty():
                st_lottie(animation, speed=1, width=500, height=500)
                time.sleep(5)
                st.write("")
        long_running_task()

        api_key = 'AuwFaMj_sB7D0goFmqRO0boq4SqvbdtnxwTlzmGqQF0pUff98KRF1w8njPi4OPNv'
        url = f'http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0={start_address}&wp.1={end_address}&key={api_key}'
        response = requests.get(url)
        data = response.json()
        try:
            
            route = data['resourceSets'][0]['resources'][0]
            distance = route['travelDistance']
            duration = route['travelDuration']
            duration/=60
            traffic=route['trafficCongestion']
            if traffic=='Medium':
                surge=1.3
            elif traffic=='Mild':
                surge=1.41
            elif traffic=='None':
                surge=1.2
            elif traffic=='High':
                surge=1.7
            else:
                surge=1.5
                
            base_go=28.25
            base_bike=11
            base_auto=20
            base_pre=42
            time=duration/60
            fare_pre=  (base_pre  +time*1.58  +15*distance)*surge-20
            fare_go=   (base_go   +time*1.6   +12*distance)*surge-20
            fare_auto= (base_auto +time*1.2   +11*distance)*surge
            fare_bike= (base_bike +time*1     +5.5*distance)*surge
            

            
            a.empty()
            b.empty()
            c.empty()
            d.empty()




            
            
            
            y1,y2,y3=st.columns(3)
            y1.text("Pickup")
            y1.write(start_address.upper())
            y2.caption("TO")
            y3.text("Drop")
            y3.write(end_address.upper())
            st.write("")
            st.write("")
            x1,x2,x3=st.columns(3)
            x1.metric(label="Distance",value=distance)
            x2.metric(label="Duration",value=round(duration,2))
            x3.metric(label="Traffic",value=traffic)
            
           
            
            st.write(" ")




            st.write(" ")
            st.write(" ")
            
            col1, col2 = st.columns(2)
            with col1:
                st.text("Auto")
            with col2:
                st.text("Bike")
            with col1:
                st.image(Auto_pic, width=80)
            with col2:
                st.image(Bike_pic, width=80)
            with col1:
                st.text(round(fare_auto, 2))
            with col2:
                st.text(round(fare_bike, 2))
            with col1:
                
                are_auto = ((base_auto + time * 1.2 + 11 * distance) * surge) + 8


     #  with col1:
    #       if st.button('↓'):
   #      with col2:
 #           if st.button('↓ '):
#                st.write("Bike")

            st.text("")
            st.text("")
            st.text("")
            col1, col2 = st.columns(2)
            with col1:
                st.text("Uber Go")
            with col2:
                st.text("Uber Premium")
            with col1:
                st.image(Go_pic, width=190)
            with col2:
                st.image(Pre_pic, width=190)
            with col1:
                st.text(round(fare_go, 2))
            with col2:
                st.text(round(fare_pre, 2))

        except Exception as e:
            st.error("Enter the details Accurately")
            
        
    





if selec=="Price Breakdown":
    
    c1,c2,c3=st.columns([1,2,1])  
    c2.header("Uber Price Breakdown")
    st.subheader("Uber Go:")
    st.text("Base Price: {} Rs".format(base_go))
    st.text("Cost per kilometer:{} Rs".format(cost_go))
    st.text("Cost per minute:{} Rs".format(1.6))
    st.subheader("Uber Premiure:")
    st.text("Base Price: {} Rs".format(base_pre))
    st.text("Cost per kilometer:{} Rs".format(cost_pre))
    st.text("Cost per minute:{} Rs".format(1.58))
    
    st.subheader("Uber Auto:")
    st.text("Base Price: {} Rs".format(base_auto))
    st.text("Cost per kilometer:{} Rs".format(cost_auto))
    st.text("Cost per minute:{} Rs".format(1.2))
    
    st.subheader("Uber Bike:")
    st.text("Base Price: {} Rs".format(base_bike))
    st.text("Cost per kilometer:{} Rs".format(cost_bike))
    st.text("Cost per minute:{} Rs".format(1))
    
 


