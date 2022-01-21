import difflib
import json

def colored(text, color):
    if color == "black":
        return "\033[1;30m" + text + "\033[0m"
    elif color == "blue":
        return "\033[1;34m" + text + "\033[0m"
    elif color == "cyan":
        return "\033[1;36m" + text + "\033[0m"
    elif color == "green":
        return "\033[1;32m" + text + "\033[0m"
    elif color in ["grey", "lightblack"]:
        return "\033[1;90m" + text + "\033[0m"
    elif color == "lightblue":
        return "\033[1;94m" + text + "\033[0m"
    elif color == "lightcyan":
        return "\033[1;96m" + text + "\033[0m"
    elif color == "lightgreen":
        return "\033[1;92m" + text + "\033[0m"
    elif color == "lightgrey":
        return "\033[0;37m" + text + "\033[0m"
    elif color == "lightmagenta":
        return "\033[1;95m" + text + "\033[0m"
    elif color == "lightred":
        return "\033[1;91m" + text + "\033[0m"
    elif color == "lightwhite":
        return "\033[1;97m" + text + "\033[0m"
    elif color == "lightyellow":
        return "\033[1;93m" + text + "\033[0m"
    elif color == "magenta":
        return "\033[1;35m" + text + "\033[0m"
    elif color == "red":
        return "\033[1;31m" + text + "\033[0m"
    elif color == "white":
        return "\033[1;37m" + text + "\033[0m"
    elif color == "yellow":
        return "\033[1;33m" + text + "\033[0m"
    else:
        return text

def print_diff(old, new):
    # Convert yo strings
    old = json.dumps(old, indent=4)
    new = json.dumps(new, indent=4)

    if old.splitlines() != new.splitlines():
        # Print the difference, removed text lines in red and added lines in green
        for line in difflib.unified_diff(new.splitlines(), old.splitlines(), lineterm=''):
            if line.startswith('-'):
                print(colored(line, 'red'), flush=True)
            elif line.startswith('+'):
                print(colored(line, 'green'), flush=True)
    else:
        print('No changes', flush=True)