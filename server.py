from flask import Flask, request, jsonify
from mobilenet import predictModel

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    try:
        response = predictModel(image)
        print(response)
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')

#running this command for create new tag
#docker buildx build --platform linux/amd64 -t flask-server .                                    
#docker tag flask-server asia-southeast1-docker.pkg.dev/flask-server-418411/cloudrun-flask/flask-server:version
#docker push asia-southeast1-docker.pkg.dev/flask-server-418411/cloudrun-flask/flask-server:version