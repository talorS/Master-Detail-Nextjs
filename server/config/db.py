from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

sqlite_db_name = "postsdb"
DATABASE_URL = f"mysql+asyncmy://root:talor115@localhost:3306/{sqlite_db_name}"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
