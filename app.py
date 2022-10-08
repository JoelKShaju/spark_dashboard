from flask import Flask, render_template, request
from data_loader import DataLoader
from utils importper_hour_consumption,  

app = Flask(__name__)

data_loader = DataLoader()
combined_df = data_loader.load_data()
current_date = "5/31/2019"
default_type = "electricity"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perhrconsumption', methods=['GET'])
def perhrconsumption():
    args = request.args
    args = args.to_dict()
    if args.get('date', ""):
        date = args['date']
    else:
        date = current_date

    if args.get('type', ""):
        type = args['type']
    else:
        type = default_type
    
    print(date, type)

    temp_df = per_hour_consumption(combined_df = combined_df, type = type, date = date)

if __name__ == '__main__':
    app.run(debug=True)