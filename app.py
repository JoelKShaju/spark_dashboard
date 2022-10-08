from flask import Flask, render_template
from data_loader import DataLoader

app = Flask(__name__)

data_loader = DataLoader()
combined_df = data_loader.load_data()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)