from typing import List
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.postModel import PostModel
from schemas.postSchema import NewPost, UpdatePost


class PostDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

# Function to get list all posts
    async def get_all_posts(self) -> List[PostModel]:
        query = select(PostModel).order_by(PostModel.id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

# Function to get post by id
    async def get_post_by_id(self, post_id: int) -> PostModel:
        post: PostModel = await self.db_session.get(PostModel, post_id)
        return post

# Function to add a new post to the database
    async def create_post(self, post: NewPost) -> PostModel:
        new_post = PostModel(**post.model_dump())
        self.db_session.add(new_post)
        await self.db_session.commit()
        self.db_session.refresh(new_post)
        return new_post

# Function to update details of the post
    async def update_post_by_id(self, post_id: int, post: UpdatePost):
        row = await self.get_post_by_id(post_id)
        if row:
            query = update(PostModel).where(
                PostModel.id == post_id).values(post.model_dump(exclude_none=True))
            query.execution_options(synchronize_session="fetch")
            await self.db_session.execute(query)
        else:
            raise Exception(f'No row entry found with id: {post_id}')

# Function to delete a post from the db

    async def delete_post_by_id(self, post_id: int):
        row = await self.get_post_by_id(post_id)
        if row:
            query = delete(PostModel).where(PostModel.id == post_id)
            await self.db_session.execute(query)
            await self.db_session.commit()
        else:
            raise Exception(f'No row entry found with id: {post_id}')
