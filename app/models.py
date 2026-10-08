
from sqlalchemy import DateTime

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    role = Column(String(50), nullable=False, default="staff") # e.g., 'admin', 'user', 'staff'

class Product(Base):
    __tablename__ = "products"

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    sku = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, nullable=False,default=0)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    total_amount = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, default="pending") # e.g., 'pending', 'completed', 'cancelled'
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False,default=1)
    price = Column(Integer, nullable=False)  # Price at the time of order


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_method = Column(String(50), nullable=False)  # e.g., 'credit_card', 'paypal', 'cash'
    status = Column(String(50), nullable=False, default="pending")  # e.g., 'pending', 'completed', 'failed'
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    total_amount = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, default="pending")  # e.g., 'pending', 'completed', 'cancelled'
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Integer, nullable=False)  # Price at the time of purchase

class InventoryTransaction(Base):
    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity_change = Column(Integer, nullable=False)  # Positive for addition, negative for subtraction
    transaction_type = Column(String(50), nullable=False)  # e.g., 'purchase', 'sale', 'adjustment'
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(
        Integer,
        ForeignKey("tenants.id"),
        nullable=False
    )

    plan_id = Column(
        Integer,
        ForeignKey("subscription_plans.id"),
        nullable=False
    )

    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=False)

    status = Column(
        String(50),
        nullable=False,
        default="active"
    )

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    price = Column(Integer, nullable=False)

    duration_days = Column(Integer, nullable=False)  # Duration of the plan in days



#  Category
# 9. Supplier
# 10. Purchase
# 11. PurchaseItem
# 12. InventoryTransaction
# 13. Store / Branch
# 14. SubscriptionPlan
# 15. Subscription