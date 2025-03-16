from twilio.rest import Client
# Credenciales Twilio
ACCOUNT_SID = "AC593a0a703e844246aa16fa4f38e1052e"
AUTH_TOKEN = "5cc1e76bafcbaaaa4f004541a2e7c991"
TWILIO_WHATSAPP = "whatsapp:+14155238886"
NUMERO_DESTINO = "whatsapp:+584120339774"
client = Client(ACCOUNT_SID, AUTH_TOKEN)
# Leer reporte
with open("reporte.txt", "r") as file:
    mensaje = file.read()
# Enviar mensaje
msg = client.messages.create(
    from_=TWILIO_WHATSAPP, 
    to=NUMERO_DESTINO, 
    body=mensaje)
print(f"Mensaje enviado con SID: {msg.sid}")