import unittest
from unittest.mock import MagicMock
from order_service import OrderService
from payment_service import PaymentService
from inventory_service import InventoryService
from notification_service import NotificationService

class TestOrderService(unittest.TestCase):
    def setUp(self):
        """"setUp metoda odpalana przed kazdym testem,ustawia srodowisko testowe,stworzenie orderService z mockami"""
        self.payment_service_mock = MagicMock(spec=PaymentService)
        self.inventory_service_mock = MagicMock(spec=InventoryService)
        self.notification_service_mock = MagicMock(spec=NotificationService)

        self.order_service = OrderService(
            self.payment_service_mock,
            self.inventory_service_mock,
            self.notification_service_mock
        )

    def test_place_order_successfully(self):
        """"
        Test poprawnego zamówienia z parametrami id_produktu:123,user_id:user1,
        ustawiamy na dostępny produkt:true i płatność:True
        result przechowywuje nam OGÓLNY wynik z metody,następnie przechodzimy przez sprawdzanie pojedynczych metod wraz
        z sprawdzeniem czy metoda została sprawdzona z odpowiednim parametryem,pozoste testy będą bardzo podobne do tego
        """
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = True
        self.payment_service_mock.process_payment.return_value = True

        result = self.order_service.place_order(user_id, product_id)

        self.assertTrue(result)

        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.payment_service_mock.process_payment.assert_called_with(user_id, product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Order placed successfully.")

    def test_place_order_product_not_available(self):
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = False

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Product is not available.")
        self.payment_service_mock.process_payment.assert_not_called()


    def test_is_product_available_and_payment_declined(self):
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = True
        self.payment_service_mock.process_payment.return_value = False

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.payment_service_mock.process_payment.assert_called_with(user_id, product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Payment failed.")


    def test_place_order_payment_failed(self):
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = True
        self.payment_service_mock.process_payment.return_value = False

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.payment_service_mock.process_payment.assert_called_with(user_id, product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Payment failed.")

    def test_place_order_payment_exception(self):
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = True
        self.payment_service_mock.process_payment.side_effect = Exception("Payment service error")

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.payment_service_mock.process_payment.assert_called_with(user_id, product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Payment failed.")

    def test_place_order_with_missing_user_id(self):
        product_id = "123"
        user_id = None

        self.inventory_service_mock.is_product_available.return_value = True

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_not_called()
        self.notification_service_mock.notify_user.assert_not_called()
        self.payment_service_mock.process_payment.assert_not_called()

    def test_place_order_with_missing_product_id(self):
        product_id = None
        user_id = '123'

        self.inventory_service_mock.is_product_available.return_value = False

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_not_called()
        self.notification_service_mock.notify_user.assert_not_called()
        self.payment_service_mock.process_payment.assert_not_called()

    def test_place_order_with_none_ids(self):
        product_id = None
        user_id = None

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_not_called()
        self.payment_service_mock.process_payment.assert_not_called()
        self.notification_service_mock.notify_user.assert_not_called()

    def test_place_order_payment_timeout(self):
        product_id = "123"
        user_id = "user1"

        self.inventory_service_mock.is_product_available.return_value = True
        self.payment_service_mock.process_payment.side_effect = TimeoutError("Payment timeout")

        result = self.order_service.place_order(user_id, product_id)

        self.assertFalse(result)
        self.inventory_service_mock.is_product_available.assert_called_with(product_id)
        self.payment_service_mock.process_payment.assert_called_with(user_id, product_id)
        self.notification_service_mock.notify_user.assert_called_with(user_id, "Payment failed.")


if __name__ == '__main__':
    unittest.main()
