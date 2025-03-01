# -*- coding: utf-8 -*-
"""part 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D3deEf8dKUsqQ_OmpZPsd7_rllp3VXPT
"""

from enum import Enum

# Define an Enum for Order Status
class OrderStatus(Enum):
    PROCESSING = "Processing"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"

class Customer:
    """Represents a customer who places delivery orders and tracks them."""

    def __init__(self, customer_id, name, email, phone, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    # Getter Methods
    def getCustomerID(self):
        return self.__customer_id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone

    def getAddress(self):
        return self.__address

    # Setter Methods
    def setEmail(self, email):
        self.__email = email

    def setPhone(self, phone):
        self.__phone = phone

    def setAddress(self, address):
        self.__address = address

class DeliveryOrder:
    """Represents a delivery request placed by a customer."""

    def __init__(self, order_id, customer_id, recipient_name, recipient_address, package_weight, status, tracking_number):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__recipient_name = recipient_name
        self.__recipient_address = recipient_address
        self.__package_weight = package_weight
        self.__status = status
        self.__tracking_number = tracking_number

    # Getter Methods
    def getOrderID(self):
        return self.__order_id

    def getCustomerID(self):
        return self.__customer_id

    def getRecipientName(self):
        return self.__recipient_name

    def getRecipientAddress(self):
        return self.__recipient_address

    def getPackageWeight(self):
        return self.__package_weight

    def getStatus(self):
        return self.__status

    def getTrackingNumber(self):
        return self.__tracking_number

    # Setter Methods
    def setStatus(self, status):
        if isinstance(status, OrderStatus):
            self.__status = status
        else:
            raise ValueError("Invalid order status")

class DeliveryStaff:
    """Represents delivery personnel responsible for handling packages."""

    def __init__(self, staff_id, name, phone):
        self.__staff_id = staff_id
        self.__name = name
        self.__phone = phone
        self.__assigned_orders = []

    # Getter Methods
    def getStaffID(self):
        return self.__staff_id

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def getAssignedOrders(self):
        return self.__assigned_orders

class Admin:
    """Represents an admin responsible for managing orders and delivery staff."""

    def __init__(self, admin_id, name, email, role):
        self.__admin_id = admin_id
        self.__name = name
        self.__email = email
        self.__role = role

    # Getter Methods
    def getAdminID(self):
        return self.__admin_id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getRole(self):
        return self.__role

# Use Objects to Generate the Delivery Note
customer1 = Customer("C101", "Salma Almansoori", "salma.almansoori@example.com", "0501234567", "45 Knowledge Ave, Dubai")
order1 = DeliveryOrder("O2025", customer1.getCustomerID(), "Salma Almansoori", "45 Knowledge Ave, Dubai", 7.0, OrderStatus.PROCESSING, "TRK2025001")
staff1 = DeliveryStaff("S201", "Mohamed Almansoori", "0500001234")
staff1.getAssignedOrders().append(order1)

# Print the Delivery Note
print("\n" + "="*40)
print(" " * 10 + "DELIVERY NOTE")
print("="*40)
print("Thank you for using our delivery service!")
print("Please print your delivery receipt and present it upon receiving your items.\n")

print("Recipient Details:")
print(f"Name: {order1.getRecipientName()}")
print(f"Contact: {customer1.getEmail()}")
print(f"Delivery Address: {order1.getRecipientAddress()}\n")

print("Delivery Information:")
print(f"Order Number: {order1.getOrderID()}")
print(f"Tracking Number: {order1.getTrackingNumber()}")
print(f"Delivery Date: January 25, 2025")
print(f"Delivery Method: Courier")
print(f"Package Weight: {order1.getPackageWeight()} kg\n")

print("Summary of Items Delivered:")
print(f"{'Item Code':<15}{'Description':<30}{'Quantity':<10}{'Unit Price (AED)':<20}{'Total Price (AED)':<20}")
print("-"*90)
print(f"{'ITM001':<15}{'Wireless Keyboard':<30}{'1':<10}{'100.00':<20}{'100.00':<20}")
print(f"{'ITM002':<15}{'Wireless Mouse & Pad':<30}{'1':<10}{'75.00':<20}{'75.00':<20}")
print(f"{'ITM003':<15}{'Laptop Cooling Pad':<30}{'1':<10}{'120.00':<20}{'120.00':<20}")
print(f"{'ITM004':<15}{'Camera Lock':<30}{'3':<10}{'15.00':<20}{'45.00':<20}")
print("-"*90)

subtotal = 270.00
taxes = 13.50
total = subtotal + taxes
print(f"\nSubtotal: AED {subtotal:.2f}")
print(f"Taxes and Fees: AED {taxes:.2f}")
print(f"Total Charges: AED {total:.2f}")
print("="*40)