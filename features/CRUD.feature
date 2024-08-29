Feature: Test API restful-booker

  @auth  
  Scenario: Create a token for authentication
    Given I request a new token
    Then I should receive a token

    
@create
Scenario: Create a new booking
    Given I have the API endpoint to create a booking
    And I have the request payload from "data/listCreateBooking.json"
    When I send a POST request to "/booking"
    Then the response status code should be 200
    And the response should be validated


  @get  
  Scenario: Get booking by id
    When I send a GET request to "/booking/{booking_id}"
    Then the get response should be validated

@UpdateBooking
Scenario: Update a booking by id
    Given I send a PUT request to "/booking/booking_id" and send data from "data/putBooking.json"
    Then the response status  should be 200
 
@DeleteBooking
Scenario: Delete a booking by id
    Given I send a DELETE request to "/booking/booking_id"
    Then the response status  should be 201
 