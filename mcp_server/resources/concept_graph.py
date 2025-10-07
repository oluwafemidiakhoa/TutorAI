"""
Educational Concept Graph

This module defines and manages the knowledge concept graph, which
represents the relationships between different educational concepts.
"""

class ConceptGraph:
    """
    A class to represent and manage the educational concept graph.
    In a real application, this would be loaded from a database or a file.
    """
    def __init__(self):
        """
        Initializes the concept graph with some sample data.
        """
        self.graph = {
            "photosynthesis": {
                "dependencies": ["cells", "sunlight"],
                "unlocks": ["ecosystems"],
            },
            "cells": {
                "dependencies": [],
                "unlocks": ["photosynthesis", "respiration"],
            },
            "sunlight": {
                "dependencies": [],
                "unlocks": ["photosynthesis"],
            },
            "ecosystems": {
                "dependencies": ["photosynthesis"],
                "unlocks": [],
            },
        }

    def get_concept_details(self, concept_name: str) -> dict:
        """
        Retrieves details for a given concept.

        Args:
            concept_name: The name of the concept to retrieve.

        Returns:
            A dictionary containing the concept's details, or None if not found.
        """
        return self.graph.get(concept_name.lower())

# Create a single instance of the concept graph to be used by other modules
concept_graph_instance = ConceptGraph()