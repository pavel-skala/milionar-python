"""
Module to open and return texts json
"""
import json

texts = {}

def get_texts():
    """
    Method to return json with texts
    """
    global texts
    if texts:
        return texts
    texts = open_text()
    return texts

def open_text():
    """
    Method to open json with texts
    """
    file = open("texts.json", encoding="utf8")
    return json.load(file)
