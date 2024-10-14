# Invoice Extractor App

A web-based application that extracts and interprets information from uploaded images of invoices using Google Generative AI (Gemini Pro) and Streamlit. This tool helps automate the process of analyzing invoices, making it useful for data extraction, summarization, and answering queries based on invoice details.

## 🚀 Features

- **Upload Invoice Image**: Upload images of invoices in JPG, JPEG, or PNG format.
- **Generative AI Analysis**: Uses Google's Gemini Pro vision model to analyze invoice images.
- **Extracted Insights**: Provides detailed responses and information based on user input and the uploaded invoice.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.

## 🛠️ Tech Stack

- **Python**: Programming language used for developing the app.
- **Streamlit**: Framework for creating the web-based interface.
- **Google Generative AI (Gemini Pro)**: AI model for analyzing and interpreting invoice images.
- **PIL (Python Imaging Library)**: For handling image files.
- **dotenv**: For loading environment variables securely.

## 📦 Installation

1. **Clone the Repository**:
```
git clone https://github.com/M-Shaharyar/invoice-extractor-app.git
cd invoice-extractor-app
```
2. **Create a Virtual Environment**:
```
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

3. **Install Required Packages**:
```
pip install -r requirements.txt
```

4. **Set Up Environment Variables**:
- Create a .env file in the project directory.
- Add your Google API key in the .env file:
- makefile
```
GOOGLE_API_KEY=your_google_api_key
```

## 🖼️ Usage
1. Run the Application:


```
streamlit run app.py
```

2. Upload an Invoice Image: Use the provided interface to upload an image of an invoice in JPG, JPEG, or PNG format.

3. Provide a Prompt: Enter a prompt to specify what you want to know about the invoice.

4. Get the Response: Click on the 'Tell me about the invoice' button to generate and display the response.

## 📝 Example Input
- **Input Prompt**: "Extract the total amount and the date from this invoice."
- **Uploaded Image**: An image of an invoice in PNG format.
## 📄 Example Output
- **Response**: "The invoice shows a total amount of $150.00, and the date is 10th October 2024."

