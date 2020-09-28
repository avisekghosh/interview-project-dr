import sqlite3

from flask import Flask, request
from slack import WebClient
from slack.errors import SlackApiError

from config import *

app = Flask(__name__)


def send_msg_to_slack(msg="HelloWorld", channel_name="#test"):
    try:
        client = WebClient(token=API_TOKEN)
        response = client.chat_postMessage(
            channel=channel_name,
            text=msg)
        assert response["message"]["text"] == msg
        return True
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        # print(e)
        return False


def write_to_db(msg=None):
    if msg is not None:
        conn = sqlite3.connect('/home/ubuntu/db_mount/filestore.db')
        try:
            conn.execute("""INSERT INTO log (msg) VALUES ("%s")""" % (msg))
            conn.commit()
            return True
        except Exception as e:
            return False
        finally:
            conn.close()




@app.route("/ping")
def ping():
    return "It Works m2"




@app.route("/msg_from_client", methods=['POST'])
def msg_from_client():
    try:
        post_data = request.get_json()
        msg = post_data.get('msg', None)
        if msg is not None:
            write_to_db(msg)
            send_msg_to_slack("Received from M1", CHANNEL)
            return {"response": "Msg sending successful"} , 200
        else:
            return {"response": "Msg sending failed", "error": "Empty msg received"}, 400
    except Exception as e:
        return {"response": "Msg sending failed", "error": str(e)}, 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')
