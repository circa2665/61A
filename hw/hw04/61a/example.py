def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree < 1):
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(t):
    if is_leaf(t):
        return 1
    return sum([count_leaves(b) for b in branches(t)])

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    return sum([leaves(b) for b in branches(t)], [])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    return tree(label(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)
    
