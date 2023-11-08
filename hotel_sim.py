import sys
import json
import argparse
import numpy
import pandas 

"""A hotel booking simulator, that takes in user input and returns
the  best hotel for their needs. """
class Hotel:
   
    def __init__(self, name):
         
        """creates name attribute to store name as argument.

        Args: 
        name (str): the user's name
        
        Side Effects:
        Creates 'name' attribute.
    
        """
        self.name = name
    def user_input(self):
        """this would be a method to get user input, pls add on
        
        """
        pass

    def check_budget(self):
        """Jeni's method
        checks if user's budget is withing range of possible hotel options.
        """
        pass

    def check_date(self):
        pass
    
    def find_match(self):
        """Samira's method. 
        """
        pass

def main():
    """Finds the the hotel that matches the user preferences based on 
    the user's input using the data from the specificed file.
    
    """
    pass

if __name__ == '__main__':
    main()
