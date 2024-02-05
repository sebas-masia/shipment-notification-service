from flask import Blueprint, request, jsonify
from app.email_service import EmailSender
from dotenv import load_dotenv
import os

load_dotenv()
webhook_listener = Blueprint('webhook_listener', __name__)
email_sender = EmailSender(os.getenv("CONNECTION_STRING"))


@webhook_listener.route('/webhook-listener', methods=['POST'])
def receive_webhook():
    data = request.json
    # Process the webhook data here
    carrier_id = data['carrierOrder'][0]['carrier']['id']
    carrier_name = data['carrierOrder'][0]['carrier']['name']
    carrier_email = data['carrierOrder'][0]['contacts'][0]['email'][0]['email']

    # Send email to carrier from extracted data
    email_sender.send_email(
        "accounting@abd1c193-74c6-42d4-acbc-50f160c1d602.azurecomm.net", carrier_email, carrier_name, carrier_id)

    return jsonify({"carrier_id": carrier_id, "carrier_name": carrier_name, "carrier_email": carrier_email}), 200
