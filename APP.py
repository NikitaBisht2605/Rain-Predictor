import pandas as pd
import streamlit as st
import pickle
import numpy as np

#pickle_in=open("A9.pkl","rb")
#reg1=pickle.load(pickle_in)

pickle_in=open("A10.pkl","rb")
reg3=pickle.load(pickle_in)


def predict_rain(MinTemp,MaxTemp,Rainfall,
       WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Temp9am,
                            Temp3pm,RainToday):
    if RainToday=='No':
        RainToday=0
    elif RainToday=='Yes':
        RainToday=1
    prediction=reg3.predict([[MinTemp,MaxTemp,Rainfall,
       WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Temp9am,
                            Temp3pm,RainToday]])
    print(prediction)
    return prediction
    
def main():
    st.title("Rainfall Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Rainfall Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MinTemp=st.text_input("Minimum Temperature","Type Here")
    MaxTemp=st.text_input("Maximum Temperature","Type Here")
    Rainfall=st.text_input("Rainfall","Type Here")
    WindSpeed9am=st.text_input("Wind Speed at 9 AM","Type Here")
    WindSpeed3pm=st.text_input("Wind Speed at 3 PM","Type Here")
    Humidity9am=st.text_input("Humidity at 9 AM","Type Here")
    Humidity3pm=st.text_input("Humidity at 3 PM","Type Here")
    Temp9am=st.text_input("Temperature at 9 AM","Type Here")
    Temp3pm=st.text_input("Temperature at 3 PM","Type Here")
    RainToday=st.text_input("Did it rain today?","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_rain(MinTemp,MaxTemp,Rainfall,
       WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Temp9am,
                            Temp3pm,RainToday)
    if result[0]==0:
        st.write("There won't be any rain tomorrow")
    else:
        st.write("There will be rain tomorrow")
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()

