# Import necessary libraries and modules
from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables from a .env file

import streamlit as st  # Streamlit library for creating the web app
import os  # Library for interacting with the operating system
from PIL import Image  # Library for handling image files
import google.generativeai as genai  # Importing Google generative AI package for content generation

# Configure the generative AI with the API key from the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the generative model (e.g., Gemini Pro vision model)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to interact with the generative model and get a response
def get_gemini_response(input, image, prompt):
    # Generate content based on the input, image, and prompt
    response = model.generate_content([input, image[0], prompt])
    # Return the text content of the response
    return response.text

# Function to extract image details from an uploaded file
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded file as bytes
        bytes_data = uploaded_file.getvalue()

        # Create a list containing details of the image, including mime type and the data
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        # Return the image details as a list of parts
        return image_parts
    else:
        # Raise an error if no file was uploaded
        raise FileNotFoundError('No file uploaded')

# Initialize Streamlit app configuration
st.set_page_config(page_title="Invoice Extractor")

# Display the header for the application
st.header("Invoice Extractor Application")

# Input field for users to provide a text prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader for users to upload an image of an invoice
uploaded_file = st.file_uploader("Choose an image of the invoice: ", type=["jpg", "jpeg", "png"])

# Variable to store the uploaded image
image = ""

# Check if a file was uploaded
if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    # Display the uploaded image with a caption in the app
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit and process the image and prompt
submit = st.button("Tell me about the invoice")

# Define the input prompt for the generative AI model
input_prompt = """
    You are an expert in understanding invoices. We will upload an image of an invoice,
    and you will have to answer any questions based on the uploaded invoice image.
"""

# Check if the submit button is clicked
if submit:
    # Get the details of the uploaded image
    image_data = input_image_details(uploaded_file)
    # Get the response from the generative model based on the prompt, image data, and user input
    response = get_gemini_response(input_prompt, image_data, input)
    # Display the response in the app
    st.subheader("The Response is")
    st.write(response)
