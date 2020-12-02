# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:59:29 2020

@author: lenovo
"""


from os import path, makedirs


class FilePreprocess:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_folder(self):
        # Creates a directory recursively.
        try:
            makedirs(self.file_path, mode=0o777, exist_ok=True)
        except PermissionError:
            return False
        return True