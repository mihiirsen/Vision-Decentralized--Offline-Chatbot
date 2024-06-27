# from flask import Flask, render_template, request
# from llm_model import text_generate
# app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def chatbot():
#     if request.method == "POST":
#         text = request.form["text"]
#         uploaded_image = request.files["image_path"]

#         upload_folder = 'uploads/'  
#         file_path = upload_folder + 'uploaded_image.jpg'  
#         uploaded_image.save(file_path)

#         output_string = text_generate(text, file_path)

#         return render_template("index.html", output=output_string)
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True, port=8000, host="0.0.0.0")
import streamlit as st
from llm_model import text_generate
from PIL import Image

def main():
    st.title("Chatbot with Image Upload")

    text = st.text_input("Enter your text here:")
    uploaded_image = st.file_uploader("Upload an image")

    if uploaded_image is not None:  # Check if an image is uploaded
        image = Image.open(uploaded_image)
        output_string = text_generate(text, image)

        st.write("Output:")
        st.write(output_string)
    else:
        st.write("Please upload an image.")

if __name__ == "__main__":
    main()

