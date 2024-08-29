# API Testing with Behave

Este repositorio contiene pruebas automatizadas utilizando Behave para la API de [restful-booker](https://restful-booker.herokuapp.com/).

## Requisitos

- Python 3.6+
- `pip` (Gestor de paquetes de Python)


## Instalación

1. Clona este repositorio: 

   ```bash
   git clone https://github.com/Mateosz12/EnerbitRetoApi.git
   ```

2. ejecutar todas las pruebas usa el comando:
   
  ```bash
    behave
  ```
3. ejecutar tag especifico
     ```bash
    behave --tags @tag_name
   ```
## Escenarios de prueba
**Auth**
```gherkin
   @auth  
  Scenario: Create a token for authentication
    Given I request a new token
    Then I should receive a token

```
**Create Booker**
```gherkin
  @create
Scenario: Create a new booking
    Given I have the API endpoint to create a booking
    And I have the request payload from "data/listCreateBooking.json"
    When I send a POST request to "/booking"
    Then the response status code should be 200
    And the response should be validated


```
**Get user booker**
```gherkin

  Scenario: Get booking by id
    When I send a GET request to "/booking/{booking_id}"
    Then the get response should be validated



```
**Update user booker**
```gherkin

@UpdateBooking
Scenario: Update a booking by id
    Given I send a PUT request to "/booking/booking_id" and send data from "data/putBooking.json"
    Then the response status  should be 200
 


```

**Delete user booker**
```gherkin

@DeleteBooking
Scenario: Delete a booking by id
    Given I send a DELETE request to "/booking/booking_id"
    Then the response status  should be 201
 


```
