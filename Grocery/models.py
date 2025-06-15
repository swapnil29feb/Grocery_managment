from Grocery import db
from datetime import datetime


# models.py
class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_admin = db.Column(db.Boolean, default=False)
    
    addresses = db.relationship('Address', back_populates='user', cascade="all, delete-orphan")
    cart = db.relationship('Cart', back_populates='user', cascade="all, delete-orphan")
    orders = db.relationship(
        'Orders',
        back_populates='user',
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    
class Address(db.Model):
    __tablename__ = 'address'
    
    address_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address1 = db.Column(db.String(255), nullable=False)
    address2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    
    user = db.relationship('Users', back_populates='addresses')
    
    def __repr__(self):
        return f'<Address {self.address_id} for User {self.user_id}>'

  
class Categories(db.Model):
    __tablename__ = 'categories'
    
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    
    products = db.relationship(
        'Products',
        back_populates='category',
        cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Category {self.name}>'


class Products(db.Model):
    __tablename__ = 'products'
    
    product_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    category = db.relationship('Categories', back_populates='products')
    inventory = db.relationship('Inventory', back_populates='product', uselist=False, cascade="all, delete-orphan")


class Inventory(db.Model):
    __tablename__ = 'inventory'
    
    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    product = db.relationship('Products', back_populates='inventory')
    
    def __repr__(self):
        return f'<Inventory {self.inventory_id} for Product {self.product_id}>'
    

class Cart(db.Model):
    __tablename__ = 'cart'
    
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    user = db.relationship('Users', back_populates='carts')
    items = db.relationship(
        'CartItems',
        back_populates='cart',
        cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Cart {self.cart_id} for User {self.user_id}>'
    

class Cart_items(db.Model):
    __tablename__ = 'cart_items'
    
    cart_item_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Products')  # optional: backref='cart_items'
    
    def __repr__(self):
        return f'<CartItem {self.cart_item_id} in Cart {self.cart_id}>'
    
    
class Orders(db.Model):
    __tablename__ = 'orders'
    
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False) 
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    
    order_items = db.relationship(
        'OrderItems',
        back_populates='order',
        cascade="all, delete-orphan")
    payment = db.relationship(
        'Payment',
        back_populates='order',
        uselist=False,
        cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return f'<Order {self.order_id} for User {self.user_id}>'
    

class Orderitems(db.Model):
    __tablename__ = 'order_items'
    
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    order = db.relationship('Orders', back_populates='order_items')
    product = db.relationship('Products')  # optional: backref='order_items'
    
    def __repr__(self):
        return f'<OrderItem {self.order_item_id} in Order {self.order_id}>'
    
    
class Payment(db.Model):
    __tablename__ = 'payments'
    
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    payment_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    
    order = db.relationship('Orders', back_populates='payment')
    
    def __repr__(self):
        return f'<Payment {self.payment_id} for Order {self.order_id}>'