from flask import Flask, render_template
from google.cloud import logging

app = Flask(__name__)

gcp_log_client = logging.Client()
log_name = "my-app-log"
logger = gcp_log_client.logger(log_name)


@app.route('/')
def welcome():
  print('Opening Welcome.html page.')
  logger.log_text("Opening Welcome.html page.", severity="INFO")
  return render_template("welcome.html")

@app.errorhandler(404)
def page_not_found(e):
  print('Page Not Found!')
  logger.log_text("Page Not Found - 404", severity="ERROR")
  return render_template('404.html'), 404

app.run(host='0.0.0.0', port=5000)
