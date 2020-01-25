*** Settings ***
Documentation       Example Robot tests for bank application

Resource            ../steps/resource.txt
Resource            ../steps/steps.txt

*** Test Cases ***
Retrieve customer balance
    Given I create the account 1111 with balance 50
    When I retrieve the account 1111
    And the balance should be 50