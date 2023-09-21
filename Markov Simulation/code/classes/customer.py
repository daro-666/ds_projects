import random
import numpy as np


arrival_choices = ['fruit', 'dairy', 'spices', 'drinks']
arrival_probs   = [0.3774345198119543,0.2875755540631296,0.18146406984553393,0.15352585627938214]
trans_choices   = ["checkout", "dairy", "drinks", "fruit", "spices"]


class Customer:
    """Customer for a supermarket Markov simulation
    """

    def __init__(self, name:str,  location="entrance", tm=trans_choices) -> None:
        """initialize a customer
        """
        
        self.name = name
        self.location = location
        self.tm = tm
        self.has_moved = True
    

    def __repr__(self) -> str:
        """prints out specifics about a customer in the format: (hh:mm:ss, name, location)
        """
        
        return f"{self.name},{self.get_location()}"


    def is_active(self) -> bool:
        """returns True while a customer is busy in any aisle and False if the customer is at checkout
        """

        if self.get_location() == "checkout":
            return False
        else:
            return True


    def next_state(self, tprob) -> None:
        """moves the customer to a new location according to the t-matrix and adds a random timedelta
        """

        self.set_location(np.random.choice(self.tm,  p=tprob.loc[self.get_location()]))


    def enter(self) -> None:
        """change location from entrance to a randomly selected aisle
        """

        self.set_location(np.random.choice(arrival_choices, p=arrival_probs))


    def get_moved(self) -> bool:
        """gets self.has_moved
        """
        
        return self.has_moved
    

    def set_moved(self, moved:bool) -> None:
        """sets self.has_moved
        """
        
        self.has_moved = moved


    def get_location(self) -> str:
        """gets self.location
        """

        return self.location
    
    def set_location(self, location:str) -> None:
        """sets self.location
        """

        self.location = location

