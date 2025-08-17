Feature: User should be able to fetch the details of dog breeds
    Scenario: User should be able to fetch all the breeds at a time
        Given A list of dog breeds are available
        When I send a request to retrive all the dog breed information
        Then It retrives the list of all the breeds
    
    Scenario: User should be able to get random breeds
        Given A list of random dog breeds
        When I send a request to randomly retrive all the dog breeds information
        Then It retrives a random list of some dog breeds

    Scenario Outline: User should be able to get results based on the breed
        Given an input of dog <breed>
        When I send a request to retrive the specific breed
        Then It retrives a list of the selected breed
        Examples:
            | hound |
            | African |
            | Akita |