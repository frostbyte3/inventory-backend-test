# Order Management Test Project Backend [Django]

Your job on this project is to develop an order management module.

Complete as many tasks as you can, submit the project when you're ready. 

It's okay if you do not complete everything, but please do not take any breaks. 
Part of the test is to see how much you get done within the timeframe of your work.

### Task 1: Setup

Create a RESTful API using Django REST framework. Use the boilerplate code, name the project "TestProject" and an app named "inventory"

### Task 2: Data Model
Create the following models to inventory smoothies:

Product Model:

id (AutoField, Primary Key)
name (CharField) - Name of the smoothie product.
description (TextField) - A description of the smoothie.
price (DecimalField) - The price of the smoothie.
created_at (DateTimeField) - Timestamp when the product was added to the inventory.
updated_at (DateTimeField) - Timestamp when the product information was last updated.

Inventory Model:

id (AutoField, Primary Key)
product (ForeignKey to Product) - A reference to the related smoothie product.
quantity (PositiveIntegerField) - The current quantity of the smoothie in stock.
created_at (DateTimeField) - Timestamp when the inventory entry was created.
updated_at (DateTimeField) - Timestamp when the inventory entry was last updated.

Sale Model:

id (AutoField, Primary Key)
product (ForeignKey to Product) - A reference to the smoothie product sold.
quantity (PositiveIntegerField) - The quantity of the smoothie sold in the transaction.
total_price (DecimalField) - The total price of the smoothie(s) sold in the transaction.
transaction_time (DateTimeField) - Timestamp when the sale transaction occurred.


StockUpdate Model:

id (AutoField, Primary Key)
product (ForeignKey to Product) - A reference to the smoothie product being updated.
quantity_change (IntegerField) - The change in quantity (positive for increase, negative for decrease).
reason (CharField) - A reason for the stock update (e.g., "Received new shipment," "Sold to customer").
update_time (DateTimeField) - Timestamp when the stock update was received via the webhook.

### Task 3: Views
Add the following Views:

Product Views:

List View: Display a list of available smoothie products.
Detail View: Show details of a specific smoothie product.
Create View: Allow adding new smoothie products to the inventory.
Update View: Edit and update existing smoothie product details.
Delete View: Remove a smoothie product from the inventory.

Inventory Views:

Inventory List View: Display the current inventory status for all products.
Inventory Detail View: Show the inventory details for a specific product.
Stock Update View (Webhook Integration): Handle incoming stock update data from the POS webhook.

Sale Views:

Sale List View: Display a list of sales transactions.
Sale Detail View: Show details of a specific sale transaction.
Create Sale View: Record new sale transactions and update inventory accordingly.
Update Sale View: Modify existing sale transaction details (e.g., for refunds or corrections).
Delete Sale View: Remove a sale transaction and adjust inventory quantities.

### Task 4: Testing
Write unit tests and integration tests for the API endpoints and webhook integration. Use libraries like Django's built-in TestCase and Django REST framework's APITestCase.

### Task 5: Error Handling
Implement proper error handling for various scenarios, such as validation errors, database errors, and authentication failures.

### Task 6: Bonus Task - Dockerization

Create a Dockerfile and Docker Compose configuration to containerize the Django application.