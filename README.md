# Key Logger
This program combines the keylogging functionality, screenshot capture, window logging, and email reports into one application. It runs each functionality in a separate thread to ensure they work concurrently.
Please use this progrom for educational use or were you have legal right. It's essential to use this monitoring tools responsibly and in compliance with the applicable laws and regulations. Make sure to inform your subject about the monitoring activities and respect their privacy within legal boundaries.

## basic implementation of the keylogger##

- Keylogging: The program utilizes the pynput.keyboard library to capture keypress events. When a key is pressed, the on_press() function is triggered, which appends the pressed key to a log file (keylog.txt).

- Screenshot Capture: The program uses the pyautogui library to capture screenshots at regular intervals. The capture_screenshot() function takes a screenshot and saves it with a timestamped filename.

- Window Logging: The program utilizes the pygetwindow library to log the currently focused window. The log_focused_window() function retrieves the active window and logs its title in a separate log file (window_log.txt).

- Email Reports: The program includes functionality to send email reports. The send_email_report() function constructs an email with a subject and message, then uses the smtplib library to send the email to a specified recipient.

- Threading: The program utilizes threading to run each functionality in separate threads, allowing them to work concurrently. Multiple threads are created for keylogging, screenshot capture, window logging, email reports, and the stop condition check.

Stop Condition: The program includes a check for a specific key combination (Ctrl + Alt + X) as a stop condition. If this combination is detected using the pynput.keyboard library, the program will stop executing.


## How to detect and prevent this keylogger##
Use reliable antivirus software: Install and regularly update reputable antivirus or anti-malware software on your device. Run a full system scan to check for any potential keyloggers or malicious programs.

Monitor running processes: Open the task manager on your device (Ctrl + Shift + Esc on Windows or Activity Monitor on macOS) and check the list of running processes. Look for any suspicious or unfamiliar processes that may indicate the presence of a keylogger.

Analyze network activity: Monitor your network traffic using network monitoring tools or firewalls. Look for any unexpected outgoing connections that may indicate data being sent by a keylogger.

Check startup programs: Review the list of programs that start automatically when your device boots up. On Windows, you can use the "Startup" tab in Task Manager or the "msconfig" command. On macOS, go to System Preferences > Users & Groups > Login Items. Disable or remove any suspicious or unrecognized programs from the startup list.

Perform a manual search: Manually search your device's file system for any suspicious files or folders. Pay attention to system directories, temporary folders, and the user's home directory. Look for any files with names that appear random or unfamiliar.

Use anti-keylogging software: Consider using specialized anti-keylogging software that can detect and prevent keyloggers. These programs can monitor and block keylogging activities on your device.

## To run this program##

Install Python: Ensure that you have Python installed on your computer. You can download the latest version of Python from the official Python website (https://www.python.org) and follow the installation instructions specific to your operating system.

Install Required Libraries: Open a terminal or command prompt and install the necessary libraries by running the following commands:

Copy code
`pip install pyautogui`
`pip install pygetwindow`
`pip install pynput`

```python 
import time
import pyautogui
import pygetwindow as gw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Listener, Key, KeyCode
```
These commands will install the required libraries for capturing screenshots, logging windows, and monitoring keyboard events.

Modify Configuration: Open the keylogger program file (in Python) using a text editor. Modify the variables at the beginning of the file to configure the program according to your needs. For example, you can set the log file names, email settings, intervals, and other parameters.

Save the Program: Save the modified program file with a .py extension, such as keylogger.py.

Run the Program: Open a terminal or command prompt, navigate to the directory where the keylogger program is saved, and run the following command:

Copy code
python keylogger.py
This command will execute the program and start capturing keystrokes, taking screenshots, logging window information, and potentially sending email reports.

