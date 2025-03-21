import pandas as pd
import re
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def clean_text(text):
    return text.replace('\u200e', '').strip()

def process_chat_file(file_obj):
    lines = file_obj.read().decode('utf-8').splitlines()

    pattern = r'^\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}:\d{2})\] (.*?): (.*)$'
    data = []

    for line in lines:
        line = clean_text(line)
        match = re.match(pattern, line)
        if match:
            date_str, time_str, name, message = match.groups()
            try:
                dt = datetime.strptime(f"{date_str} {time_str}", '%m/%d/%y %H:%M:%S')
            except ValueError:
                continue
            data.append([dt, clean_text(name), clean_text(message)])

    df = pd.DataFrame(data, columns=['datetime', 'name', 'message'])

    # Filter by date
    df_filtered = df[df['datetime'] >= datetime.strptime("3/1/25", "%m/%d/%y")]

    # Filter for image messages
    image_patterns = ['image omitted', r'<attached: .*PHOTO.*>']
    pattern_combined = '|'.join(image_patterns)
    df_images = df_filtered[df_filtered['message'].str.contains(pattern_combined, case=False, regex=True)]

    df_images = df_images.copy()
    df_images['date'] = df_images['datetime'].dt.date

    # Drop duplicate (name, date)
    df_unique_daily = df_images.drop_duplicates(subset=['name', 'date'])

    # Count unique image days
    daily_image_counts = df_unique_daily['name'].value_counts().reset_index()
    daily_image_counts.columns = ['name', 'unique_image_days']

    return daily_image_counts

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None

    if request.method == 'POST':
        file = request.files['chatfile']
        if file:
            results = process_chat_file(file)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
