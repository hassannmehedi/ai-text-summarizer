from flask import Flask, render_template, request
import os
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=f"Summarize the following text in simple English:\n\n{text}"
            )

            summary = response.text

    return render_template(
        "index.html",
        summary=summary
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))