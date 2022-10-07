import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "bb069256a7msh323cd2fc9d52026p18adb6jsn4d849ea7e97e",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}



async def remove_background(img_url):
	payload = f"image_url = {img_url}"
	response = requests.request("POST", url, data = payload, headers = headers)
	return response.json()['response']['image_url']