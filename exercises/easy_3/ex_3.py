'Write a function that takes a short line of text and prints it within a box.'
import shutil
WIDTH = shutil.get_terminal_size().columns - 2

def split_str(_str: str):
    word_list = _str.split()
    split_list = []

    for word in word_list:
        if split_list and (len(split_list[-1] + word) < (WIDTH - 2)):
            split_list[-1] += " " + word
        else:
            split_list.append(word)
    return split_list

def print_header():
    print(f"+{'-'*(WIDTH)}+")
    print(f"|{' '*(WIDTH)}|")

def print_footer():
    print(f"|{' '*(WIDTH)}|")
    print(f"+{'-'*(WIDTH)}+")

def print_in_box(_str: str):
    sentence_list = split_str(_str)
    print_header()
    for string in sentence_list:
        print(f"|{string.center(WIDTH)}|")
    print_footer()

print_in_box(
    'Luke Skywalker has returned to '
    'his home planet of Tatooine in '
    'an attempt to rescue his '
    'friend Han Solo from the '
    'clutches of the vile gangster '
    'Jabba the Hutt. '
    'Little does Luke know that the '
    'GALACTIC EMPIRE has secretly '
    'begun construction on a new '
    'armored space station even '
    'more powerful than the first '
    'dreaded Death Star. '
    'When completed, this ultimate '
    'weapon will spell certain doom '
    'for the small band of rebels '
    'struggling to restore freedom '
    'to the galaxy...'
    )