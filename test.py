#Test Dosyası 02.03.2025
import os
import openai
from dotenv import load_dotenv

load_dotenv() # .env dosyasındaki değişkenleri yükler

openai.api_key = os.getenv("OPENAI_API_KEY") # Ortam değişkeninden anahtarı alır

try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", # Veya seçtiğimiz başka bir model
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Say 'Merhaba Dünya!'"}
      ]
    )
    answer = response['choices'][0]['message']['content']
    print("API Bağlantısı Başarılı! Yanıt:", answer)
except Exception as e:
    print(f"API Bağlantı Hatası: {e}")