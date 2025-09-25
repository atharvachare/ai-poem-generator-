from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
import threading

app = Flask(__name__)

# Load model lazily in a background thread to avoid blocking startup if desired:
generator = None
def load_model():
    global generator
    try:
        generator = pipeline("text-generation", model="gpt2")
        print("Model loaded.")
    except Exception as e:
        print("Error loading model:", e)

# Start background loader so site comes up quickly and model loads while you view page
threading.Thread(target=load_model, daemon=True).start()

@app.route("/", methods=["GET", "POST"])
def index():
    global generator
    poem_text = None
    prompt = ""
    loading_message = None

    if request.method == "POST":
        theme = request.form.get("theme", "").strip()
        if theme == "":
            prompt = "Write a short poem about life and hope:"
        else:
            prompt = f"Write a short poem about {theme.strip()}:"

        if generator is None:
            # Model not loaded yet — load synchronously (fallback)
            loading_message = "Model is loading — please wait a few seconds..."
            load_model()

        # Generate poem (keep short)
        try:
            raw = generator(prompt, max_length=120, num_return_sequences=1,
                            do_sample=True, temperature=0.8)
            poem_text = raw[0]["generated_text"]
            # If model copies the prompt, strip it for cleaner display:
            if poem_text.startswith(prompt):
                poem_text = poem_text[len(prompt):].strip()
        except Exception as e:
            poem_text = f"Error generating poem: {e}"

    return render_template("index.html", poem=poem_text, prompt=prompt, loading=loading_message)


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
