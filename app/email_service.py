from azure.communication.email import EmailClient


class EmailSender:
    def __init__(self, connection_string):
        self.client = EmailClient.from_connection_string(connection_string)

    def send_email(self, sender_address, recipient_address, subject, plain_text_content):
        message = {
            "senderAddress": sender_address,
            "recipients": {
                "to": [{"address": recipient_address}],
            },
            "content": {
                "subject": subject,
                "plainText": plain_text_content,
            }
        }

        try:
            poller = self.client.begin_send(message)
            result = poller.result()
            return result
        except Exception as ex:
            return str(ex)

# Test email service
# test_trial = EmailSender(os.getenv("CONNECTION_STRING"))
# test_trial.send_email("accounting@abd1c193-74c6-42d4-acbc-50f160c1d602.azurecomm.net",
#                       "smasia@roklanes.com", "hola", "hola")
