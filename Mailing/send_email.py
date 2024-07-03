import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fonction pour lire le contenu HTML du fichier
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Informations de l'email
from_email = "adresse mail "
to_emails = "destinataire"
subject = "Exemple de sujet"

# Lire le contenu HTML du fichier
html_content = read_html_file("index.html")

# Configuration du message
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = from_email
message["To"] = ", ".join(to_emails)  # Joindre les adresses email avec une virgule

# Ajouter le contenu HTML
html_part = MIMEText(html_content, "html")
message.attach(html_part)

# Mot de passe (utilisez un mot de passe d'application si 2FA est activé)
password = "mot de passe generer"

# Envoyer l'email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Démarrer la connexion TLS
        server.login(from_email, password)
        server.sendmail(from_email, to_emails, message.as_string())
        print("Email envoyé avec succès à tous les destinataires")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email: {e}")
