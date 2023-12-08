"""
Module to load and return texts json
"""
import json

def get_texts():
    """
    Method to return json with texts
    """
    texts = {}
    if texts:
        return texts
    texts = load_text()
    return texts

def load_text():
    """
    Method to load json with texts
    """
    with open("texts.json", encoding= "utf8") as file:
        data = json.load(file)
        return data
