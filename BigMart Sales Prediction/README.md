# BigMart Sales Prediction

This project aims to predict the sales of products across various stores of BigMart. The prediction is based on key features such as Item MRP, Outlet Identifier, Outlet Size, Outlet Type, and Outlet Establishment Year. We used the XGBRFRegressor model to achieve accurate predictions. Additionally, a GUI was developed using Streamlit to allow users to input details and receive sales predictions.

## Introduction

BigMart is a retail chain that operates a variety of stores selling different product categories. Accurate sales predictions help in better inventory management, resource allocation, and decision-making. This project provides a solution for predicting sales using historical data and machine learning.

## Features
**Item MRP:** The maximum retail price of the item.  
**Outlet Identifier:** A unique identifier for the outlet/store.  
**Outlet Size:** The size of the outlet, such as Small, Medium, or Large.  
**Outlet Type:** The type of the outlet, such as Supermarket Type1, Type2, etc.  
**Outlet Establishment Year:** The year the outlet was established.  

## Model
We used the XGBRFRegressor model, a variant of XGBoost that incorporates a Random Forest approach. This model was chosen for its ability to handle non-linear relationships and interactions between features.

## GUI Development
The graphical user interface (GUI) was developed using Streamlit. The GUI allows users to input the necessary details about the item and the outlet to predict the sales amount. The user-friendly interface makes it easy for users to interact with the model and get quick predictions.

![Capture2](https://github.com/user-attachments/assets/c2c5505e-eac4-404e-aaad-d49e87671f3f)

![Capture1](https://github.com/user-attachments/assets/b3294e97-4050-434e-8d6f-d17a0caf00e4)

## Usage
1. **Download Files:** Download all the project files to your local machine.

2. **Run Application:** Navigate to the project directory and run the app.py file or directly run "streamlit run app.py" in the cmd of the same folder.

## Results
The model provides accurate sales predictions with a high degree of confidence. The Streamlit app displays the predicted range of sales amount in a user-friendly format.
