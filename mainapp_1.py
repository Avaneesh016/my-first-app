import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client=genai.Client()
st.markdown("""
    <div style="
        text-align: center;
        padding: 25px;
        border-radius: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    ">
        <h1 style="
            color: white;
            font-size: 50px;
            font-weight: 800;
            margin: 0;
            letter-spacing: 2px;
        ">
            ✈️ Travel Assistant 🌍
        </h1>

        <p style="
            color: #f0f0f0;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 0;
        ">
            🌴 Plan • Explore • Discover • Travel ✨
        </p>
    </div>
""", unsafe_allow_html=True)

import streamlit as st
st.title("🌍Travel Assistant")
st.caption("This is a Travel Manager for your travel needs.Lets get going!!!")
location=st.text_input("Enter your destination")
days=st.number_input("Enter number of days you want to travel",min_value=1,max_value=30)
budget=st.selectbox("Select Budget",["Luxury","Moderate","Budgeted"])
Travel_Type=st.radio("Who are you travelling with ",["Family","Freinds","Solo"])
prompt=f"""You are Travel Planner. You are an expert in planning trips and creating itineraries. 
he/she wants to go to{location}for {days}.Plan a trip and write in bullet form.He/She is on a Budget of {budget} and is Travelling type is :{Travel_Type} """
if st.button("Plan My Trip"):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
    )
    with st.spinner("Wait fot it ....",show_time=True):
        time.sleep(5)
    st.success("Voila!!There is your Wonderful Trip")
    st.write(interaction.output_text)
