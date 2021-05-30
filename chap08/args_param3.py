def concatenate(*args):
    result = ''
    result += '・'.join(args)
    return result


print(concatenate('[', ']', '鈴木', 'エルメシア', '富士子'))  # [鈴木・エルメシア・富士子]
