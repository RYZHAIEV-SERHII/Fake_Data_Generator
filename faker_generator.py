import json

from faker import Faker

# Declare faker object
fake = Faker()

# Dictionary mapping data type names to Faker methods
data_types = {
    'id': fake.random_number,
    'name': fake.name,
    'birthdate': fake.date,
    'address': fake.address,
    'email': fake.email,
    'phone': fake.phone_number
}


def generate_data(records, selected_data_types):
    # Declare an empty list to store data
    data_list = []

    # Iterate the loop based on the input value and generate fake data
    for n in range(0, records):
        data_dict = {}
        for data_type in selected_data_types:
            # Call the Faker method dynamically to get a new value each time
            data_dict[data_type] = data_types[data_type]()
        data_list.append(data_dict)

    # Write the data into the JSON file
    with open('fake_data.json', 'w') as fp:
        json.dump(data_list, fp)

    return 'fake_data.json'
