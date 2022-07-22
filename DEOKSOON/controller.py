
from fastapi import FastAPI
from DEOKSOON import service


app = FastAPI()

@app.get("/run")
async def run():
    """
    TODO:
    # 장이 열린 평일 오전 9시에 자동실행한다.
    1. 토큰 생성여부와 함께 health를 체크한다.
    2. 현재시간과 장 상황을 브리핑한다.
    3. 주요기사의 제목과 링크를 가져온다.
    4. 해당 내용들을 메시지에 담아 디스코드로 전송한다.
    5. 메시지에는 '거래시작' 여부를 묻는 내용을 포함한다.
    """
    token = service.get_access_token()
    if token:
        print(token)
    return "고양이 덕순이가 아침 '우다다'를 시작합니다."


@app.get("/run/trade")
async def run_trade(): 
    """
    TODO:
    # 디스코드를 통해 '거래시작' 버튼을 누를때 실행한다.
    1. 자동매매를 실행한다.
    2. 거래시작 메시지와 '일하는 덕순이' 사진을 디스코드로 전송한다.
    3. 3시 20분, 거래종료 메시지와 '퇴근하는 덕순이' 사진을 디스코드로 전송한다.
    4. 오늘 거래내용과 실적을 노션 데이터베이스에 업로드 한다.
    5. Access Token을 None으로 초기화 한다.
    """
    print("덕순이가 커피를 마시며 매매를 시작합니다.")
    return "덕순이가 매매를 마치고 퇴근합니다."