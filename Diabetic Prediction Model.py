import numpy as np
import streamlit as st
import pickle


#loading a save model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# createing a function for prediction


def Diabetic_Prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
 
def main():
    
    # giveing title
    st.title("Diabetic Prediction Web App")
    
    
    # Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome

    Pregnancies=st.text_input("Number of  Pregnancies : ")
    Glucose=st.text_input("Glucode Level:")
    BloodPressure=st.text_input("BloodPressure Value : ")
    SkinThickness=st.text_input("Skin Thickness Value : ")
    Insulin =st.text_input("Insulin Level: ")
    BMI=st.text_input("BMI Value : ")
    DiabetesPedigreeFunction =st.text_input("Diabetic Pedigree Function : ")
    Age	=st.text_input("Age of Person : ")
    
    #code for  preiction
    diagonis=''
    
    # creating a button
    if st.button('Diabetic test Result '):
        diagonis = Diabetic_Prediction([Pregnancies,	Glucose,	BloodPressure, 	SkinThickness	,Insulin,	BMI	,DiabetesPedigreeFunction	,Age	])
        
    st.success(diagonis)    
   
   
if __name__ == '__main__':
    main()    