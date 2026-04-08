from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    # Obtener el texto ingresado por el usuario en la interfaz web
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pasar el texto a nuestra función de detección de emociones
    response = emotion_detector(text_to_analyze)
    
    # Formatear la cadena de salida exactamente como se requiere
    formated_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formated_response

@app.route("/")
def render_index_page():
    # Renderizar la página HTML principal
    return render_template('index.html')

if __name__ == "__main__":
    # Ejecutar la aplicación en el puerto 5000
    app.run(host="0.0.0.0", port=5000)
