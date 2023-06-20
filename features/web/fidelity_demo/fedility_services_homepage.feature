# created by Abhijeet Thorat at 2023-06-13 17:24.
#

Feature:Launch Fidelity Services Group web application

    @chrome.driver
    Scenario Outline: Launch Fidelity services and verify homepage
    Given I am on Fidelity services group home page
    Then I verify about us menu
    When I verify and click Our Products & Services menu
    Then I verify all product and services tab


  Examples:
   |  username |password|
   |12345789052|Testing|