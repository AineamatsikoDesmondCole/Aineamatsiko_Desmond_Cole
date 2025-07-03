import requests
from datetime import datetime
import os


class TelegramPoster:
    def __init__(self, bot_token, chat_id):
        
        self.bot_token = '7023104789:AAGA3BvjEHj1WI6dkQMMdeaKi8PHDMa6QsY'   
        self.chat_id = '-1002751282818'
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/"
        
    def send_text_post(self, message, parse_mode="Markdown"):
     
        url = f"{self.base_url}sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": parse_mode
        }
        response = requests.post(url, params=params)
        return response.json()
    
    def send_photo_post(self, photo_path, caption=None):
        """
       
        """
        url = f"{self.base_url}sendPhoto"
        with open(photo_path, 'rb') as photo_file:
            files = {'photo': photo_file}
            data = {'chat_id': self.chat_id}
            if caption:
                data['caption'] = caption
            response = requests.post(url, files=files, data=data)
        return response.json()
    
    def schedule_post(self, post_function, post_time, *args, **kwargs):
       
        now = datetime.now()
        scheduled_time = datetime.strptime(post_time, '%Y-%m-%d %H:%M')
        
        if scheduled_time < now:
            return "Error: Scheduled time must be in the future"
            
        time_difference = (scheduled_time - now).total_seconds()
        
        
        import time
        time.sleep(time_difference)
        
        result = post_function(*args, **kwargs)
        return f"Post sent at {datetime.now()}. Result: {result}"

#
if __name__ == "__main__":
    
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your_bot_token_here')
    CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'your_chat_id_here')
    
    poster = TelegramPoster(BOT_TOKEN, CHAT_ID)
    
    
    text_response = poster.send_text_post(
        "Hi this is Desmonds Poster Bot",
        parse_mode="Markdown"
    )
    print("Text post response:", text_response)
    
  