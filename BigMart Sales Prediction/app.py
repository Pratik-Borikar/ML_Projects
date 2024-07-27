import streamlit as st
import numpy as np
import datetime as dt
import joblib

current_year = dt.datetime.today().year

def predict_sales(Item_MRP, Outlet_Identifier, Outlet_Size, Outlet_Type, Outlet_Establishment_Year):
    try:
        outlet_identifier_mapping = {
            "OUT010": 0, "OUT013": 1, "OUT017": 2, "OUT018": 3, 
            "OUT019": 4, "OUT027": 5, "OUT035": 6, "OUT045": 7, 
            "OUT046": 8, "OUT049": 9
        }
        p2 = outlet_identifier_mapping[Outlet_Identifier]
        
        outlet_size_mapping = {"High": 0, "Medium": 1, "Small": 2}
        p3 = outlet_size_mapping[Outlet_Size]
        
        outlet_type_mapping = {
            "Supermarket Type1": 1, "Supermarket Type2": 2, 
            "Supermarket Type3": 3, "Grocery Store": 0
        }
        p4 = outlet_type_mapping[Outlet_Type]
        
        p5 = current_year - Outlet_Establishment_Year
        
        model = joblib.load('bigmart_model')
        result = model.predict(np.array([[Item_MRP, p2, p3, p4, p5]]))
        
        return float(result) - 714.42, float(result) + 714.42
    except Exception as e:
        return str(e), str(e)

st.title("Big Mart Sales Prediction System")

st.write("""
### Enter the details to predict the sales amount
""")

Item_MRP = st.text_input("Item MRP")
Outlet_Identifier = st.selectbox("Outlet Identifier", ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027',
                                                        'OUT035', 'OUT045', 'OUT046', 'OUT049'])
Outlet_Size = st.selectbox("Outlet Size", ['High', 'Medium', 'Small'])
Outlet_Type = st.selectbox("Outlet Type", ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])
Outlet_Establishment_Year = st.text_input("Outlet Establishment Year")

if st.button('Predict'):
    try:
        Item_MRP = float(Item_MRP)
        Outlet_Establishment_Year = int(Outlet_Establishment_Year)
        lower_bound, upper_bound = predict_sales(Item_MRP, Outlet_Identifier, Outlet_Size, Outlet_Type, Outlet_Establishment_Year)
        st.write(f"### Sales Amount is between {lower_bound} and {upper_bound}")
    except ValueError:
        st.write("Please enter valid numerical values for Item MRP and Outlet Establishment Year")
