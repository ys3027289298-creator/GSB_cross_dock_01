import json


def new_game():
    return {'events': {}, 'paused': False, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_18(state):
    event_id = 1
    if event_id in state['events']:
        return False
    state['events'][event_id] = {'status': 'scheduled'}
    return True

def bug_25(state):
    if state['paused']:
        return state['clock']
    state['clock'] += 1
    return state['clock']

def bug_2(state):
    return None

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    return [row for row in state['audit'] if row[0] == 'a']

def bug_23(state):
    return state['cap'] - state['used']

def bug_0(state):
    entry = ('process', 'dock-item')
    if entry in state['log']:
        return False
    state['log'].append(entry)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    target_slot = 1
    if target_slot <= state['used']:
        return False
    return True

def bug_30(state):
    snapshot = state['snapshot']
    try:
        if ('op', 'failed') in state['log']:
            raise RuntimeError('transaction step failed')
        return True
    except RuntimeError:
        state['value'] = snapshot
        return False

def bug_31(state):
    if state['settled']:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
