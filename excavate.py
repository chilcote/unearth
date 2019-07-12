#!/usr/bin/python
"""This module can be used to return one or more artifacts about a Mac"""

import imp
import os


class Excavate(object):
    """Digging for artifacts"""

    def __init__(self):
        self.artifacts = {}
        self.module_dir = os.path.join(os.path.dirname(__file__), "artifacts")

    def get(self, categories):
        """Returns artifacts for the given list of categories"""
        for category in categories:
            filename = os.path.join(self.module_dir, category + ".py")
            if os.path.exists(filename):
                try:
                    module = imp.load_source(category, filename)
                    self.artifacts.update(module.fact())
                except (ImportError, AttributeError) as err:
                    print("Error %s in file %s" % (err, filename))
        return self.artifacts
