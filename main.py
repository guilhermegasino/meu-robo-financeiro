import telebot
import os
from flask import Flask

# 1. Configuração do Bot
TOKEN = "8327712242:AAHrsMt1iYMsfoNJASrPj-Xk4KJX9ZHeA14"
bot = telebot.TeleBot(TOKEN)

# 2. Truque para o Render (Servidor Web Simples)
app = Flask(__name__)

@app.route('/')
def home():
    return "Robô Elixir está online!"

@bot.message_handler(func=lambda message: True)
def salvar_lancamento(message):
    try:
        texto = message.text
        with open("lancamentos.csv", "a", encoding="utf-8") as f:
            f.write(f"{texto}\n")
        bot.reply_to(message, "✅ Lançamento registrado no Render!")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro: {e}")

# 3. Rodar o Bot
if __name__ == "__main__":
    # Inicia o bot em uma thread separada ou apenas o polling
    print("🚀 Robô Elixir ON no Render!")
    bot.infinity_polling()
