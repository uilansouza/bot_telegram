import telebot

CHAVE_API ="6081310971:AAGXgLSmN7DEHP4APGKdUvA1rnJctVnCefU"

bot = telebot.TeleBot(CHAVE_API)
@bot.message_handler(commands=['pizza'])
def pizza(message):
    bot.send_message(message.chat.id,"Enviando pizza para a sua casa")

@bot.message_handler(commands=['hamburguer'])
def hamburguer(message):
    bot.send_message(message.chat.id,"Enviando hamburguer para a sua casa")

@bot.message_handler(commands=['salada'])
def salada(message):
    bot.send_message(message.chat.id, "Sua salada já esta a caminho")


@bot.message_handler(commands=['opcao1'])
def opcao1(message):
    texto = """
    O que você deseja:
    /pizza para pedir pizza
    /hamburguer para pedir hamburger
    /salada para pedir salada
    /voltar voltar ao menu principal
    """
    bot.send_message(message.chat.id,texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(message):
    bot.send_message(message.chat.id, "Para enviar uma reclação, envie um email para uilan.souza@uol.com.br")

@bot.message_handler(commands=['opcao3'])
def opcao3(message):
    #bot.reply_to(message,"Salve pra você também")
    bot.send_message(message.chat.id,"Salve pra você também")
def verificar(message):
    return True


@bot.message_handler(func=verificar)
def response(message):
    texto = """
    Não entendi o que escreveu, escolha uma opção:
    /opcao1 Fazer um pedido
    /opcao2 Reclamar um pedido
    /opcao3 Mandar um salve
    Nada que você escrever alem disso vai funcionar """
    bot.reply_to(message,texto)

bot.polling()