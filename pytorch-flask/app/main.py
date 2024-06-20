from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    pass
    # 1 load image
    # 2 image -> tensor
    # 3 prediction
    # 4 return json
    return None