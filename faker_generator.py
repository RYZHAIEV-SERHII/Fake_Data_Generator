import json
from datetime import date
from decimal import Decimal

from faker import Faker

# Dictionary mapping data type names to Faker methods
data_types = {
    'id': 'random_number',
    'name': 'name',
    'birthdate': 'date',
    'address': 'address',
    'phone': 'phone_number',
    'email': 'email',
    'url': 'url',
    'country': 'country',
    'profile': 'profile',
    'job': 'job',
    'time': 'time',
    'year': 'year',
    'text': 'text',
    'sentence': 'sentence'
}


def convert_to_serializable(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, date):
        return obj.isoformat()  # Convert date to string
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    return obj


def generate_data(records, selected_data_types, selected_locale):
    # Create a Faker instance with the selected locale
    fake = Faker(locale=selected_locale)

    # Declare an empty list to store data
    data_list = []

    # Iterate the loop based on the input value and generate fake data
    for n in range(0, records):
        data_dict = {}
        for data_type in selected_data_types:
            # Handle the "profile" data type separately
            if data_type == 'profile':
                value = convert_to_serializable(fake.profile())
            else:
                # Call the Faker method dynamically to get a new value each time
                method_name = data_types[data_type]
                faker_method = getattr(fake, method_name)
                value = faker_method()

            data_dict[data_type] = value

        data_list.append(data_dict)

    # Write the data into the JSON file
    with open('fake_data.json', 'w') as fp:
        json.dump(data_list, fp, default=convert_to_serializable)

    return 'fake_data.json'
