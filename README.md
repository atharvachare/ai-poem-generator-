# 🤖 Flask GPT-2 Poem Generator

This project is a simple web application built with **Flask** and **Hugging Face Transformers** that generates short poems based on a theme provided by the user[cite: 1]. It uses the popular **GPT-2** language model for text generation.

A key feature of this app is its **lazy model loading** using Python threading, which allows the Flask server to start up quickly while the large machine learning model loads in the background, improving perceived responsiveness.

---

## ✨ Features

- **Poem Generation:** Generates original poetry using the `gpt2` model.
- **Flask Web Interface:** Simple web UI to input a theme and display the generated poem.
- **Asynchronous Model Loading:** Uses a background thread to load the large `gpt2` model after the server starts, preventing long startup delays.
- [cite\_start]**Simple Deployment Ready:** Includes `requirements.txt` and is compatible with web hosts[cite: 1].

---

## 🛠️ Installation and Setup

Follow these steps to get a local copy of the project up and running.

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 2: Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# Create the environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### Step 3: Install Dependencies

All necessary libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will now be running at **`http://127.0.0.1:5000/`**.

**Note:** The first time you visit the page, the GPT-2 model will begin downloading and loading. You may see a message saying "**Model is loading — please wait a few seconds...**" until the generation pipeline is fully ready.

---

## 📝 Usage

1.  Navigate to the application's URL (`http://127.0.0.1:5000/`).
2.  In the text box, enter a **theme** (e.g., "the ocean and freedom," "winter rain").
3.  Click the "Generate Poem" button.
4.  The application will use GPT-2 to write a short, unique poem based on your prompt. If you leave the theme blank, it defaults to "life and hope".

---

## 📂 Project Files

| File/Folder        | Description                                                                                        |
| :----------------- | :------------------------------------------------------------------------------------------------- |
| `app.py`           | The main Flask application, containing routes and the logic for model loading and text generation. |
| `requirements.txt` | [cite\_start]Lists Python dependencies: `flask`, `transformers`, `torch`, and `gunicorn`[cite: 1]. |
| `templates/`       | Directory containing the `index.html` template for the web interface.                              |
| `.gitignore`       | Standard file to exclude virtual environments and temporary files from Git tracking.               |

---

## ⚙️ Dependencies

- [cite_start][**Flask**](https://flask.palletsprojects.com/): The web framework[cite: 1].
- [cite_start][**Hugging Face Transformers**](https://huggingface.co/docs/transformers/): Used for easy access to and use of the `gpt2` model[cite: 1].
- [cite_start][**PyTorch (torch)**](https://pytorch.org/): The deep learning library that powers the generation model[cite: 1].
- [cite\_start]**Gunicorn** (optional): A WSGI HTTP server for production deployment[cite: 1].
