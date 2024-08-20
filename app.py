import csv
from faker import Faker

fake = Faker()

datas = []

def generate_data():
    for i in range(1000):
        row = [
            i + 1,
            fake.name(),
            fake.email(),
            f"https://github.com/{fake.user_name()}",
            fake.city(),
            fake.country(),
            fake.state(),  
            
        ]
        datas.append(row)
    
    csv_file = 'fake_data.csv'

    with open(csv_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['index','name','E mail' 'city', 'country', 'State', 'Github Link', 'phone_number'])
        writer.writerows(datas)

    print(f'1000 rows of fake data added to {csv_file}.')

generate_data()