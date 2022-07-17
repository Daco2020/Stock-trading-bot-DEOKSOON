import os

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")

#계좌번호 앞 8자리
CANO=os.getenv("CANO")
#계좌번호 뒤 2자리
ACNT_PRDT_CD=os.getenv("ACNT_PRDT_CD")

#실전투자
URL_BASE = "https://openapi.koreainvestment.com:9443"
#모의투자
# URL_BASE: "https://openapivts.koreainvestment.com:29443"

#디스코드 웹훅 URL
DISCORD_WEBHOOK_URL=os.getenv("DISCORD_WEBHOOK_URL")