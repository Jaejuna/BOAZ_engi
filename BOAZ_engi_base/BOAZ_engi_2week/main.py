import requests
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
	return "API 실습을 해봅시당!"

# 주소 검색하기
def getLatLng(address):
	result = ""
	url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
	rest_api_key = 'f5f917814b3a2660477be5fb69905930'
	header = {'Authorization': 'KakaoAK ' + rest_api_key}

	r = requests.get(url, headers=header)

	if r.status_code == 200:
		result_address = r.json()["documents"][0]["address"]
		result = result_address["y"], result_address["x"]
	else:
		result = "ERROR[" + str(r.status_code) + "]"

	return result

# 장소 정보 가져오기
def getInfo(latlng, keyword):
	y = str(latlng[0]) # 위도
	x = str(latlng[1]) # 경도
	radius = str(20000) # 반경 최대 20km 이내
	url = 'https://dapi.kakao.com/v2/local/search/keyword.json?' \
		+ 'y=' + y + '&' + 'x=' + x + '&' + 'radius=' + radius + '&query=' + keyword
	rest_api_key = 'f5f917814b3a2660477be5fb69905930'
	header = {'Authorization': 'KakaoAK ' + rest_api_key}
	r = requests.get(url, headers=header)
	
	if r.status_code == 200:
		result = r.json()["documents"][0] # 첫번째 검색 결과
	else:
		result = "ERROR[" + str(r.status_code) + "]"
	
	return result

@app.get("/place")
def myPlace():
	address = "서울특별시 용산구 신흥로3길 2 (용산동2가)" # 서울시청 주소
	address_latlng = getLatLng(address)
	keyword = "보니스 피자펍" # keword에 소개하고 싶은 맛집 이름을 적어주면 됩니다!
	place_info = getInfo(address_latlng, keyword)
	
	return place_info