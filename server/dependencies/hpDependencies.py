from config.db import async_session
from dal.hpRepository import HpDAL


async def get_hp_dal():
    async with async_session() as session:
        async with session.begin():
            yield HpDAL(session)
