import streamlit as st
import requests
from openweathermapy import utils, core

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # 온도를 섭씨로 받아옴
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def main():
    st.title("날씨 정보 애플리케이션")

    # 사용자로부터 API 키 입력 받기
    api_key = st.text_input("OpenWeatherMap API 키를 입력하세요:")

    # 사용자로부터 도시 입력 받기
    city = st.text_input("날씨 정보를 확인할 도시를 입력하세요:")

    if st.button("날씨 정보 가져오기"):
        if api_key and city:
            try:
                weather_data = get_weather(api_key, city)

                # 가져온 데이터 출력
                st.write(f"{city}의 현재 날씨 정보:")
                st.write(f"온도: {weather_data['main']['temp']}°C")
                st.write(f"습도: {weather_data['main']['humidity']}%")
                st.write(f"날씨: {weather_data['weather'][0]['description']}")
            except Exception as e:
                st.error(f"날씨 정보를 가져오는 도중 오류가 발생했습니다: {e}")
        else:
            st.warning("API 키와 도시를 입력해주세요.")

if __name__ == "__main__":
    main()
