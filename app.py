import streamlit as st
import PyPDF2
from io import BytesIO
from pyspark.sql import SparkSession

# Initialize Spark connection
spark = SparkSession.builder \
    .appName("Databricks App") \
    .config("spark.databricks.service.server.enabled", "true") \
    .config("spark.uri", "your_databricks_uri") \
    .config("spark.token", "your_access_token") \
    .getOrCreate()

# Create sidebar with multiple tabs
st.sidebar.title("Choose a Functionality")
option = st.sidebar.selectbox(
    "Select option:",
    ("Home", "File Upload", "Calculate Sum", "About")
)

# Based on sidebar choice, display corresponding activity in main area
if option == "Home":
    st.title("Welcome to the Home Page!")
    st.write("Choose an option from the sidebar to get started.")

elif option == "Calculate Sum":
    st.title("Simple Calculator")
    num1 = st.text_input("Enter first number:", 0)
    num2 = st.text_input("Enter second number:", 0)

    if st.button("Calculate"):
        try:
            result = float(num1) + float(num2)
            st.write("Result:", result)
        except ValueError:
            st.write("Please enter valid numbers.")

elif option == "File Upload":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Convert the uploaded file to bytes
        pdf_bytes = BytesIO(uploaded_file.read())
        
        # To read PDF file using the updated PdfReader class
        pdfReader = PyPDF2.PdfReader(pdf_bytes)
        
        # Get number of pages in PDF
        st.write("Number of Pages: ", len(pdfReader.pages))

elif option == "About":
    st.title("About this app")
    st.write("This is a simple Streamlit app demonstrating multiple functionalities.")

