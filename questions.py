"""
Module for getting quusitons from json
"""
import json

def get_quetions(name):
    """
    Method for getting questions from json
    """
    file = open(name, encoding="utf8")
    data = json.load(file)
    return data
