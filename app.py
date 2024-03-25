from flask import Flask, request, render_template
import google.generativeai as genai
import os
app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():
   return render_template('index.html')
@app.route("/generate_products", methods=["POST"])
def generate_products():
  
  if request.method == "POST":
        productUrl = request.form.get('productUrl')
    
        if productUrl:
            prompt_text =f"""Can you suggest a better product or a better price for this one?

Here's the link: {productUrl}
"""
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt_text)
          
            return render_template("index.html", generated_products=response.text)
    

if __name__ == "__main__":
  app.run(debug=True)