from app.desing_patterns.creational_patterns.singleton.database_singleton import DatabaseSingleton


async def get_training_document(topic_name:str, document_name:str):

    training_document = await DatabaseSingleton.get_training_document(topic_name, document_name)

    return training_document


async def get_workshop():
    
    workshop = await DatabaseSingleton.get_workshop()

    return workshop
