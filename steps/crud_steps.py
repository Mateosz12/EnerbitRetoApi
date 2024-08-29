from behave import *
import requests
import logging
import json

## AUTHENTICATION

BASE_URL = 'https://restful-booker.herokuapp.com'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
TOKEN = None
TOKEN_FILE = 'data/token.json'

@given(u'I request a new token')
def step_request_new_token(context):
    response = requests.post(f'{BASE_URL}/auth', json={"username": "admin", "password": "password123"})
   
    if response.status_code == 200:
       
        context.token = response.json().get('token')
        with open(TOKEN_FILE, 'w') as file:
             json.dump({'token': context.token}, file)

        logging.info(f"succesfull: {response.status_code} - {response.text}")
    else:
        logging.info(f"Error: {response.status_code} - {response.text}")


@then(u'I should receive a token')
def step_verify_token(context):
    assert context.token is not None, "Token was not received"




 ## CREATE
@given('I have the API endpoint to create a booking')
def step_given_api_endpoint(context):
    context.endpoint = '/booking'

@given('I have the request payload from "{filename}"')
def step_given_request_payload(context, filename):
    with open(filename, 'r') as file:
        context.request_payload = json.load(file)

@when('I send a POST request to "{endpoint}"')
def step_when_send_post_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    headers = {'Accept': 'application/json'}
    context.response = requests.post(url, json=context.request_payload, headers=headers)

    response_json = context.response.json()
    context.booking_id = response_json.get('bookingid')

    
    with open('data/booking_id.txt', 'w') as file:
        file.write(str(context.booking_id))


@then('the response status code should be 200')
def step_then_status_code(context):
    assert context.response.status_code == 200

@then('the response should be validated')
def step_then_validate_response(context):
    assert context.response.status_code == 200

    response_json = context.response.json()
    logging.info(response_json)
    logging.info(f"Booking ID: {context.booking_id}")
    
    assert context.booking_id is not None, "ID was not received"
    assert isinstance(response_json['booking']['firstname'], str), "First name is not a string"
    assert isinstance(response_json['booking']['lastname'], str), "Last name is not a string"
    assert isinstance(response_json['booking']['totalprice'], (int, float)), "Total price is not a number"
    assert isinstance(response_json['booking']['depositpaid'], bool), "Deposit paid is not a boolean"
    assert isinstance(response_json['booking']['bookingdates'], dict), "Booking dates are not an object"
    assert isinstance(response_json['booking']['additionalneeds'], str), "Additional needs is not a string"
   


   ## GET

@when('I send a GET request to "/booking/{booking_id}"')
def step_when_send_get_request(context, booking_id):


    #logging.info(context.booking_id)
    with open('data/booking_id.txt', 'r') as file:
       context.booking_id = file.read().strip()
    

    url = f"{context.base_url}/booking/{context.booking_id}"
    headers = {'Accept': 'application/json'}
    context.response = requests.get(url, headers=headers)
   
    

@then('the get response should be validated')
def step_then_validate_response(context):
    logging.info(context.booking_id)
    logging.info(context.response.status_code)
    logging.info(context.response.text)
    assert context.response.status_code == 200



    ## UPDATE
@given(u'I send a PUT request to "/booking/booking_id" and send data from "{filename}"')
def step_impl(context,filename):

    with open(filename, 'r') as file:
        context.request_put = json.load(file)

    with open('data/booking_id.txt', 'r') as file:
       context.booking_id = file.read().strip()

    with open('data/token.json', 'r') as file:
        token_data = json.load(file)
        token = token_data.get('token')
    
    url = f"{context.base_url}/booking/{context.booking_id}"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={token}'
        }
    
    context.response = requests.put(url, headers=headers, json=context.request_put)
   


@then(u'the response status  should be 200')
def step_impl(context):
    assert context.response.status_code == 200

    response_json = context.response.json()
    logging.info(response_json)
   
    
   
    assert isinstance(response_json["firstname"], str), "First name is not a string"
    assert isinstance(response_json["lastname"], str), "Last name is not a string"
    assert isinstance(response_json["totalprice"], (int, float)), "Total price is not a number"
    assert isinstance(response_json["depositpaid"], bool), "Deposit paid is not a boolean"
    assert isinstance(response_json["bookingdates"], dict), "Booking dates are not an object"
    assert isinstance(response_json["additionalneeds"], str), "Additional needs is not a string"
   

## DELETE
@given(u'I send a DELETE request to "/booking/booking_id"')
def step_impl(context):

    with open('data/booking_id.txt', 'r') as file:
       context.booking_id = file.read().strip()

    with open('data/token.json', 'r') as file:
        token_data = json.load(file)
        token = token_data.get('token')
    
    url = f"{context.base_url}/booking/{context.booking_id}"

    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={token}'
        }
    
    context.response = requests.delete(url, headers=headers)


@then(u'the response status  should be 201')
def step_impl(context):

    logging.info(context.response.status_code)
    assert context.response.status_code == 201
    