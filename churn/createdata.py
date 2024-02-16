import pandas as pd
from faker import Faker
import random
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta, datetime
import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)
warnings.simplefilter("ignore", category=FutureWarning)

df_vehicles = pd.read_csv(f'Car_Models.csv')
df_vehicles["car_model"] = df_vehicles['Company'].astype(str) +" "+ df_vehicles["Model"]
df_vehicles['Year'] = df_vehicles['Model Year Range'].str.split('-').str[0]
df_vehicles = df_vehicles.drop(['Horsepower','Torque', 'Transmission Type','Drivetrain','Fuel Economy','Number of Doors','Body Type','Engine Type','Number of Cylinders','Company','Model','Price','Model Year Range'],axis=1)

fake = Faker('pt-BR')

def create_insurance_df(num_entries):
    data = {
        'Costumer_name': [],
        'Costumer_age': [],
        'Costumer_email': [],
        'Costumer_address': [],
        'Type_situation':[],
        'Outcome_insurance':[],
        'Days_to_fix':[],
        'Active_user':[]
    }
    
    for i in range(num_entries):
        name = fake.name()
        age = random.randint(20, 70)
        email = fake.email()
        address = fake.address()
        outcome_situation = fake.random_element(elements=('APPROVED', 'DENIED', 'NOT USED'))
        type_accident = fake.random_element(elements=('Collision', 'Natural Phenomena', 'Fire', 'Robbery'))
        days_to_fix = random.randint(1, 110)
        active_user = random.randint(0, 1)

        data['Costumer_name'].append(name)
        data['Costumer_age'].append(age)
        data['Costumer_email'].append(email)
        data['Costumer_address'].append(address)
        data['Type_situation'].append(type_accident)
        data['Outcome_insurance'].append(outcome_situation)
        data['Days_to_fix'].append(days_to_fix)
        data['Active_user'].append(active_user)
    
    return pd.DataFrame(data)

insurance_df = create_insurance_df(100)
for _ in range(22):  
    insurance_df = insurance_df.append(create_insurance_df(100), ignore_index=True)

insurance_df['random_car_model'] = [random.choice(df_vehicles['car_model'].tolist()) for _ in range(len(insurance_df))]
insurance_df = insurance_df.merge(df_vehicles, left_on='random_car_model',right_on='car_model', how='left')
insurance_df = insurance_df.drop('random_car_model',axis=1)
insurance_df['Count_claims'] = insurance_df.groupby('Costumer_name')['Costumer_name'].transform('count')

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

date_range = end_date - start_date

insurance_df['Situation_Date'] = [start_date + timedelta(days=random.randint(0, date_range.days)) for _ in range(len(insurance_df))]
insurance_df.drop_duplicates()
insurance_df['Costumer_id'] = pd.factorize(insurance_df['Costumer_name'])[0] + 1
insurance_df = insurance_df.rename(columns={'car_model': 'Car_model'})

insurance_df.to_csv("insurance_df.csv", index= False)