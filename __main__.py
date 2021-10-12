import ast
from collections import deque
import re


# 나중에 dfs로 변경
def is_recursive(ast_tree):
    """ Returns
    Args:
        tree (ast.Module): ast tree

    Returns:
        bool: return recursive or not
    """
    for child in ast.iter_child_nodes(ast_tree):
        if isinstance(child, ast.FunctionDef):
            function_name = child.name # function name
            for c in ast.iter_child_nodes(child):
                if ('Call(func=Name(id=\'' + function_name) in ast.dump(c):
                    return True
    return False

# binary search를 사용하는지 확인


# import한 라이브러리를 알 수 있음
# 수정 => body 안에서 타고 내려갈 수 있도록
# ast_tree.dump()한 결과들만 알 수 있도록 되어 있음
# 이거 수정해야 함
def get_libraries(code):
    code = code.split()
    libraries = []
    import_pattern = re.compile('name=[a-z\']+')
    import_from_pattern = re.compile('module=[a-z\']+')

    for i in range(len(code)):
        if code[i][:-1] == 'Import':
            libraries.append(import_pattern.search(code[i+2]).group()[6:-1])
        elif code[i][:-1] == 'ImportFrom':
            libraries.append(import_pattern.search(code[i+3]).group()[6:-1] + ' from ' + import_from_pattern.search(code[i+1]).group()[8:-1])

    return libraries

# list, dictionary, set, deque
# queue 1. Collection 모듈의 deque, 2. queue 모듈의 Queue
# flattening한 ast_tree필요 -> ast.dump(ast_tree)
def get_data_structure(ast_tree):
    return_list = []

    t = ast.dump(ast_tree)
    # print(t)

    # count set
    if 'Call(func=Name(id=\'set\'' in t:
        return_list.append(('set', t.count('Call(func=Name(id=\'set\'')))
    
    # count deque
    if 'value=Call(func=Name(id=\'deque\'' in t:
        return_list.append(('deque', t.count('value=Call(func=Name(id=\'deque\'')))
    
    # count list
    value = 0
    value += t.count('Call(func=Name(id=\'list\'')
    value += t.count('value=List')

    if value:
        return_list.append(('list', value))
    
    value = 0
    value += t.count('value=Dict')
    value += t.count('Call(func=Name(id=\'dict\'')

    if value:
        return_list.append(('dictionary', value))    


    return return_list

# binary search를 사용하고 있는지 검사
# ast.dump(ast_tree)
def is_bisect(dump_ast_tree):
    if 'Call(func=Name(id=\'bisect_left\'' in dump_ast_tree or 'Call(func=Name(id=\'bisect_right\'' in dump_ast_tree:
        return True
    return False

def main(code):
    ast_tree = ast.parse(code)
    
    print("<recursion>")
    print(is_recursive(ast_tree))

    print("<data structure>")
    print(get_data_structure(ast_tree))

    print("<binary search>")
    print(is_bisect(ast.dump(ast_tree)))

# binary search
# 중첩 for문
if __name__ == "__main__":

    f = read_file('./test/test_recursion.py') # read code
    main(f)