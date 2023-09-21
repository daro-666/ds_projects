from utils import record, predict, start_process, stop_process
import logging


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
files_process, web_process, mail_process, media_process = None, None, None, None

logging.info("Ready!")

while True:

    command = predict(record("Waiting for voice input"))

    if command == 'open' or command == 'close': logging.info(f"command: {command}")
    
    if command == 'exit':
        confirm = input("Really want to quit? ([y]/n)\n")
        if confirm == 'y' or not confirm: break
    

    if command == 'open':
        while True:
            
            command = predict(record("Open"))
            
            if command != 'silence' and command != 'open' and command != 'close': logging.info(f"command: {command}")
            
            if command == 'files' and not files_process:
                logging.info("Opening Nautilus...")
                files_process = start_process('nautilus')
                break

            if command == 'web' and not web_process:
                logging.info("Opening Firefox...")
                web_process = start_process('firefox')
                break

            if command == 'mail' and not mail_process:
                logging.info("Opening Thunderbird...")
                mail_process = start_process('thunderbird')
                break

            if command == 'media' and not media_process:
                logging.info("Opening VLC...")
                media_process = start_process('vlc')
                break
            
            if command == 'exit': break


    if command == 'close':
        while True:
            
            command = predict(record("Close"))
            
            if command != 'silence' and command != 'open' and command != 'close': logging.info(f"command: {command}")
            
            if command == 'files' and files_process:
                logging.info("Closing Nautilus...")
                stop_process(files_process)
                files_process = None
                break

            if command == 'web' and web_process:
                logging.info("Closing Firefox...")
                stop_process(web_process)
                web_process = None
                break

            if command == 'mail' and mail_process:
                logging.info("Closing Thunderbird...")
                stop_process(mail_process)
                mail_process = None
                break

            if command == 'media' and media_process:
                logging.info("Closing VLC...")
                stop_process(media_process)
                media_process = None
                break

            if command == 'exit': break
