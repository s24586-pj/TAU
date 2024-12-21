from payment_service import PaymentService
from inventory_service import InventoryService
from notification_service import NotificationService

class OrderService:
    """"
    Klasa order service tworzy konstruktor zlozony z mocków PaymentService,InventoryService,NotificationService
    oraz osobną funkcje place_order(zwraca true/false w zaleznosci czy zamowienie jest porpawne)
    która odpowiada za składanie zamówień.
    Idealny wypadek:Tworzenie konstruktora->place_order(Produkt dostępny->poprawna zapłata->powiadomeinie usera)
    """
    def __init__(self, payment_service: PaymentService, inventory_service: InventoryService, notification_service: NotificationService):
        self.payment_service = payment_service
        self.inventory_service = inventory_service
        self.notification_service = notification_service

    def place_order(self, user_id: str, product_id: str) -> bool:
        if not user_id or not product_id:
            return False

        try:
            if not self.inventory_service.is_product_available(product_id):
                self.notification_service.notify_user(user_id, "Product is not available.")
                return False
        except Exception as e:
            self.notification_service.notify_user(user_id, "Error checking product availability.")
            return False

        try:
            payment_success = self.payment_service.process_payment(user_id, product_id)
        except Exception as e:
            self.notification_service.notify_user(user_id, "Payment failed.")
            return False

        if not payment_success:
            self.notification_service.notify_user(user_id, "Payment failed.")
            return False

        try:
            self.notification_service.notify_user(user_id, "Order placed successfully.")
        except Exception as e:
            self.notification_service.notify_user(user_id, "Error sending order confirmation.")
            return False

        return True


