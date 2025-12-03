from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/emote", methods=["GET"])
def emote():
    uid = request.args.get("uid")
    team = request.args.get("team")
    emote = request.args.get("emote")

    emote_map = {
        "dance1": 53,
        "dance2": 54,
        "dance3": 55
    }
    emote_id = emote_map.get(emote, 53)
    return jsonify({"status": "ok", "emote_id": emote_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)