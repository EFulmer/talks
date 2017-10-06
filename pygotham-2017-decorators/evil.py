# -*- coding: utf-8 -*-
"""very bad thing"""
import ast

def rev_deco(func):
    """Calls func with arguments provided in reversed order."""
    def deco(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return deco

def mutate_functions(body):
    p = ast.parse(body)
    for thing in p.body:
        if isinstance(thing, ast.FunctionDef):
            thing.decorator_list.append()



# sketch:
# create AST (`p = ast.parse(body)`)
# walk AST, for each node: (`for node in p.walk():`)
    # if node is a function: `if isinstance($THING, ast.FunctionDef):`
        # append rev_deco to function's decorator_list (HOW?)
        # (`$THING.insert(0, $DECORATOR)`)
        # maybe like `Name(id='rev_deco', ctx=Load())`
# compile this altered AST

# ... later on
# create an import hook that does all this evil stuff

# ... even later
# probabilistically destroy the AST
