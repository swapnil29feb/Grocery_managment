# Grocery_managment
Grocery_managment using flask


🔄 Summary Diagram of Relationships
Parent	Child	Relationship Type
Users	Address	One-to-Many
Users	Cart	One-to-Many
Users	Orders	One-to-Many
Orders	OrderItems	One-to-Many
Cart	CartItems	One-to-Many
Categories	Products	One-to-Many
Products	Inventory	One-to-One
Orders	Payment	One-to-One
CartItems	Products	Many-to-One
OrderItems	Products	Many-to-One
