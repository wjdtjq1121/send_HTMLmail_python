import smtplib
from email.mime.multipart import MIMEMultipart
#from email.header import Header
from email.mime.text import MIMEText

def sender(recipients):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('brian.jeongseop.han@bringko.com', 'qjkmetjrvtenpjly')

    body = """

    <div style="margin-left: 20px; margin-top: 20px;">
        send html email 
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

