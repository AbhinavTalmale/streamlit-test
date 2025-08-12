import streamlit as st 
import pandas as pd
import pickle
import sklearn 

st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Title styling */
        .app-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #aaa;
            margin-bottom: 2rem;
        }
        /* Card styling */
        .stCard {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            color: white;
        }
        label {
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='app-title'>🚗 Car Price Prediction App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Get an instant estimated price based on your car's details</div>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center;'>Car Price Prediction App</h1>", unsafe_allow_html=True)

df = pd.read_csv('cars24-car-price.csv')

# Load model
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

# CSS for card styling
st.markdown("""
    <style>
        .stCard {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            color: white;
        }
        .stSlider > div[data-baseweb="slider"] {
            padding-top: 8px;
        }
        label {
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

# Layout: image on left, big form on right
col1, col_form = st.columns([0.8, 1.8])

with col1:
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2OvX5pIl9OPNEU5s5r3_Y_Xeyw3AledOWUQ&s",
        caption="Experts at Work",
        use_container_width=True
    )

with col_form:
    with st.container():
        st.markdown("<div class='stCard'>", unsafe_allow_html=True)
        st.subheader("Enter Car Details")

        # Row 1
        r1c1, r1c2, r1c3 = st.columns(3)
        with r1c1:
            year = st.selectbox("Year", options=range(2025, 1990, -1), index=0)
        with r1c2:
            seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
        with r1c3:
            km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000, step=1000)

        # Row 2
        r2c1, r2c2, r2c3 = st.columns(3)
        with r2c1:
            fuel_type = st.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
        with r2c2:
            transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])
        with r2c3:
            mileage = st.slider("Mileage (km/l)", 0.0, 50.0, 20.0)

        # Row 3
        r3c1, r3c2, r3c3 = st.columns(3)
        with r3c1:
            engine_cc = st.slider("Engine (CC)", 500, 5000, 100)
        with r3c2:
            max_power = st.slider("Max Power (bhp)", 0.0, 500.0, 100.0)
        with r3c3:
            seats = st.selectbox("Seats", [2, 4, 5, 7, 8, 9, 10, 12, 15, 16, 20])

        encode_dict = {
            'fuel_type': {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
            'seller_type': {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
            'transmission_type': {'Manual': 1, 'Automatic': 2}
        }

        if st.button("Get Price", use_container_width=True):
            encoded_fuel_type = encode_dict['fuel_type'][fuel_type] 
            encoded_seller_type = encode_dict['seller_type'][seller_type]
            encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
            
            input_data = [[year, encoded_seller_type, km_driven, encoded_fuel_type, encoded_transmission_type, mileage, engine_cc, max_power, seats]]
            price = model.predict(input_data)
            st.success(f"Predicted Price : {price[0]:,.2f}L INR")

        st.markdown("</div>", unsafe_allow_html=True)

