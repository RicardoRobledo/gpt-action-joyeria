from ..repositories import user_action_repository


async def post_register_action(id, method, path, status_code):

    return await user_action_repository.post_register_action(id, method, path, status_code)
