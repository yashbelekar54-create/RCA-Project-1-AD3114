"""Generate the synthetic Food Delivery Customers dataset used in this project.

Run:  python generate_dataset.py
Output: Food Delivery Customers.csv  (500 rows, 8 columns)

The data is synthetic (seeded, reproducible). Yearly spend (INR) depends on
order frequency, app time and membership length, weakly on website time,
plus random noise.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 500

cities = ["Mumbai", "Pune", "Bengaluru", "Delhi", "Hyderabad", "Chennai",
          "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"]
avatars = ["Teal", "Saffron", "Indigo", "Crimson", "Olive", "Violet", "Coral", "Slate"]

orders = np.clip(rng.normal(6, 1.5, n), 1, None)          # orders per month
app = rng.normal(14, 2.0, n)                              # minutes per session on app
web = rng.normal(30, 4.0, n)                              # minutes per session on website
member = np.clip(rng.normal(3.5, 1.0, n), 0.2, None)      # years of membership

spend = (15000 + 3200 * orders + 2100 * app + 150 * web + 6800 * member
         + rng.normal(0, 3500, n))

df = pd.DataFrame({
    "Email": [f"customer{i:03d}@example.com" for i in range(1, n + 1)],
    "City": rng.choice(cities, n),
    "Avatar": rng.choice(avatars, n),
    "Avg. Orders per Month": orders.round(2),
    "Time on App": app.round(2),
    "Time on Website": web.round(2),
    "Length of Membership": member.round(2),
    "Yearly Amount Spent": spend.round(2),
})
df.to_csv("Food Delivery Customers.csv", index=False)
print(df.shape)
