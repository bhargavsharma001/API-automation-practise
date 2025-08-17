import requests
from resources import * 
from configurations import *

config=get_config()
resource=Resources()

#get All breeds
get_all_breeds=config['API']['url']+resource.get_all_breeds()
try:
    response_get_all_breeds=requests.get(get_all_breeds,verify=False)
except Exception as e:
    print(e)
    
if response_get_all_breeds.status_code==200:
    assert response_get_all_breeds.json().get('status')=='success'
else:
    print("Some error occured while fetching all breeds")


#get random breeds
get_random_breeds=config['API']['url']+resource.get_random_breed()
try:
    response_random_breeds=requests.get(get_random_breeds,verify=False)
except Exception as e:
    print(e)
    
if response_random_breeds.status_code==200:
    assert response_random_breeds.json().get('status')=='success'
else:
    print("Some error occured while getting random breeds")



#get by breed

get_by_breed=config['API']['url']+resource.get_by_breed('hound')
try:
    response_get_by_breed=requests.get(get_random_breeds,verify=False)
except Exception as e:
    print(e)

if response_get_by_breed.status_code==200:
    assert response_get_by_breed.json().get('status')=='success'
else:
    print("Some error occured while getting get by breed type")


