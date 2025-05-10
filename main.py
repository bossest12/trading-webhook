from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "웹훅 서버가 정상적으로 동작 중입니다.", 200
    elif request.method == 'POST':
        data = request.json
        print(f"알림 데이터 수신: {data}")
        return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
