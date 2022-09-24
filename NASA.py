from dotenv import dotenv_values
from random import randint
import httpx


class HttpxInjection:
    base_url = None

    def _get(self, url):
        return httpx.get(f"{self.base_url}{url}")


class NASABaseAPI(HttpxInjection):
    env = dotenv_values(".env")
    api_key = env["NASA_API_KEY"]
    base_url = "https://api.nasa.gov"

    def astronomy_picture_of_the_day(self):
        url = f"/planetary/apod?api_key={self.api_key}"
        response = self._get(url).json()
        return response


class NASAImageAndVideoAPI(HttpxInjection):
    env = dotenv_values(".env")
    api_key = env["NASA_API_KEY"]
    base_url = "https://images-api.nasa.gov"

    def search(self, search_term):
        url = f"/search?q={search_term}"
        response = self._get(url).json()
        return response

    def search_im_feeling_lucky(self, search_term):
        url = f"/search?q={search_term}"
        response = self._get(url).json()["collection"]["items"]
        nasa_id = response[randint(0, len(response) - 1)]["data"][0]["nasa_id"]
        return self.asset(nasa_id)

    def asset(self, nasa_id):
        url = f"/asset/{nasa_id}"
        response = self._get(url).json()
        return response


if __name__ == "__main__":
    NASA = NASABaseAPI()
    NASA_images = NASAImageAndVideoAPI()
    # print(NASA.astronomy_picture_of_the_day())
    print(NASA_images.search_im_feeling_lucky("mars"))
    # print(NASA_images.asset("Ep224_Radio Waves"))
