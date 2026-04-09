from flask import Flask, request, jsonify # Import Flask and related modules

app = Flask(__name__) # Create a Flask app instance

class DummyModel: # Define a dummy model class
    def predict(self, X): # Implement a simple prediction method that sums each row of the input
        return [sum(row) for row in X] # Return the sum of each row as the prediction

MODEL = DummyModel() # Create an instance of the dummy model

@app.route("/predict", methods=["POST"]) # Define a route for the /predict endpoint that accepts POST requests
def predict():
    data = request.get_json() # Get the JSON data from the request
    X = data["X"] # Extract the input data (X) from the JSON payload
    y = MODEL.predict(X) # Use the model to make predictions based on the input data
    return jsonify({"y": y}), 200 # Return the predictions as a JSON response with a 200 OK status code

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)