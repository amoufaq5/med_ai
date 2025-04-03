# app/main.py
from threading import Thread
from app.scheduler.scheduler import start_scheduler

if __name__ == "__main__":
    # Start scheduled scraping in a separate thread
    scheduler_thread = Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()
    
    # For now, we won't start the chatbot UI.
    print("Scheduler started. Running without UI. Press Ctrl+C to exit.")
    
    try:
        while True:
            pass  # Keeps the main thread alive
    except KeyboardInterrupt:
        print("Exiting...")
