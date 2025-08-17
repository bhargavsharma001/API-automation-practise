from behave import *
from behave.api.pending_step import StepNotImplementedError
import requests

from configurations import *
from resources import *


config=get_config()
resource=Resources()

@given('A list of dog breeds are available')
def step_impl(context):
    context.get_all_breeds=config['API']['url']+resource.get_all_breeds()
    

@when(u'I send a request to retrive all the dog breed information')
def step_impl(context):
    try:
        context.response_get_all_breeds=requests.get(context.get_all_breeds,verify=False)
    except Exception as e:
        print(e)

@then(u'It retrives the list of all the breeds')
def step_impl(context):
    if context.response_get_all_breeds.status_code==200:
        assert context.response_get_all_breeds.json().get('status')=='success'
    else:
        print("Some error occured while fetching all breeds")
        
        
        
@given('A list of random dog breeds')
def step_impl(context):
    context.get_random_breeds=config['API']['url']+resource.get_random_breed()

@when('I send a request to randomly retrive all the dog breeds information')
def step_impl(context):
    
    try:
        context.response_random_breeds=requests.get(context.get_random_breeds,verify=False)
    except Exception as e:
        print(e)


@then('It retrives a random list of some dog breeds')
def step_impl(context):
    if context.response_random_breeds.status_code==200:
        assert context.response_random_breeds.json().get('status')=='success'
    else:
        print("Some error occured while getting random breeds")
        
        
@given('an input of dog {breed}')
def step_impl(context,breed):
    context.get_by_breed=config['API']['url']+resource.get_by_breed(breed)


@when('I send a request to retrive the specific breed')
def step_impl(context):
    try:
        context.response_get_by_breed=requests.get(context.get_by_breed,verify=False)
    except Exception as e:
        print(e)


@then('It retrives a list of the selected breed')
def step_impl(context):
    if context.response_get_by_breed.status_code==200:
        assert context.response_get_by_breed.json().get('status')=='success'
    else:
        print("Some error occured while getting get by breed type")