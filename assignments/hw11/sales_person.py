class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        return self.sales.append(sale)

    def total_sales(self):
        total = 0
        sales_list = self.sales
        for i in sales_list:
            total = total + i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales > SalesPerson.total_sales(self):
            return -1
        else:
            return 1

    def __str__(self):
        return self.employee_id, self.name, self.total_sales()

