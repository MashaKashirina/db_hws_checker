# 📊 EER Diagram Evaluator

This project is a simple web app that allows you to upload PDF files containing EER diagrams. It extracts the content from each PDF, sends it to the OpenAI GPT model (e.g., GPT-4), and returns an expert-like evaluation of the diagram.

---

## 🧰 Features

- Upload and evaluate PDF files with EER diagrams (text-based).
- Uses OpenAI Chat API for automatic evaluation.
- Clean and responsive UI built with Tailwind CSS.
- Shows evaluation results directly on the page.

---

## 🖥️ Requirements

Make sure you have the following installed:

- Python 3.7+
- pip (Python package manager)
- OpenAI API Key

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/eer-evaluator.git
cd eer-evaluator
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key**

Open the `app.py` file and replace:

```python
openai.api_key = "your-openai-api-key"
```

with your actual key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).

---

## ▶️ Steps to Run the App

1. In your terminal, start the Flask app:

```bash
python app.py
```

2. Open your web browser and go to:

```
http://127.0.0.1:5000
```

3. Upload a `.pdf` file that contains an EER diagram (preferably in textual format).

4. Wait a few seconds. The evaluation result will appear below the form.

---

## 📁 Project Structure

```
eer-evaluator/
│
├── app.py               # Flask backend
├── templates/
│   └── index.html       # HTML frontend
├── static/
│   └── style.css        # Optional custom CSS
├── uploads/             # PDF uploads directory (auto-created)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 💡 Tip

The GPT model works best with EER diagrams that are described with clear text (e.g., entity names, relationships, attributes). If your diagrams are image-only, consider adding captions or use OCR tools to convert them to text first.

---

## 🔧 Future Ideas

- Extract diagram images and send them to GPT with image understanding (GPT-4o or Vision).
- Batch upload and grading.
- Save evaluations to database or downloadable report.
- Transfer uploads to a database as well