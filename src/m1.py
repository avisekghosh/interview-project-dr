import requests
from flask import Flask, request

app = Flask(__name__)


def send_to_m1(msg):
    r = requests.post('http://m2-net:5001/msg_from_client', json={"msg": msg})
    if r.status_code == 200:
        return True
    else:
        return False

@app.route("/ping")
def ping():
    return "It Works m1"


@app.route("/msg", methods=['POST'])
def msg():
    try:
        post_data = request.get_json()
        msg = post_data.get("msg", None)

        if msg is None:
            return {"response": "Msg sending failed", "error": "Empty msg received"}, 400
        else:
            out = send_to_m1(msg)
            if out:
                return {"response": "Msg sending successful"} , 200
            else:
                return {"response": "Msg sending failed"}, 500
    except Exception as e:
        return {"response": "Msg sending failed", "error": str(e)}, 500




if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')