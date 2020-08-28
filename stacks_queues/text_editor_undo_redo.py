from enum import Enum


class Action:
    def __init__(self, action_type, char=None):
        self.action_type = action_type
        self.char = char

class ActionType(Enum):
    INSERT = 'INSERT'
    DELETE = 'DELETE'
    UNDO = 'UNDO'
    REDO = 'REDO'


def perform_actions(actions):
    undo_stack = []
    redo_stack = []
    progress_str = ''
    for action in actions:
        action_name = action[0]
        if action_name == 'INSERT':
            characters = action[1]
            first_char = ''
            if len(characters) > 0:
                first_char = characters[0]
            progress_str = insert_char(first_char, undo_stack, progress_str)
            redo_stack.clear()
        elif action_name == 'DELETE':
            progress_str = delete_char(undo_stack, progress_str)
            redo_stack.clear()
        elif action_name == 'UNDO':
            undo_action = undo_stack.pop()
            if undo_action.action_type == ActionType.INSERT:
                progress_str = insert_char(undo_action.char, redo_stack, progress_str)
            elif undo_action.action_type == ActionType.DELETE:
                progress_str = delete_char(redo_stack, progress_str)
        elif action_name == 'REDO':
            if len(redo_stack) != 0:
                redo_action = redo_stack.pop()
                if redo_action.action_type == ActionType.INSERT:
                    progress_str = insert_char(redo_action.char, undo_stack, progress_str)
                elif redo_action.action_type == ActionType.DELETE:
                    progress_str = delete_char(undo_stack, progress_str)
        else:
            raise Exception('unsupported action type')
    return progress_str



def insert_char(char, stack, progress_str):
    opposite_action = Action(ActionType.DELETE)
    stack.append(opposite_action)
    return progress_str + char


def delete_char(stack, progress_str):
    last_char = progress_str[-1:]
    opposite_action = Action(ActionType.INSERT, last_char)
    stack.append(opposite_action)
    return progress_str[:-1]