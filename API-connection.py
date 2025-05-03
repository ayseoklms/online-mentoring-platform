from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(_name_)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/explain-question", methods=["POST"])
def explain_question():
    data = request.get_json()

    # JSON'dan bilgileri çek
    question = data.get("questionText")
    optionA = data.get("optionA")
    optionB = data.get("optionB")
    optionC = data.get("optionC")
    optionD = data.get("optionD")
    optionE = data.get("optionE")
    correctOption = data.get("correctOption")
    level = data.get("level")
    category = data.get("category")

    # Prompt oluştur
    prompt = f"""
Sen YDS öğrencilerini YDS sınavına hazırlayan bir ingilizce öğretmenisin. Bu soruyu Öğrencine anlayacağı şekilde açıkla.

Sana verdiğimiz çoktan seçmeli soruların seviyesi {level} ve kategorisi {category}:

Soru: {question}

Seçenekler:
A) {optionA}
B) {optionB}
C) {optionC}
D) {optionD}
E) {optionE}

Doğru Cevap: {correctOption}

Doğru seçeneğin neden doğru olduğuna ve diğerlerinin neden yanlış olduğuna dair açık ve özlü bir açıklama yapın. {level} öğrencileri için uygun olan basit ve içten bir dil kullanın.

"""

    # OpenAI API çağrısı
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen yardımsever ve açıklayıcı bir ingilizce öğretmenisin."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=400
        )

        explanation = response.choices[0].message["content"]

        return jsonify({
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if _name_ == "_main_":
    app.run(debug=True)