def read(token_stream):
    found = False
    token = next(token_stream, None)
    
    if token == 8: # READ
        token = next(token_stream, None)
        if token == 20: # (
            if idlist(token_stream):
                token = next(token_stream, None)
                if token == 21: # )
                    found = True
    return found

def idlist(token_stream):
    found = False
    token = next(token_stream, None)
    
    if token == 22: # id
        found = True
        token = next(token_stream, None)
        
        while token == 14 and found: # ,
            token = next(token_stream, None)
            if token == 22: # id
                token = next(token_stream, None)
            else:
                found = False
    return found
