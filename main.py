import os
import time

def main():
    # These grab the keys you saved in your Railway Variables
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    print("🚀 BIZ4U Signals Bot is starting...")
    print(f"📡 Connected to Chat ID: {chat_id}")
    
    # This is the loop that keeps your bot running 24/7
    while True:
        print("📊 Bot is watching the markets...")
        # Your trading strategy logic will go here
        time.sleep(60)

if __name__ == "__main__":
    main()
