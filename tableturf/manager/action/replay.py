from controller import Controller
from logger import logger
from tableturf.manager.action import util


def move_replay_cursor_marco(target: int, current: int) -> str:
    logger.debug(f'action.move_replay_cursor_marco: target={target}, current={current}')
    buttons = []
    if target > current:
        buttons += [Controller.Button.DPAD_LEFT]
    elif target < current:
        buttons += [Controller.Button.DPAD_RIGHT]
    return util.buttons_to_marco(buttons)
