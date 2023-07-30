from fastapi import APIRouter, HTTPException, status, Response, Depends
from dependencies.postDependencies import get_post_dal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from controllers.postsController import getAllPosts, getPostById, createPost, updatePostById, deletePostById
from dal.postsRepository import PostDAL
from schemas.postSchema import NewPost, UpdatePost

postRouter = APIRouter(prefix="/api")


@postRouter.get("/get_posts")
async def get_all_posts(postDal: PostDAL = Depends(get_post_dal)):
    try:
        postsList = await getAllPosts(postDal)
        response = {"res": "OK", "data": postsList}
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@postRouter.get("/get_post/{id}")
async def get_post(id: int, postDal: PostDAL = Depends(get_post_dal)):
    try:
        post = await getPostById(id, postDal)
        response = {"res": "OK", "data": post}
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))


@postRouter.post("/create_post")
async def add_post(post: NewPost, postDal: PostDAL = Depends(get_post_dal)):
    try:
        newPost = await createPost(post, postDal)
        response = {"res": "OK", "data": newPost}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(response))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))


@postRouter.put("/update_post/{id}")
async def update_post(id: int, post: UpdatePost, postDal: PostDAL = Depends(get_post_dal)):
    try:
        await updatePostById(id, post, postDal)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))


@postRouter.delete("/delete_post/{id}")
async def delete_post(id: int, postDal: PostDAL = Depends(get_post_dal)):
    try:
        await deletePostById(id, postDal)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))
