import pandas as pd
import os

excel_file = 'pylinux_processed.csv'
df = pd.read_csv(excel_file)

user_packages = {}

for _, row in df.iterrows():
    package = row['Package']
    user = row['User']
    
    if user not in user_packages:
        user_packages[user] = []
    
    user_packages[user].append(package)

for user, packages in user_packages.items():
    # Create directory for the user
    os.makedirs(user, exist_ok=True)
    
    with open(f'{user}/requirements_pylinux.txt', 'w') as f:
        for package in packages:
            f.write(f'{package}\n')

print("Requirements files generated successfully.")
