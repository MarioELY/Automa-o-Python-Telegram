import telebot

token="SEU TOKEN"
chat_id = "SEU CHAT-ID"

while True:
    # Mensagem inicial
    bot = telebot.TeleBot(token)
    entrada_tipo = input("Informe o tipo de entrada (coluna ou dúzia): ")
    if entrada_tipo == 'sair':
        break
    bot.send_message(chat_id, f"⚠️ Atenção possível entrada {entrada_tipo.upper()}⚠️")

    # Solicitar ao usuário o tipo de entrada (coluna ou dúzia)


    # Solicitar ao usuário os números da entrada separados por espaço
    entrada_numeros = input("Informe os números da entrada separados por espaço: ")

    #Nivel da entrada
    nivel = input('Assertividade: ')
    # Solicitar ao usuário o "último número"
    ultimo_numero = input("Informe o último número: ")

    # Construir a mensagem com base nas informações fornecidas pelo usuário
    mensagem = f"🚨 ENTRADA CONFIRMADA\n💿 Roleta: A\n👑 Entrada: {entrada_tipo.upper()} {entrada_numeros}\n❤️ Até duas proteções\n⚠️ Marcar o Zero\n💎 Último número: {ultimo_numero}\n❗ Nivel de assertividade: {nivel} "

    # Enviar a mensagem para o Telegram
    bot.send_message(chat_id, mensagem)

    # Solicitar ao usuário ('win' ou 'loss')
    while True:
        resultado = input("Informe o resultado ('win' ou 'loss'): ")

        if resultado.lower() == 'win':
            quantidade_martingales = input("Quantos Martingales você usou? ")
            bot.send_message(chat_id, f"✅{quantidade_martingales} ")
            break
        else:
            bot.send_message(chat_id, "❌ Resultado: loss")
            break



