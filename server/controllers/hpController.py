from models.hpModel import HpModel
from dal.hpRepository import HpDAL
from schemas.hpSchema import hpData

# Function to get list of all posts


async def getHomepageData(hp_dal: HpDAL) -> HpModel:
    row = await hp_dal.get_hp_data()
    return HpModel(headline=row.headline)

# Function to add a new post to the db


async def createHpData(hpData: hpData, hp_dal: HpDAL) -> HpModel:
    return await hp_dal.create_hp_data(hpData)
