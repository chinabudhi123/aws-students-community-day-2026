from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask! 🖥️",
        "timestamp": str(datetime.now()),
        "status": "running"
    })

@app.route("/about")
def about():
    return jsonify({
        "session": "From Zero to AI App",
        "event": "AWS Students Community Day 2026",
        "stack": ["S3", "EC2", "API Gateway", "Bedrock"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
