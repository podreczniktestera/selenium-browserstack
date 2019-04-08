#noinspection CucumberUndefinedStep
Feature: Google search bar

  Testing google search bar


  @search_button
  Scenario Outline: Search for things
    Given user is at google home page
     When search for "<thing>"
     Then waits for page to finish loading
      And results page shows up
      And results for "<thing>" are displayed

         Examples:
          | thing    |
          | python   |
          | 234153   |


  @feeling_lucky_button
  Scenario: I'm feeling lucky
    Given user is at google home page
     When user types "chromedriver" in search bar
      And clicks on "I'm feeling lucky" button
     Then waits for page to finish loading
      And result for "chromedriver" is displayed
