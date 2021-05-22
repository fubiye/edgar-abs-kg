def get_query_value(url, param,next_parm):
    query = '&'+param+'='
    next_query = '&'+next_parm+'='
    return url[url.index(query)+len(query):url.index(next_query)]