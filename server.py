# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
# 서버 정보
info = ("127.0.0.1", 9999)
# 소켓 생성
s = socket.socket()
# 9999번 포트 바인딩
s.bind(info)
# 바인딩 포트 리스닝
s.listen(5)
while True:
    # 접속요청 승인
    conn, address = s.accept()
    print "[+] new connection from %s(%d)" % (address[0], address[1])
    while True:
        try:
            # 클라이언트가 전송한 데이터 수신
            data = conn.recv(1024)
        except:
            print "Exception!!!"
            break
        if not data:
            # 데이터를 보내지 않은 클라이언트 연결 종료
            conn.close()
            break
        print "address %s send data: %s" % ( address[0], data)
        # 수신 데이터를 클라이언트에 전송
        conn.send(data)