
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    text_info = (len(string), string.lower(), string.upper())
    return text_info

def is_contains(string, list_to_search):
    count_calls()
    list(list_to_search)
    print(string)
    new_list = [s.lower() for s in list_to_search ]
    # for i in list_to_search:
    #     print(i)
    if string.lower() in new_list:
        return True
    else:
        return False

print(string_info('weapon'))
print(is_contains('pAnda', ['PanDa', 'tiger', 'Dog']))
print(calls)