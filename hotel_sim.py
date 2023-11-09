import sys
import json
import argparse

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
    def check_location(self):
        """Taliyah's method
        
        """
        pass

    def check_budget(self):
        """Jeni's method
        checks if user's budget is withing range of possible hotel options.
        """
        pass

    def check_date(self):
        """Kassia's method
        """
        pass
    
    def find_intersection(self, user_dict, file_dict):
        """Samira's method. Takes a dictionary made from the user's preferences
        dictionary made earlier and a dictionary from the json file. Finds
        the best hotel that matches the user's specified preferences from 
        earlier.
        
        Args:
            user_dict (dict): Dictionary of all the user's answers for each
            question asked earlier, has their preference in hotels.
            file_dict (dict): Dictionary of all hotels and their details from
            an external file.
        
        Returns:
            best_hotel (dict key): Name of the best hotel found from 
            intersection
        """
        best_hotel = None
        num_intersections = 0
        
        for hotel_name, hotel_details in file_dict.items():
            intersection = user_dict.intersection(hotel_details)
            if len(intersection) > num_intersections:
                num_intersections = len(intersection)
                best_hotel = hotel_name
        return best_hotel

def read_file():
    """Sathya's function
    """
    pass

def main():
    """Finds the the hotel that matches the user preferences based on 
    the user's input using the data from the specificed file.
    """
    
    pass

if __name__ == '__main__':
    main()
