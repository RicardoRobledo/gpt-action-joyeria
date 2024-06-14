from ..repositories import training_repository


async def get_training_document(topic_name:str, document_name:str):

    training_document = await training_repository.get_training_document(topic_name, document_name)
    
    return training_document

async def get_workshop():

    course = await training_repository.get_workshop()
    
    return course
