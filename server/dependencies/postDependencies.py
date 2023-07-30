from config.db import async_session
from dal.postsRepository import PostDAL


async def get_post_dal():
    async with async_session() as session:
        async with session.begin():
            yield PostDAL(session)
