# created by Abhijeet Thorat at 2023-06-13 19:49.
#

Feature: Mobile App application Login Test

  @appium.server
  Scenario Outline: Login to mobile application
    Given I Open one app on device
    When I enter valid msisdn "<msisdn>"
    Then I enter valid pin "<pin>"
    Then I enter valid otp "<OTP>"
    Then I verify and click on shop menu and then I do swipe up and swipe down
  Examples:
  |  msisdn |pin  |OTP|
  |630189444|12580|88888|