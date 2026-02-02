def query_to_dict(query):
    """
    Transforma el registro actual de un QSqlQuery en un diccionario.
    No necesita 'self', así que se puede usar en cualquier parte.
    """
    record = query.record()
    return {record.fieldName(i): query.value(i) for i in range(record.count())}

def query_to_list(query):
    # Ejecuta la query y devuelve una lista con todos los registros como diccionario.
    resultados = []
    # No hacemos query.exec() aquí porque ya debería venir ejecutada
    while query.next():
        resultados.append(query_to_dict(query))
    return resultados