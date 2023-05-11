Feature: Login page

  Background:
    Given the user navigates to login page

  Scenario: login credentials presences on the login page
    When user should view the login credentials in the login page
    Then verify the login credentials presences in the login page

  Scenario: SignIn with login credentials
    When the user fills the user name in the login page
    And the user fills the password in the login page
    And click on the login Button
    Then home page is loaded

