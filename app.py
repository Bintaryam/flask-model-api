from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

class DummyModel:
    def predict(self, X):
        return [sum(row) for row in X]

MODEL = DummyModel()

# --- HTML PAGE ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask ML API</title>
</head>
<body>
    <h1>Number Sum Predictor</h1>

    <p>Enter rows of numbers (comma separated):</p>

    <textarea id="numbers" rows="6" cols="40">1,2,3
10,20,30</textarea>
    <br><br>

    <button onclick="predict()">Predict</button>

    <h2>Result:</h2>
    <pre id="result"></pre>

    <script>
        async function predict() {
            const text = document.getElementById("numbers").value;

            const X = text
                .split("\\n")
                .filter(line => line.trim() !== "")
                .map(line => line.split(",").map(Number));

            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ X: X })
            });

            const data = await response.json();
            document.getElementById("result").textContent = JSON.stringify(data, null, 2);
        }
    </script>
</body>
</html>
"""

# --- HOME PAGE ---
@app.route("/")
def home():
    return render_template_string(HTML)

# --- API ENDPOINT ---
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = data["X"]
    y = MODEL.predict(X)
    return jsonify({"y": y}), 200

# --- RUN APP ---
if __name__ == "__main__":
    app.run(debug=True)