from fastapi import APIRouter, HTTPException, status, Depends
from dependencies.hpDependencies import get_hp_dal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from controllers.hpController import getHomepageData, createHpData
from dal.hpRepository import HpDAL
from schemas.hpSchema import hpData

hpRouter = APIRouter(prefix="/api")


@hpRouter.get("/get_hp_data")
async def get_hp_data(hpDal: HpDAL = Depends(get_hp_dal)):
    try:
        homepageData = await getHomepageData(hpDal)
        response = {"res": "OK", "data": homepageData}
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@hpRouter.post("/create_hp_data")
async def create_hp_data(homepageData: hpData, hpDal: HpDAL = Depends(get_hp_dal)):
    try:
        newHpData = await createHpData(homepageData, hpDal)
        response = {"res": "OK", "data": newHpData}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(response))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))
