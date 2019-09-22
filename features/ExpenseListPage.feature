Feature: Expense List Page

    @default
    Scenario: Displays default data
        Given Expense List Page is loaded
        Then Expense List Page has expense with title "Beer", payer "Amine" and amount "15.00 $" 
        Then Expense List Page has expense with title "Costumes", payer "Kévin" and amount "135.00 $" 
        Then Expense List Page has expense with title "Movies", payer "Julie" and amount "35.00 $" 
        Then Expense List Page has expense with title "Dinner", payer "Kévin" and amount "115.00 $" 
        Then Expense List Page has expense with title "Escape Game", payer "Amine" and amount "85.00 $" 

    @filtering
    Scenario: Filtering by Payer yields correct results
        Given Expense List Page is loaded
        When Perform filtering on "Amine"
        Then Expense List Page has expense with title "Beer", payer "Amine" and amount "15.00 $" 
        Then Expense List Page has expense with title "Escape Game", payer "Amine" and amount "85.00 $" 
        Then Expense List Page has not expense with title "Costumes", payer "Kévin" and amount "135.00 $" 
        Then Expense List Page has not expense with title "Movies", payer "Julie" and amount "35.00 $" 
        Then Expense List Page has not expense with title "Dinner", payer "Kévin" and amount "115.00 $" 

    @filtering
    Scenario: Filtering by Payer yields correct results
        Given Expense List Page is loaded
        When Perform filtering on "Amine"
        Then Expense List Page has expense with title "Beer", payer "Amine" and amount "15.00 $" 
        Then Expense List Page has expense with title "Escape Game", payer "Amine" and amount "85.00 $" 
        Then Expense List Page has not expense with title "Costumes", payer "Kévin" and amount "135.00 $" 
        Then Expense List Page has not expense with title "Movies", payer "Julie" and amount "35.00 $" 
        Then Expense List Page has not expense with title "Dinner", payer "Kévin" and amount "115.00 $" 
        When Perform filtering on "Tous"
        Then Expense List Page has expense with title "Beer", payer "Amine" and amount "15.00 $" 
        Then Expense List Page has expense with title "Costumes", payer "Kévin" and amount "135.00 $" 
        Then Expense List Page has expense with title "Movies", payer "Julie" and amount "35.00 $" 
        Then Expense List Page has expense with title "Dinner", payer "Kévin" and amount "115.00 $" 
        Then Expense List Page has expense with title "Escape Game", payer "Amine" and amount "85.00 $" 
    
    @addexpense
    Scenario: Adding valid new expense
        Given Expense List Page is loaded
        And Expense List has "5" entries
        When Add new expense with title "Diving", payer "Amine" and amount "12.00 $" 
        Then Expense List Page has expense with title "Diving", payer "Amine" and amount "12.00 $"
        And Expense List has "6" entries

    @fails @addexpense
    Scenario: Adding invalid new expense - no title        
        Given Expense List Page is loaded
        And Expense List has "5" entries
        When Add new expense with title "n/a", payer "Kévin" and amount "3.00 $"
        Then Expense List Page has no expense with title "n/a", payer "Kévin" and amount "3.00 $"
        And Expense List has "5" entries

    @fails @addexpense
    Scenario: Adding invalid new expense - no payer
        Given Expense List Page is loaded
        And Expense List has "5" entries
        When Add new expense with title "Wine", payer "n/a" and amount "7.00 $" 
        Then Expense List Page has no expense with title "Wine", payer "n/a" and amount "7.00 $"
        And Expense List has "5" entries

    @fails @addexpense
    Scenario: Adding invalid new expense - no amount
        Given Expense List Page is loaded
        And Expense List has "5" entries
        When Add new expense with title "Nuts", payer "Kévin" and amount "n/a" 
        Then Expense List Page has no expense with title "Nuts", payer "Kévin" and amount "n/a"
        And Expense List has "5" entries

    @sum
    Scenario: Expense Sum is correct
        Given Expense List Page is loaded
        Then Expense List Sum is equal to "385 $"

    @sum
    Scenario: Expense Sum is updated after adding new Expense
        Given Expense List Page is loaded
        And Expense List Sum is equal to "385 $"
        When Add new expense with title "Diving", payer "Amine" and amount "12.00 $" 
        Then Expense List Sum is equal to "397 $"

    @addpayer
    Scenario: Add new valid payer
        Given Expense List Page is loaded
        And Filter has not "Adam" as selectable value
        And Dropdown for payer in new expense has not "Adam" as selectable value
        When Add new payer with name "Adam"
        Then Filter has "Adam" as selectable value
        Then Dropdown for payer in new expense has "Adam" as selectable value

    @addpayer   @fails
    Scenario: Add new invalid payer
        Given Expense List Page is loaded
        And Filter has not "n/a" as selectable value
        And Dropdown for payer in new expense has not "n/a" as selectable value
        When Add new payer with name "n/a"
        Then Filter has not "n/a" as selectable value
        Then Dropdown for payer in new expense has not "n/a" as selectable value

    @journey
    Scenario: Add new payer and add new expense
        Given Expense List Page is loaded
        And Expense List Sum is equal to "385 $"
        When Add new payer with name "Adam"
        When Add new expense with title "Wheels", payer "Adam" and amount "312.00 $"
        Then Expense List Sum is equal to "697 $"
