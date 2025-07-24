from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import openai
import fitz  # PyMuPDF
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

openai.api_key = "your-openai-api-key"  # Вставь сюда свой ключ

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def evaluate_with_gpt(text):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in evaluating EER diagrams submitted by students."},
            {"role": "user", "content": f"Evaluate the following EER diagram:\n\n{text}"}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    evaluations = []
    if request.method == "POST":
        files = request.files.getlist("pdf")
        for file in files:
            if file and file.filename.endswith(".pdf"):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                text = extract_text_from_pdf(filepath)
                result = evaluate_with_gpt(text)
                evaluations.append({"filename": filename, "result": result})
    return render_template("index.html", evaluations=evaluations)

if __name__ == "__main__":
    app.run(debug=True)
