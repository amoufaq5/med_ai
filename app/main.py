# app/main.py
from threading import Thread
from app.ui.chatbot_ui import app as ui_app
from app.scheduler.scheduler import start_scheduler

if __name__ == "__main__":
    # Start scheduled scraping in a separate thread
    scheduler_thread = Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()
    
    # Start the Flask UI/API server
    ui_app.run(host="0.0.0.0", port=5000)
