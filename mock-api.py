from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

# Generates X numbers of records
NUM_RECORDS = 10000

# Define the endpoint to retrieve random data
@app.route('/api/product', methods=['GET'])
def get_random_data():
    data = generate_random_data(NUM_RECORDS)
    return jsonify(data)

def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'id': fake.uuid4(),
            'total_availlble': fake.random_int(),
            'name': fake.word(ext_word_list=['Chair', 'Shoes', 'Shirt', 'Soap', 'Hat', 'keyboard']),
            'unit_price': round(random.uniform(0.0, 1000.0), 2),
            'created_at': fake.date_time(),
            'total_purchased': fake.random_int(),
            'color': fake.color(),
            'total_clicks': fake.random_int(),
            # Add more fields as needed
        }
        data.append(record)
    return data

if __name__ == '__main__':
    app.run(debug=True)