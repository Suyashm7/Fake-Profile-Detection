from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load pre-trained models from the 'models' directory
models = {
    'Decision Tree': 'models/decision_tree.pkl',
    'Naive Bayes': 'models/naive_bayes.pkl',
    'XGBoost': 'models/xgboost.pkl',
    'Random Forest': 'models/random_forest.pkl'
}

# Load models into a dictionary
loaded_models = {}
for model_name, model_path in models.items():
    try:
        with open(model_path, 'rb') as f:
            loaded_models[model_name] = pickle.load(f)
    except FileNotFoundError:
        print(f"Model file not found: {model_path}. Please ensure the model file exists.")

# Home page with slider and "Let's Start" button
@app.route('/')
def home():
    return render_template('home.html')

# Fake profile detection page
@app.route('/fake-detection', methods=['GET', 'POST'])
def fake_detection():
    if request.method == 'POST':
        # Retrieve form data
        selected_model = request.form['model']
        # Parse form data
        try:
            profile_pic = float(request.form['profile_pic'])
            username_length = float(request.form['username_length'])
            fullname_words = float(request.form['fullname_words'])
            fullname_length = float(request.form['fullname_length'])
            name_equals_username = float(request.form['name_equals_username'])
            description_length = float(request.form['description_length'])
            external_url = float(request.form['external_url'])
            is_private = float(request.form['is_private'])
            num_posts = float(request.form['num_posts'])
            num_followers = float(request.form['num_followers'])
            num_follows = float(request.form['num_follows'])
        except ValueError:
            return render_template('fake_detection.html', models=list(models.keys()), error="Please enter valid numerical values.")
            
        # Prepare input data for prediction
        profile_data = [
            profile_pic, username_length, fullname_words,
            fullname_length, name_equals_username,
            description_length, external_url,
            is_private, num_posts,
            num_followers, num_follows
        ]

        # Make prediction using the selected model
        model = loaded_models.get(selected_model)
        prediction = model.predict([profile_data])[0]

        # Determine if the profile is fake or genuine
        result = 'Fake Profile' if prediction == 1 else 'Genuine Profile'

        # Return result page with prediction
        return render_template('fake_detection_result.html', result=result)

    # Render the fake detection page
    return render_template('fake_detection.html', models=list(models.keys()))

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
