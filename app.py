import streamlit as st
import pandas as pd
import joblib
import pickle

df = pickle.load(open('data.pkl', 'rb'))
best_model = pickle.load(open(r'sales.pkl', 'rb'))

st.markdown("""
<style>
.center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}
</style>
""", unsafe_allow_html=True)


def main():
    st.title('Sales predictor')

    st.header('Fill the details to predict the sales for the products based on certain conditions')
    
    
    Product_Name=st.selectbox('Product Name',df['Product_Name'].unique())
    Discount=st.number_input('Discount on the product')
    Actual_Discount=st.number_input('Actual Discount on the product')
    Profit=st.number_input('Profit on the product')
    Quantity=st.number_input('Quantity of the product')
    Category = st.selectbox('Category', df['Category'].unique())
    Sub_category = st.selectbox('Sub-Category', df['Sub_category'].unique())
    City = st.selectbox('City', df['City'].unique())
    Country = st.selectbox('Country', df['Country'].unique())
    Region = st.selectbox('Region', df['Region'].unique())
    Segment = st.selectbox('Segment', df['Segment'].unique())
    Ship_Mode = st.selectbox('Ship Mode', df['Ship_Mode'].unique())
    State = st.selectbox('State', df['State'].unique())
    O_day = st.selectbox('O_day', df['O_day'].unique())
    O_year = st.selectbox('O_year', df['O_year'].unique())
    O_month = st.selectbox('O_month', df['O_month'].unique())
    Days_to_ship=st.selectbox('Shipping Days',df['Days_to_ship'].unique())


    data = pd.DataFrame({'Product_Name': Product_Name,
                            'Discount': Discount,
                            'Actual_Discount': Actual_Discount,
                            'Profit': Profit,
                            'Quantity': Quantity,
                            'Category': Category,
                            'Sub_category': Sub_category,
                            'City': City,
                            'Country': Country,
                            'Region': Region,
                            'Segment': Segment,
                            'Ship_Mode': Ship_Mode,
                            'State': State,
                            'O_day': O_day,
                            'O_year': O_year,
                            'O_month': O_month,
                            'Days_to_ship': Days_to_ship}, index=[0])
    
    if st.button('Predict Sales'):
        # Make predictions
        predictions = best_model.predict(data)
        predicted_sales = "{:.2f}".format(predictions[0])
        st.success(f'Predicted Sales is about {predicted_sales} Unit')

 
 
# Run the web app
if __name__ == '__main__':
    main()