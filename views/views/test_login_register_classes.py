import unittest
from classes.login_register_classes import *


class TrekkingData(unittest.TestCase):
    """ Performs testing of five different functions."""
    admin_classes = AdminClasses()
    peak_classes = PeakClasses()
    permit_classes=PermitClasses()

    def test_change_password1(self):
        result = self.admin_classes.change_password('ram123', 'ram', 'ram')
        self.assertIs(result, True)

    def test_change_password2(self):
        result = self.admin_classes.change_password('', 'ram', 'ram123')
        self.assertIs(result, False)

    def test_delete_employee1(self):
        result = self.admin_classes.delete_employee(1)
        self.assertIs(result, True)

    def test_delete_employee2(self):
        result = self.admin_classes.delete_employee("")
        self.assertIs(result, False)

    def test_update_employee_detail1(self):
        result = self.admin_classes.delete_employee(1)
        self.assertIs(result, True)

    def test_update_employee_detail2(self):
        result = self.admin_classes.delete_employee("")
        self.assertIs(result, False)

    def test_delete_peak_detail1(self):
        result = self.peak_classes.delete_peak_detail(1)
        self.assertIs(result, True)

    def test_delete_peak_detail2(self):
        result = self.peak_classes.delete_peak_detail("")
        self.assertIs(result, False)

    def test_add_bill1(self):
        result = self.permit_classes.add_bill(1,'2000-09-09',1,'sanjiv','1234','ram','4321',1234)
        self.assertIs(result, True)

    def test_add_bill2(self):
        result = self.permit_classes.add_bill('','2000-09-09','1','sanjiv','1234','ram','4321',1234)
        self.assertIs(result, False)


if __name__ == "__main__":
    unittest.main()