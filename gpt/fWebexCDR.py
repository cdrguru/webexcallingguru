import pandas as pd
import numpy as np
from faker import Faker
import random
import uuid

fake = Faker()

# Constants for dataset
num_records = 1000
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ']
departments = ['Cardiology', 'Emergency', 'General Surgery', 'Pediatrics', 'Radiology', 'Administration']
call_types = ['SIP_INBOUND', 'SIP_OUTBOUND', 'SIP_INTERNATIONAL', 'SIP_MEETING']
call_results = ['Success', 'Failure', 'No Answer']
user_types = ['Doctor', 'Nurse', 'Administrative Staff', 'Patient', 'Emergency Response Team']
client_types = ['Desktop', 'Mobile', 'Web']

# Generate fake dataset
data = []

for _ in range(num_records):
    start_time = fake.date_time_this_month()
    duration = np.random.randint(1, 3600)  # Duration in seconds
    call_type = np.random.choice(call_types)
    call_result = np.random.choice(call_results)
    user_type = np.random.choice(user_types)
    department = np.random.choice(departments)
    state = np.random.choice(states)
    client_type = np.random.choice(client_types)
         
    # Simulating realistic phone numbers
    calling_number = fake.msisdn()
    called_number = fake.msisdn()
         
    data.append({
        'Call Correlation ID': str(uuid.uuid4()),
        'Calling Line ID': calling_number,
        'Called Line ID': called_number,
        'Call Type': call_type,
        'Call Direction': 'INBOUND' if call_type == 'SIP_INBOUND' else 'OUTBOUND',
        'Duration': duration,
        'Answered': call_result == 'Success',
        'Start Time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'End Time': (start_time + pd.Timedelta(seconds=duration)).strftime('%Y-%m-%d %H:%M:%S'),
        'User ID': str(uuid.uuid4()),
        'Answer Time': start_time.strftime('%Y-%m-%d %H:%M:%S') if call_result == 'Success' else None,
        'Call Outcome': call_result,
        'Client Type': client_type,
        'User Type': user_type,
        'Department': department,
        'State': state
    })

# Create DataFrame
df = pd.DataFrame(data)

df.head()
