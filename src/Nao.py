from search import Problem
from utils import *
import math 

def entropy_calc(choreography):
    # We keep track of the moves used in the choreography
    frequency_dict = {}
    for move in choreography:
        if move not in frequency_dict:
            # If absent initialize it to 1
            frequency_dict[move] = 1
        else:
            # If present update the value
            frequency_dict[move] += 1
    result = 0.0
    # Entropy as defined by Shannon
    for unique_move, frequency in frequency_dict.items():
        probability = frequency / len(choreography)
        # The log is negative so we used -=
        result -= probability * math.log(probability, 2)
    return result

class NaoProblem(Problem):
  def __init__(self, initial, goal, moves, previous_moves, avg_time): # avg_time, previous_moves
    super().__init__(initial, goal)
    self.available_moves = moves 
    self.previous_moves = previous_moves 
    self.avg_time = avg_time

  # Function that evaluates if a move is usable after a certain state
  def isValid(self, stateT, move_name, move):
    state = dict((key, value) for key, value in stateT)
    if state['remaining_time'] < move[0]:
      return False
    # Check preconditions
    if 'standing' in move[1]:
      if state['standing'] != move[1]['standing']:
        return False
        
    # Check if the move is different from the last two in the choreography
    ######### DA COMPLETARE #########
    return True

  def actions(self, state):
    valid_actions = []
    # We cycle trough the moves set and check each for usability from current state
    for move_name, move in self.available_moves.items():
        if self.isValid(state, move_name, move):
            # The moves that satisfy our condition are added to the result
            valid_actions.append(move_name)
    # We shuffle the result list to increase diversity in the final solution
    random.shuffle(valid_actions)
    return valid_actions

  def result(self, stateT, action):
    state = dict((key, value) for key, value in stateT)
    # We already checked the action in the actions function so they are valid
    nao_move = self.available_moves[action]
    # We used a util function to convert the state in a dictionary

    # We create a temp choreography, including past steps, to later calculate its entropy
    temp_choreography = [*self.previous_moves, *state['choreography'], action]
    # Now we calculate the entropy of the temp choreography using a util function
    temp_entropy = entropy_calc(temp_choreography)
    # We set the postcondition of this action
    if 'standing' in nao_move[2]:
        temp_standing = nao_move[2]['standing']
    else:
        # If the action don't modify the standing state we keep the last one
        temp_standing = state['standing']

    return (('choreography', (*state['choreography'], action)), ('standing', temp_standing), 
            ('remaining_time', state['remaining_time'] - nao_move[0]), 
            ('moves_done', state['moves_done'] + 1), ('entropy', temp_entropy))

  def goal_test(self, stateT):
    state = dict((key, value) for key, value in stateT)
    goal = dict((key, value) for key, value in self.goal)

    # Given a state, return True if state is a goal state or False, otherwise
    # We used a util function to convert the state in a dictionary

    # We create an interval to check if we filled the time slot for this step
    goal_remaining_time = goal['remaining_time']
    a = goal_remaining_time
    b = goal_remaining_time + 1

    # We check if all our condition are met
    # Check if we filled the time slot for this step
    time_constraint = (a <= state['remaining_time'] <= b)
    # Check if we chose enough moves for this step
    moves_done_constraint = (state['moves_done'] >= goal['moves_done'])
    # Check if we chose moves that are diverse enough
    entropy_constraint = (state['entropy'] >= goal['entropy'])
    # Check if we reached our goal standing state
    standing_constraint = (state['standing'] == goal['standing'])
    #print(f"standing {state['standing']} == {goal['standing']}  :  {standing_constraint}")
    print(time_constraint and moves_done_constraint and entropy_constraint and standing_constraint)
    return time_constraint and moves_done_constraint and entropy_constraint and standing_constraint

    # Heuristic function used in A* search
  def h(self, nodeT):
    state = dict((key, value) for key, value in nodeT.state)
    goal = dict((key, value) for key, value in self.goal)
    # We implemented a simple heuristic that estimates the cost to reach the goal
    # by multiplying the number of remaining moves to the avg_time of our moves set
    return (goal['moves_done'] - state['moves_done']) * self.avg_time
