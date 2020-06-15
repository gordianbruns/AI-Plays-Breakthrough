''' File:    node.py
 *  Purpose: Represents a tree for the game breakthrough
 *
 *  Note: Contains Node <class>
 *  Class-functions: getters and setters, some helper functions, evasive, conqueror, balanced, rusher,
 *                   calculate_utility
 '''

import random
import math


class Node:
    def __init__(self, environment_state):
        self.state = environment_state
        self.children = []
        self.depth = 0
        self.utility_estimate = 0.0

    def get_state(self):
        return self.state

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def add_child(self, node):
        self.children.append(node)

    def get_utility(self):
        return self.utility_estimate

    def set_utility(self, utility):
        self.utility_estimate = utility

    def evasive(self):  # strategy1
        if self.state.get_turn() == 0:
            utility = len(self.state.get_black_pawns()) + random.uniform(0, 1)
        else:
            utility = len(self.state.get_white_pawns()) + random.uniform(0, 1)
        return utility

    def conqueror(self):    # strategy2
        if self.state.get_turn() == 0:
            utility = (0 - len(self.state.get_white_pawns())) + random.uniform(0, 1)
        else:
            utility = (0 - len(self.state.get_black_pawns())) + random.uniform(0, 1)
        return utility

    def balanced(self): # strategy3
        if self.state.get_turn() == 0:
            utility = len(self.state.get_black_pawns()) - len(self.state.get_white_pawns()) + random.uniform(0, 1)
        else:
            utility = len(self.state.get_white_pawns()) - len(self.state.get_black_pawns()) + random.uniform(0, 1)
        return utility

    def _distance(self):  # helper function for rusher
        distance = 100000
        if self.state.get_turn() == 0:
            for pawn in self.state.get_black_pawns():
                if pawn[0] < distance:
                    distance = pawn[0]
        else:
            for pawn in self.state.get_white_pawns():
                if (self.state.get_rows() - pawn[0] - 1) < distance:
                    distance = self.state.get_rows() - pawn[0] - 1
        return distance

    def rusher(self):   # strategy4
        if self.state.get_turn() == 0:
            utility = len(self.state.get_black_pawns()) - len(self.state.get_white_pawns()) - self._distance() + \
                      random.uniform(0, 1)
        else:
            utility = len(self.state.get_white_pawns()) - len(self.state.get_black_pawns()) - self._distance() + \
                      random.uniform(0, 1)
        return utility

    def calculate_utility(self):  # does the main work for minimax (in main.py)
        maximum2 = None
        '''Gives a node a very high or very low utility value, if the player or the opponent is close to finishing'''
        if self.state.get_terminal():
            if self.state.get_terminal() == 1:
                if self.depth == 1:
                    if self.state.get_turn():  # actually whites turn
                        self.utility_estimate = 100001
                    else:
                        self.utility_estimate = -100000
                elif self.depth == 2:
                    if self.state.get_turn():  # actually blacks turn
                        self.utility_estimate = -100000
                    else:
                        self.utility_estimate = 100001
                elif self.depth == 3:
                    if self.state.get_turn():  # actually whites turn
                        self.utility_estimate = 50000
                    else:
                        self.utility_estimate = -50000
            if self.state.get_terminal() == 2:
                if self.depth == 1:
                    if self.state.get_turn():  # actually whites turn
                        self.utility_estimate = -100000
                    else:
                        self.utility_estimate = 100001
                elif self.depth == 2:
                    if self.state.get_turn():  # actually blacks turn
                        self.utility_estimate = 100001
                    else:
                        self.utility_estimate = -100000
                elif self.depth == 3:
                    if self.state.get_turn():  # actually whites turn
                        self.utility_estimate = -50000
                    else:
                        self.utility_estimate = 50000
            return
        '''end of implementation of defence and finish automation'''
        if self.depth == 2:
            maximum1 = Node(self.state)
            maximum1.utility_estimate = -math.inf
            for child in self.children:
                if child.utility_estimate > maximum1.utility_estimate:
                    maximum1 = child
            self.utility_estimate = maximum1.utility_estimate  # maximum of depth 3 children
        elif self.depth == 1:
            minimum = Node(self.state)
            minimum.utility_estimate = math.inf
            for child in self.children:
                if child.utility_estimate < minimum.utility_estimate:
                    minimum = child
            self.utility_estimate = minimum.utility_estimate  # minimum of depth 2 children
        elif self.depth == 0:
            maximum2 = Node(self.state)
            maximum2.utility_estimate = -math.inf
            for child in self.children:
                if child.utility_estimate > maximum2.utility_estimate:
                    maximum2 = child
            self.utility_estimate = maximum2.utility_estimate  # maximum of depth 1 children
        return maximum2
