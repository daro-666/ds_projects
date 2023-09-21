from classes.customer import Customer
from datetime import datetime, timedelta
from faker import Faker
import random
import numpy as np
import pandas as pd


mu_normal    = 1.6482222222222223
sigma_normal = 0.4540737638126464
mu_peak      = 2.3866666666666663
sigma_peak   = 0.41334229380968485

hop_chance   = 0.5352791768909552

f = Faker()


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """


    def __init__(self, name: str, tprob: pd.DataFrame, customers=[], datetime=datetime(2023, 1, 1, 7, 0, 0)):
        """initialize attribites of a new supermarket instance
        """
        
        self.name = name
        self.customers = customers
        self.datetime = datetime
        self.tprob = tprob


    def __repr__(self):
        return f"Supermarket: {self.name}, # of customers: {len(self.customers)}, at: {self.get_time()}"


    def get_time(self):
        """current time in HH:MM:SS format
        """
        
        timestr = self.datetime.time().strftime("%H:%M:%S")
        return timestr


    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        
        return [print(f"{self.get_time()},{customer}") for customer in self.customers if customer.get_moved()]


    def next_minute(self) -> None:
        """propagates all customers to the next state.
        """
        
        # move time forward 1 min
        self.datetime = self.datetime + timedelta(minutes=1)
        
        # switch customer generation between peak and normal hours
        if self.datetime.time().hour == 8 or self.datetime.time().hour == 19: 
            for _ in range(round(np.random.normal(mu_peak, sigma_peak, 1)[0])):
                self.add_new_customers()
        else:
            for _ in range(round(np.random.normal(mu_normal, sigma_normal, 1)[0])):
                self.add_new_customers()

        # handle customer state changes 
        for customer in self.customers:
            if customer.location == "entrance":
                customer.enter()
                customer.set_moved(True)
            else:  
                if random.random() < hop_chance:
                    customer.next_state(self.tprob)
                    customer.set_moved(True)
                else:
                    customer.set_moved(False)
        
        
    def add_new_customers(self) -> None:
        """creates new customers with random name.
        """
        
        customer = Customer(f.name())
        self.customers.append(customer)
        #print(f"{self.get_time()}, {customer.name}, ENTERED")
        

    def remove_churned_customers(self) -> None:
        """removes every customer that is not active.
        """
        
        self.customers = [customer for customer in self.customers if customer.is_active() == True]

        
        # did not work
        """ for i, customer in enumerate(self.customers):
            if not customer.is_active():
                #print(f"{self.get_time()}, {customer.name}, LEFT")
                self.customers.pop(i) """