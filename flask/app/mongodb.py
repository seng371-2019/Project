def FromMongo(query, limit=250, cursor=None):
    cursor = int(cursor) if cursor else 0

    results = mongo.db.books.find(skip=cursor, limit=10) # Perform some search on data
    data = builtin_list(map(from_mongo, results))

    return (data)
