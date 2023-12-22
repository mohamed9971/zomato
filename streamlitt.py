import streamlit as st
import joblib
import pandas as pd
import numpy as np








Model = joblib.load('\app\project\zomato_rf.h5') 

def main():

    st.write('Welcome to zomato Classification Project')

    online_order = st.selectbox('Choose Online order Availability' , ('Yes' , 'No'))

    book_table = st.selectbox('Choose Table Book Availability' , ('Yes' , 'No'))

    votes = st.number_input('Please Enter Number of Votes')

    location = st.selectbox('Enter location' , 
                            ('BTM',
                              'HSR',
                            'Koramangala 5th Block',
                            'JP Nagar',
                            'Whitefield',
                            'Indiranagar',
                            'Jayanagar',
                            'Marathahalli',
                            'Bannerghatta Road',
                            'Bellandur',
                            'Electronic City',
                            'Koramangala 1st Block',
                             'Brigade Road',
                            'Koramangala 7th Block',
                            'Koramangala 6th Block',
                            'Sarjapur Road',
                            'Ulsoor',
                            'Koramangala 4th Block',
                            'MG Road',
                            'Banashankari',
                            'Kalyan Nagar',
                            'Richmond Road',
                            'Frazer Town',
                            'Malleshwaram',
                            'Basavanagudi',
                            'Other'
                            ))

    rest_type = st.selectbox('Enter Restaurant Type' ,('Quick Bites',
                                                        'Casual Dining',
                                                        'Cafe',
                                                        'Delivery',
                                                        'Dessert Parlor',
                                                        'Takeaway, Delivery',
                                                        'Casual Dining, Bar',
                                                        'Bakery',
                                                        'Beverage Shop',
                                                        'Bar') )

    approx_cost = st.number_input('Enter approximate cost for two people')


    prediction = 'Prediction is not made yet, Click Predict Car Price to make prediction.'

    input_data = [online_order,book_table,votes,location,rest_type,approx_cost]

    input_df = pd.DataFrame([input_data] , columns=['online_order','book_table','votes','location','rest_type','approx_cost(for two people)	'])

    if st.button('Predict Restaurant Rating.'):
        prediction = f'Restaurant Rating is {"{}".format(Model.predict(input_df)[0])}'
        
    st.success(prediction)


if __name__ == '__main__':
    main()
    
