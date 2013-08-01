"""
Generates a statistical model of the Python `if` statement, based on some
corpus of Python code we have.
"""

import glob, re, collections, lisp_parser


PARSED_IF_STMTS = 'data/ifprs/*.prs'


def if_asts ():
    """Gets all parsed `if` statements, return Python representation of parse
    tree.

    Specifically, the the `if` statements each have their own file, and they're
    represented as a lispy tree. This function just turns that lispy tree into
    a Python tree."""
    data = [file(f).read() for f in glob.glob(PARSED_IF_STMTS)]
    return map(lisp_parser.read, data)

def countup(trees):
    """Builds a histogram counting the times different features have occurred."""
    counts = collections.Counter()
    for tree in trees:
        walk(tree, counts)
    return counts

def walk(tree, counts):
    if not tree: return
    head = tree[0]
    if len(tree) == 1:
        entry = (head, None)
    else:
        for child in tree[1:]:
            entry = (head, head_of(child))
            print child
            print entry
            counts[entry] += 1
            walk(child, counts)

def head_of(tree):
    return tree[0] if isinstance(tree,list) else None

def lisp_to_python(text):
    text = text[1:].replace('(', '[').replace(')', ']')
    print text
    return re.sub('([_a-zA-Z]+)', r'"\1",', text)

if __name__ == '__main__':
    print countup(if_asts())
