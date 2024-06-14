from app.desing_patterns.creational_patterns.singleton.database_singleton import DatabaseSingleton


async def post_register_action(id, method, path, status_code):

    return await DatabaseSingleton.post_register_action(id, method, path, status_code)
