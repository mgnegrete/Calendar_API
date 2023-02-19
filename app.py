import google.cloud.logging
import logging

# Instantiates a client
client = google.cloud.logging.Client()

# Configure the default logger to use the logging client
client.setup_logging()

def log_messages():
  logging.warning("Hello, World!")
  dict_info = {"foo": "bar", "info_id": 7}
  logging.info("Some extra information", extra = {"json_fields": dict_info})
log_messages()
