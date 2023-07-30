from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.hpModel import HpModel
from schemas.hpSchema import hpData


class HpDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

# Function to get list all posts
    async def get_hp_data(self) -> HpModel:
        query = select(HpModel)
        result = await self.db_session.execute(query)
        curr = result.scalar()
        if curr:
            return curr
        else:
            raise Exception(f'No row entry found - db is empty!')

# Function to add a new post to the database
    async def create_hp_data(self, hpData: hpData) -> HpModel:
        new_hp_data = HpModel(**hpData.model_dump())
        self.db_session.add(new_hp_data)
        await self.db_session.commit()
        self.db_session.refresh(new_hp_data)
        return new_hp_data
