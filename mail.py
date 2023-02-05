import smtplib
from email.mime.multipart import MIMEMultipart
#from email.header import Header
from email.mime.text import MIMEText

def sender(recipients):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('brian.jeongseop.han@bringko.com', 'qjkmetjrvtenpjly')

    body = """

    <div class="mail_content" style="margin-left: 20px; margin-top: 20px;">
        <div class="bringko_logo">
            <img style= "width: 107px; object-fit: cover;" src="data:image/png;base64,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
    ">
        </div>
        <div class="to_customer_alarm" style="color: black; font-size: 15px; padding-top: 34px; letter-spacing: 0.16px; line-height: 23px; font-stretch: 95%;">
            안녕하세요, 00고객님. <br>
            고객님께서는 현재 총 00포인트를 보유 중입니다. <br>
            이 중 00포인트가 30일 이후 소멸됩니다. 소멸 전 사용하세요!
        </div>
        <div class="to_customer_bullet" style="padding-top: 29px; letter-spacing: 0.16px; line-height: 25px; font-size: 16px; font-weight: bold; font-stretch: 95%;">
            • 포인트 잔액: 00 <br> 
            • 사용기한: (한국시간 기준) 00/00 0요일 23:59까지(미사용 시 자동소멸) <br>
            • 사용방법: Bringko 서비스 2차 결제(해외 배송비)에 사용 가능
        </div>
        <div style="padding-top: 34px;">
            <button type="button" class="bringko_button" style="width: 230px; height: 60px; background: #ff8800; color: white;
            font-size: 16px; letter-spacing: 0.16px; font-stretch: 95%; font-weight: bold; border-radius: 10px; border: none;">
                브링코 앱 바로 가기 >>>
            </button>
        </div>
        <div class="divider" style="padding-top: 30px; width: 650px; border-bottom: 2px solid #d0d0d0;"></div>
        <div class="footer" style="padding-top: 15px; color: black; letter-spacing: 0; font-size: 14px; line-height: 24px; font-stretch: 95%;">
            *사용기한은 연장이 불가합니다. <br>
            *적립금 잔액은 '마이페이지 > 포인트'에서 확인 가능합니다. <br>
            *본 안내는 00/00 기준으로 발송되어 수신 시점에 따라 소멸 예정 금액이 상이할 수 있습니다.
        </div>
    </div>

    """

    for item in recipients:
        print('이메일 보내는중 :' + item['email'])

        msg = MIMEMultipart('alternative')

        msg['Subject'] = '메일 제목'
        msg['From'] = 'brian.jeongseop.han@bringko.com'
        msg['To'] = item['email']

        msg.attach(MIMEText(body,'html'))

        server.send_message(msg)

    print('이메일 보내기 완료')
    server.quit()


if __name__ == '__main__':
    list_json = [
    {'email': 'brian.jeongseop.han@bringko.com'},
     ]
    sender(list_json)

