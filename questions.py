"""
Module for getting quusitons from json
"""
import json

def get_quetions(name):
    """
    Method for getting questions from json
    """
    with open(name, encoding= "utf8") as file:
        data = json.load(file)
    return data
