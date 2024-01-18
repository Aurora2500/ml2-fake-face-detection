import shutil
import os
import re
import random

data = 'data'
train_test_split = 0.8
random.seed(42)

patterns = [
    (0, 'left_eye'),
    (1, 'right_eye'),
    (2, 'nose'),
    (3, 'mouth')
]

shutil.rmtree('data_test', ignore_errors=True)
shutil.rmtree('data_train', ignore_errors=True)
for b, name in patterns:
    shutil.rmtree(f'data_{name}', ignore_errors=True)
    new_data = f'data_{name}'
    os.makedirs(new_data, exist_ok=True)
    os.makedirs(f'{new_data}/real', exist_ok=True)
    os.makedirs(f'{new_data}/fake', exist_ok=True)

os.makedirs('data_test/real', exist_ok=True)
os.makedirs('data_test/fake', exist_ok=True)
os.makedirs('data_train/real', exist_ok=True)
os.makedirs('data_train/fake', exist_ok=True)

for file in os.listdir(f'data/real'):
    if random.random() < train_test_split:
        for _, name in patterns:
            shutil.copy(f'data/real/{file}', f'data_{name}/real/{file}')
        shutil.copy(f'data/real/{file}', f'data_train/real/{file}')
    else:
        shutil.copy(f'data/real/{file}', f'data_test/real/{file}')

for file in os.listdir(f'data/fake'):
    if random.random() < train_test_split:
        for b, name in patterns:
            if re.search('_' + '[01]' * b + '1' + '[01]' * (3-b) + '.jpg$', file):
                shutil.copy(f'data/fake/{file}', f'data_{name}/fake/{file}')
        shutil.copy(f'data/fake/{file}', f'data_train/fake/{file}')
    else:
        shutil.copy(f'data/fake/{file}', f'data_test/fake/{file}')
