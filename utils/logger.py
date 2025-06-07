# Placeholder for logger.py
import logging

logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_request_response(user_input, response):
    logging.info(f"USER: {user_input}")
    logging.info(f"BOT: {response}")
