##Creating a dummy data set and save the data in a csv

import pandas as pd
from faker import Faker
import random

fake =  Faker()

data = []

for _ in range(51):
    data.append(
        {
        "id":fake.uuid4(),
        "name":fake.name(),
        "email": fake.email(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today'),
        "country": fake.country(),
        "age": random.randint(18, 65),
        "purchase_amount": round(random.uniform(10.5, 999.99), 2)
        }
    )

df = pd.DataFrame(data)
df.to_csv("sample_customers.csv", index=False)