from typing import List, Optional
from models.postModel import PostModel
from dal.postsRepository import PostDAL
from schemas.postSchema import NewPost, UpdatePost

# Function to get list of all posts


async def getAllPosts(post_dal: PostDAL) -> List[PostModel]:
    return await post_dal.get_all_posts()

# Function to get a post by id


async def getPostById(post_id: int, post_dal: PostDAL) -> PostModel:
    return await post_dal.get_post_by_id(post_id)

# Function to add a new post to the db


async def createPost(post: NewPost, post_dal: PostDAL) -> PostModel:
    return await post_dal.create_post(post)

# Function to update details of the post


async def updatePostById(post_id: int, post: Optional[UpdatePost], post_dal: PostDAL):
    await post_dal.update_post_by_id(post_id, post)

# Function to delete a post from the db


async def deletePostById(post_id: int, post_dal: PostDAL):
    await post_dal.delete_post_by_id(post_id)
