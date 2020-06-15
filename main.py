''' File:    main.py
 *  Purpose: Play a game of Breakthrough
 *
 *  Input:   rows, columns, rows_of_pawns, whites_function, blacks_function
 *  Output:  Solved maze, number of expanded node, and cost of the path
 *
 *  Usage: python main.py [rows] [columns] [rows_of_pawns] [whites_function] [blacks_function]
 *
 *  Note:  whites_function and blacks_function = {evasive, conqueror, balanced, rusher}
           rows and columns >= 1
           0 < rows_of_pawns <= rows // 2
 '''

import sys
import copy
from environmentState import EnvironmentState
from node import Node


def main(argv):
    if len(sys.argv) != 6:
        print("Correct usage: python main.py [rows]<int >= 1> [columns]<int >= 1> "
              "[rows_of_pawns]<int >= 1 and <= rows // 2> [whites_function] [blacks_function]")
        exit(0)
    rows = int(sys.argv[1])
    if rows < 1:
        print("Correct usage: python main.py [rows]<int >= 1> [columns]<int >= 1> "
              "[rows_of_pawns]<int >= 1 and <= rows // 2> [whites_function] [blacks_function]")
        exit(0)
    columns = int(sys.argv[2])
    if columns < 1:
        print("Correct usage: python main.py [rows]<int >= 1> [columns]<int >= 1> "
              "[rows_of_pawns]<int >= 1 and <= rows // 2> [whites_function] [blacks_function]")
        exit(0)
    pawns = int(sys.argv[3])
    if pawns < 1 or pawns >= rows // 2:
        print("Correct usage: python main.py [rows]<int >= 1> [columns]<int >= 1> "
              "[rows_of_pawns]<int >= 1 and <= rows // 2> [whites_function] [blacks_function]")
        exit(0)
    function1 = sys.argv[4]
    if function1 not in ["evasive", "conqueror", "balanced", "rusher"]:
        print("The function for white and the function for black must be in [evasive, conqueror, balanced, rusher]")
        exit(0)
    function2 = sys.argv[5]
    if function2 not in ["evasive", "conqueror", "balanced", "rusher"]:
        print("The function for white and the function for black must be in [evasive, conqueror, balanced, rusher]")
        exit(0)
    initial = initial_state(rows, columns, pawns)
    play_game(Node(initial), function1, function2, 0)
'''  main  '''


''' Function:    initial_state
 *  Purpose:     creates the initial state of the game
 *  Input args:  rows <int>, columns <int>, rows_of_pawns <int>
 *  Return val:  initial <object EnvironmentState>
'''
def initial_state(rows, columns, rows_of_pawns):
    initial = EnvironmentState(rows, columns, None, None)
    white_pawns = set()
    black_pawns = set()
    for i in range(rows_of_pawns):
        for j in range(columns):
            white_pawns.add((i, j))
            black_pawns.add((rows - (i + 1), j))
    initial.set_white_pawns(white_pawns)
    initial.set_black_pawns(black_pawns)
    return initial
'''  initial_state  '''


''' Function:    transition_function
 *  Purpose:     moves a pawn
 *  Input args:  environmentState <object EnvironmentState>, pawn_to_move <tuple <int, int>>,
                 goal_location <tuple <int, int>>
 *  Return val:  state <object EnvironmentState>
'''
def transition_function(environment_state, pawn_to_move, goal_location):
    state = copy.deepcopy(environment_state)
    if goal_location[0] < 0 or goal_location[0] > state.get_rows() - 1 or goal_location[1] < 0 or goal_location[1]\
            > state.get_columns() - 1 or goal_location == pawn_to_move:
        return None
    if state.get_turn():
        if pawn_to_move not in state.get_black_pawns() or goal_location in state.get_black_pawns():
            return None
        if goal_location[0] - pawn_to_move[0] != -1 or abs(goal_location[1] - pawn_to_move[1]) > 1:
            return None
        if goal_location in state.get_white_pawns():
            if goal_location[1] == pawn_to_move[1]:
                return None
            else:
                state.remove_white_pawn(goal_location)
        state.remove_black_pawn(pawn_to_move)
        state.add_black_pawn(goal_location)
    else:
        if pawn_to_move not in state.get_white_pawns() or goal_location in state.get_white_pawns():
            return None
        if goal_location[0] - pawn_to_move[0] != 1 or abs(goal_location[1] - pawn_to_move[1]) > 1:
            return None
        if goal_location in state.get_black_pawns():
            if goal_location[1] == pawn_to_move[1]:
                return None
            else:
                state.remove_black_pawn(goal_location)
        state.remove_white_pawn(pawn_to_move)
        state.add_white_pawn(goal_location)
    state.terminal_test()
    state.switch_turn()
    return state
'''  transition_function  '''


''' Function:    move_generator
 *  Purpose:     calculates all possible moves
 *  Input args:  state <object EnvironmentState>
 *  Return val:  moves <list with tuples <tuple <int, int>, tuple <int, int>>>
'''
def move_generator(state):
    moves = []
    if state.get_turn():
        for pawn in state.get_black_pawns():
            move1 = transition_function(state, pawn, (pawn[0] - 1, pawn[1] - 1))
            move2 = transition_function(state, pawn, (pawn[0] - 1, pawn[1]))
            move3 = transition_function(state, pawn, (pawn[0] - 1, pawn[1] + 1))
            if move1:
                moves.append((pawn, (pawn[0] - 1, pawn[1] - 1)))
            if move2:
                moves.append((pawn, (pawn[0] - 1, pawn[1])))
            if move3:
                moves.append((pawn, (pawn[0] - 1, pawn[1] + 1)))
    else:
        for pawn in state.get_white_pawns():
            move1 = transition_function(state, pawn, (pawn[0] + 1, pawn[1] - 1))
            move2 = transition_function(state, pawn, (pawn[0] + 1, pawn[1]))
            move3 = transition_function(state, pawn, (pawn[0] + 1, pawn[1] + 1))
            if move1:
                moves.append((pawn, (pawn[0] + 1, pawn[1] - 1)))
            if move2:
                moves.append((pawn, (pawn[0] + 1, pawn[1])))
            if move3:
                moves.append((pawn, (pawn[0] + 1, pawn[1] + 1)))
    return moves
'''  move_generator  '''


''' Function:    create_tree
 *  Purpose:     creates a tree of maximal depth 3 with the possible moves as children
 *  Input args:  environment_state <object EnvironmentState>
 *  Return val:  current_state <object EnvironmentState>, depth3 <list with <object Node>>
'''
def create_tree(environment_state):
    current_state = Node(environment_state)
    moves = move_generator(environment_state)
    depth3 = []
    for move in moves:
        child = transition_function(environment_state, move[0], move[1])
        child_node = Node(child)
        current_state.add_child(child_node)
        child_node.set_depth(1)
    for child in current_state.get_children():
        moves = move_generator(child.get_state())
        for move in moves:
            child2 = transition_function(child.get_state(), move[0], move[1])
            child2_node = Node(child2)
            child.add_child(child2_node)
            child2_node.set_depth(2)
        for child2 in child.get_children():
            moves = move_generator(child2.get_state())
            for move in moves:
                child3 = transition_function(child2.get_state(), move[0], move[1])
                child3_node = Node(child3)
                child2.add_child(child3_node)
                child3_node.set_depth(3)
                depth3.append(child3_node)
    return current_state, depth3
'''  create_tree  '''


''' Function:    minimax
 *  Purpose:     calculates utility values for each node and determines an action
 *  Input args:  node <object Node>
 *  Return val:  action <object Node>
'''
def minimax(node):
    if node is None:
        return
    for child in node.get_children():
        minimax(child)
    action = node.calculate_utility()
    if action:
        return action
'''  minimax  '''


''' Function:    play_game
 *  Purpose:     simulates an actual game
 *  Input args:  node <object Node>, function1 <String>, function2 <String>, count <int>
 *  Return val:  None
'''
def play_game(node, function1, function2, count):
    count += 1  # keeps track of how many moves have been taken
    node.get_state().display_state()
    node.get_state().terminal_test()
    if node.get_state().get_terminal() == 1:
        print("White won!")
        print(count)
        return
    elif node.get_state().get_terminal() == 2:
        print("Black won!")
        print(count)
        return
    tree, depth3 = create_tree(node.get_state())
    if tree.get_state().get_turn():
        if function2 == "evasive":
            for node in depth3:
                node.set_utility(node.evasive())
        elif function2 == "conqueror":
            for node in depth3:
                node.set_utility(node.conqueror())
        elif function2 == "balanced":
            for node in depth3:
                node.set_utility(node.balanced())
        elif function2 == "rusher":
            for node in depth3:
                node.set_utility(node.rusher())
    else:
        if function1 == "evasive":
            for node in depth3:
                node.set_utility(node.evasive())
        elif function1 == "conqueror":
            for node in depth3:
                node.set_utility(node.conqueror())
        elif function1 == "balanced":
            for node in depth3:
                node.set_utility(node.balanced())
        elif function1 == "rusher":
            for node in depth3:
                node.set_utility(node.rusher())
    next_node = minimax(tree)
    next_node.get_state().terminal_test()
    play_game(next_node, function1, function2, count)
'''  play_game  '''


if __name__ == '__main__':
    main(sys.argv[:5])
