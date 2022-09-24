import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import dotenv_values
from NASA import NASABaseAPI, NASAImageAndVideoAPI


env = dotenv_values(".env")


app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url='/NASA/picture-of-the-day')


@app.get("/NASA/picture-of-the-day")
async def get_nasa_astronomy_picture_of_the_day():
    api=NASABaseAPI()
    return api.astronomy_picture_of_the_day()

@app.get("/NASA/image_and_video/search/{search_term}")
async def search_nasa_images_and_videos(search_term):
    api=NASAImageAndVideoAPI()
    return api.search(search_term=search_term)

@app.get("/NASA/image_and_video/search/im-feeling-lucky/{search_term}")
async def search_for_first_nasa_image_and_video(search_term):
    api=NASAImageAndVideoAPI()
    return api.search_im_feeling_lucky(search_term=search_term)

@app.get("/NASA/image_and_video/asset/{nasa_id}")
async def search_nasa_images_and_videos(nasa_id):
    api=NASAImageAndVideoAPI()
    return api.asset(nasa_id=nasa_id)

if __name__ == "__main__":
    os.system("uvicorn main:app --host 0.0.0.0 --port 80")


