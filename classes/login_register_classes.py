from tkinter import *
from classes.database_connection import *


class LoginRegisterClasses:
    """Performs tasks like passing query to perfom login related operation"""

    def __init__(self):
        self.my_connection = MyConnection()

    def check_username(self):
        qry = 'select username from registration'
        reg_email = self.my_connection.get_data(qry)
        return reg_email

    def registration(self, first_name, last_name, mobile_no, gender, date_of_birth, address, username, email,
                     password, confirm_password):
        qry = "insert into registration(first_name," \
              "last_name,mobile_no,gender,date_of_birth," \
              "address,username,email,password,confirm_password)" \
              " values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, mobile_no, gender, date_of_birth, address, username, email, password,
                  confirm_password)
        self.my_connection.iud(qry, values)
        return True

    def login(self, username, password):
        qry = "select * from registration where username=%s and password=%s"
        values = (username, password)

        data = self.my_connection.get_data_p(qry, values)
        length = len(data)
        return length

    def admin_or_user(self, username, password):
        qry = "select * from registration where username=%s and password=%s"
        values = (username, password)
        data = self.my_connection.get_data_p(qry, values)
        return data


class AdminClasses:
    """Performs tasks like passing query to perfom admin related operation"""

    def __init__(self):
        self.my_connection = MyConnection()

    def assign_role(self, type, username):
        try:
            if type == "" or username == "":
                return False
            qry = "update registration set type = %s where username = %s"
            values = (type, username)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def change_password(self, password, username, old_password):
        try:
            if password == "" or username == "" or old_password == "":
                return False
            qry = "update registration set password=%s where username=%s " \
                  "and password=%s"
            values = (password, username, old_password)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def employee_detail(self):
        qry = "select * from registration"
        data = self.my_connection.get_data(qry)
        return data

    def delete_employee(self, emp_id):
        try:
            if emp_id == "":
                return False
            qry = "delete from registration where emp_id=%s"
            values = (emp_id,)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def search_employee(self, option, value):
        qry = "select * from registration where" + " " + option \
              + " " + "LIKE '" + value + "' "

        data = self.my_connection.get_data(qry)
        return data


class PeakClasses:
    """Performs tasks like passing query to perfom peak related operation"""

    def __init__(self):
        self.my_connection = MyConnection()

    def add_peak_detail(self, peak_name, height, himalayan_range, district, caravan_route):
        qry = "insert into peak (peak_name, height, himalayan_range, district, caravan_route)" \
              " values(%s, %s, %s, %s, %s)"
        values = (peak_name, height, himalayan_range, district, caravan_route)
        self.my_connection.iud(qry, values)
        return True

    def peak_detail(self):
        qry = "select * from peak"
        data = self.my_connection.get_data(qry)
        return data

    def update_peak_detail(self, peak_name, height, himalayan_range, district, caravan_route, update_index):
        try:
            if peak_name == "" or height == "" or himalayan_range == "" or district == "" \
                    or caravan_route == "" or update_index == "":
                return False
            qry = "update peak set peak_name= %s, height= %s, himalayan_range= %s, district= %s, " \
                  "caravan_route= %s where peak_id= %s "
            values = (peak_name, height, himalayan_range, district, caravan_route, update_index)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def delete_peak_detail(self, update_index):
        try:
            if update_index == "":
                return False
            qry = "delete from peak where peak_id=%s"
            values = (update_index,)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def search_peak(self, option, value):
        qry = "select * from peak where" + " " + option \
              + " " + "LIKE '" + value + "' "

        data = self.my_connection.get_data(qry)
        return data


class PermitClasses:
    def __init__(self):
        self.my_connection = MyConnection()

    def add_permit(self, name_of_peak, height, climbing_period,
                   trekking_route, leader_name, leader_country,
                   leader_passport_no, leader_age, leader_sex,
                   member_name, member_country, member_passport_no,
                   member_age, member_sex, total_climber,
                   name_of_trekking_company, name_of_guide,
                   guide_reg, permit_date, permit_cost):

        if name_of_peak == "" or height == "" or climbing_period == "" \
                or trekking_route == "" or leader_name == "" or \
                leader_country == "" or leader_passport_no == "" \
                or leader_age == "" or leader_sex == "" or member_name \
                == "" or member_country == "" or member_passport_no == "" \
                or member_age == "" or member_sex == "" or \
                total_climber == "" or name_of_trekking_company == "" \
                or name_of_guide == "" or guide_reg == "" or \
                permit_date == "" or permit_cost == "":
            return False

        qry = "insert into climbing_permit(name_of_peak, height," \
              " climbing_period, trekking_route," \
              " leader_name, leader_country,leader_passport_no," \
              " leader_age, leader_sex," \
              " member_name, member_country, member_passport_no," \
              "member_age, member_sex," \
              " total_no_of_climbers, name_of_trekking_company," \
              " name_of_sardar_or_guide, sardar_or_guide_reg_no, permit_date, permit_cost) values(%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        value = (name_of_peak, height, climbing_period, trekking_route,
                 leader_name, leader_country,
                 leader_passport_no, leader_age, leader_sex,
                 member_name, member_country, member_passport_no,
                 member_age, member_sex, total_climber,
                 name_of_trekking_company, name_of_guide,
                 guide_reg, permit_date, permit_cost)

        self.my_connection.iud(qry, value)
        return True

    def permit_detail(self):
        qry = "select * from climbing_permit"
        data = self.my_connection.get_data(qry)
        return data

    def search_permit(self, option, value):
        qry = "select * from climbing_permit where" + " " + option \
              + " " + "LIKE '" + value + "' "

        data = self.my_connection.get_data(qry)
        return data

    def delete_permit(self, update_index):
        qry = "delete from climbing_permit where permit_no=%s"
        values = (update_index,)
        self.my_connection.iud(qry, values)
        return True

    def update_permit(self, name_of_peak, height, climbing_period,
                      trekking_route, leader_name, leader_country,
                      leader_passport_no, leader_age, leader_sex,
                      member_name, member_country, member_passport_no,
                      member_age, member_sex, total_climber,
                      name_of_trekking_company, name_of_guide,
                      guide_reg, permit_date, permit_cost, update_index):

        if name_of_peak == "" or height == "" or climbing_period == "" \
                or trekking_route == "" or leader_name == "" or \
                leader_country == "" or leader_passport_no == "" \
                or leader_age == "" or leader_sex == "" or member_name \
                == "" or member_country == "" or member_passport_no == "" \
                or member_age == "" or member_sex == "" or \
                total_climber == "" or name_of_trekking_company == "" \
                or name_of_guide == "" or guide_reg == "" or \
                permit_date == "" or permit_cost == "" or update_index == "":
            return False

        qry = "update climbing_permit set name_of_peak=%s, height=%s," \
              " climbing_period=%s, trekking_route=%s, leader_name=%s," \
              " leader_country=%s, leader_passport_no=%s, leader_age=%s," \
              " leader_sex=%s, member_name=%s, member_country=%s," \
              " member_passport_no=%s, member_age=%s, member_sex=%s, " \
              "total_no_of_climbers=%s, name_of_trekking_company=%s," \
              " name_of_sardar_or_guide=%s, sardar_or_guide_reg_no=%s," \
              " permit_date=%s permit_cost=%s where permit_no=%s"

        value = (name_of_peak, height, climbing_period, trekking_route,
                 leader_name, leader_country,
                 leader_passport_no, leader_age, leader_sex,
                 member_name, member_country, member_passport_no,
                 member_age, member_sex, total_climber,
                 name_of_trekking_company, name_of_guide,
                 guide_reg, permit_date, permit_cost, update_index)

        self.my_connection.iud(qry, value)
        return True

    def permit_detail_for_bill(self, update_index):
        qry = "select * from climbing_permit where permit_no=%s"
        values = (update_index,)
        data = self.my_connection.get_data_p(qry, values)
        return data

    def add_bill(self, permit_no, permit_date, bill_no, member_name, member_passport_no, leader_name,
                 leader_passport_no, permit_cost):
        try:
            if permit_no == "" or permit_date == "" or bill_no == "" or member_name == "" or \
                    member_passport_no == "" or leader_name == "" or leader_passport_no == "" or permit_cost == "":
                return False
            qry = "insert into bill(permit_no,permit_date,bill_no,member_name,member_passport_no,leader_name," \
                  "leader_passport_no,permit_cost) values(%s,%s,%s,%s,%s,%s,%s,%s) "
            values = (permit_no, permit_date, bill_no, member_name, member_passport_no,
                      leader_name, leader_passport_no, permit_cost)
            self.my_connection.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def show_bill(self):
        qry = "select * from bill"
        data = self.my_connection.get_data(qry)
        return data


if __name__ == "__main__":
    LoginRegisterClasses()
