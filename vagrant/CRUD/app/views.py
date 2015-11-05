from app import app, db, models
from sqlalchemy.sql import func, desc

def CustomerList():
    customer = models.Customer
    return customer.query.order_by(customer.account_name).group_by(customer.account_name).having(func.max(customer.renewal_date)).all()

def CustomerCountryView():
    customer = models.Customer
    country = models.CustomerCodes
    return customer.query.order_by(customer.account_name).group_by\
    (customer.account_name).having(func.max(customer.renewal_date)).\
    join(country, customer.country_code == country.CODE).\
    add_columns(customer.account_name, customer.customer_name, customer.account_id, customer.CustomerNote, country.COUNTRY, country.SupportRegion, customer.renewal_date, customer.contract_type, customer.CCGroup).all()

def CustomerCountryPages(page):
    customer = models.Customer
    country = models.CustomerCodes
    return customer.query.order_by(customer.account_name).group_by\
    (customer.account_name).having(func.max(customer.renewal_date)).\
    join(country, customer.country_code == country.CODE).\
    add_columns(customer.account_name, customer.customer_name, customer.account_id, customer.CustomerNote, country.COUNTRY, country.SupportRegion, customer.renewal_date, customer.contract_type, customer.CCGroup).paginate(page, 50, False)
