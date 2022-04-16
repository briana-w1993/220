from sales_person import *

class SalesForce:
    def __init__(self, sales_people):
        self.sales_people = sales_people

    def add_data(self, file_name):
        open(file_name, "r").readlines()


    def quota_report(self, quota):
        employee_info = []
        employee_id = SalesPerson.get_id(self.sales_people)
        name = SalesPerson.get_name(self.sales_people)
        sales = SalesPerson.total_sales(self.sales_people)
        employee_info.append(employee_id)
        employee_info.append(name)
        employee_info.append(sales)

        if SalesPerson.met_quota(self.sales_people, quota) == quota:
            return employee_info.append(True)
        else:
            return employee_info.append(False)






    def top_seller(self):
        employee_info = []
        sales = 0
        seller_info = []

        for total_sales in self.sales_people:
            employee_info.append(SalesPerson(total_sales[0], total_sales[1]))

        for top_seller in employee_info:
            if sales < top_seller.total_sales():
                seller_info.append(top_seller.total_sales())
            elif top_seller.total_sales() == sales:
                seller_info.append(top_seller)


    def individual_sales(self, employee_id):
        if self.sales_people[0] == employee_id:
            return self.sales_people[1]
        else:
            return None

    def get_sale_frequencies(self):
        sale_amount = {"sale amount:" }
        sales = 0
        for i in SalesPerson.total_sales(self.sales_people):
            sales = sales + i
        sale_amount.add(sales)
        return sale_amount















