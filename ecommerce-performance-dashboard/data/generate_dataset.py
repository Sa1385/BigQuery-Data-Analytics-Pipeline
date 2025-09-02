import pandas as pd
import random
from faker import Faker

fake = Faker()

num_rows = 1000
categories = ["Tops & Tees", "Jeans", "Sweaters", "Swim", "Suits & Sportswear", "Footwear", "Accessories"]
regions = ["North", "South", "East", "West"]

data = []
for _ in range(num_rows):
    data.append({
        "order_id": fake.uuid4(),
        "customer_id": fake.random_int(min=1000, max=9999),
        "order_date": fake.date_between(start_date="-5y", end_date="today"),
        "category": random.choice(categories),
        "region": random.choice(regions),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 200), 2),
        "revenue": 0  
    })


for row in data:
    row["revenue"] = row["quantity"] * row["price"]

df = pd.DataFrame(data)
output_file = "sales_data.csv"
df.to_csv(output_file, index=False)

print(f"✅ Dataset generated successfully! Saved as: {output_file}")
print(f"📊 Rows generated: {len(df)}")


