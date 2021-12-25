---
title: "socket前后端传输数据"
summary: socket前后端传输数据
date: 2021-12-23
tags: ["socket"]
author: "YSL"
draft: false
weight: 2
---

### 前端
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>websocket</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
  </head>
  <body>
    <ul id="content"></ul>
    <form class="form">
      <input type="text" placeholder="请输入发送的消息" class="message" id="message"/>
      <input type="button" value="发送" id="send" class="connect"/>
      <input type="button" value="连接" id="connect" class="connect"/>
    </form>
  </body>
 
<script>
    var oUl=document.getElementById('content');
    var oConnect=document.getElementById('connect');
    var oSend=document.getElementById('send');
    var oInput=document.getElementById('message');
    var ws=null;
    oConnect.onclick=function(){
      ws=new WebSocket('ws://127.0.0.1:10083');
      ws.onopen=function(){
        oUl.innerHTML+="<li>客户端已连接</li>";
      }
 
      ws.onmessage=function(evt){
        console.log("fdsa")
        oUl.innerHTML+="<li>"+evt.data+"</li>";
      }
      ws.onclose=function(){
        oUl.innerHTML+="<li>客户端已断开连接</li>";
      };
      ws.onerror=function(evt){
        oUl.innerHTML+="<li>"+evt.data+"</li>";
      };
    };
    oSend.onclick=function(){
      if(ws){
        ws.send($("#message").val())
      }
    }
 
</script>
<style>
  *{
    margin: 0;
    padding: 0;
  }
  .message{
    width: 60%;
    margin: 0 10px;
    display: inline-block;
    text-align: center;
    height: 40px;
    line-height: 40px;
    font-size: 20px;
    border-radius: 5px;
    border: 1px solid #B3D33F;
  }
  .form{
    width:100%;
    position: fixed;
    bottom: 300px;
    left: 0;
  }
  .connect{
    height: 40px;
    vertical-align: top;
    /* padding: 0; */
    width: 80px;
    font-size: 20px;
    border-radius: 5px;
    border: none;
    background: #B3D33F;
    color: #fff;
  }
</style>
 
</html>
```

### 后端
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
import struct
import socket
import base64
import hashlib
import threading
 
def get_headers(data):
    headers = {}
    data = str(data, encoding='utf-8')
    header, body = data.split('\r\n\r\n', 1)
    header_list = header.split('\r\n')
    for i in header_list:
        i_list = i.split(':', 1)
        if len(i_list) >= 2:
            headers[i_list[0]] = "".join(i_list[1::]).split()
        else:
            i_list = i.split(" ", 1)
            if i_list and len(i_list) == 2:
                headers["method"] = i_list[0]
                headers["protocol"] = i_list[1]
    return headers
 
def send_msg(conn, msg_bytes):
    token = b'\x81'
    length = len(msg_bytes)
    if length < 126:
        token += struct.pack('B', length)
    elif length <= 0xFFFF:
        token += struct.pack('!BH', 126, length)
    else:
        token += struct.pack('!BQ', 127, length)
    msg = token + msg_bytes
    conn.sendall(msg)
    return True
 
# 解码
def parse_payload(payload):
    payload_len = payload[1] & 127
    if payload_len == 126:
        extend_payload_len = payload[2:4]
        mask = payload[4:8]
        decoded = payload[8:]
    elif payload_len == 127:
        extend_payload_len = payload[2:10]
        mask = payload[10:14]
        decoded = payload[14:]
    else:
        extend_payload_len = None
        mask = payload[2:6]
        decoded = payload[6:]
    bytes_list = bytearray()
    for i in range(len(decoded)):
        chunk = decoded[i] ^ mask[i % 4]
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')
    return body
 
# 建立连接
def handler_accept(sock):
    while True:
        conn, addr = sock.accept()
        data = conn.recv(8096)
        headers = get_headers(data)
        response_tpl = "HTTP/1.1 101 Switching Protocols\r\n"\
                       "Upgrade:websocket\r\n" \
                       "Connection: Upgrade\r\n" \
                       "Sec-WebSocket-Accept:%s\r\n" \
                       "WebSocket-Location:ws://%s\r\n\r\n"
        magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        if headers.get('Sec-WebSocket-Key'):
            value = headers['Sec-WebSocket-Key'][0] + magic_string
        ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
        response_str = response_tpl % (ac.decode('utf-8'), headers.get("Host"))
        conn.sendall(bytes(response_str, encoding="utf-8"))
        t = threading.Thread(target=handler_msg, args=(conn, ))
        t.start()
 
# 请求内容
def handler_msg(conn):
    with conn as c:
        while True:
            data_recv = c.recv(8096)
            if data_recv[0:1] == b'\x81':
                data_recv = parse_payload(data_recv)
                print(data_recv)
            send_msg(c, bytes('服务端revc:{}'.format(data_recv), encoding='utf-8'))
 
# 开起本地的服务
def server_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 10083))
    sock.listen(5)
    t = threading.Thread(target=handler_accept(sock))


    # conn, addr = sock.accept()
    # print(conn)
    # data = conn.recv(8096)
    # headers = get_headers(data)
    # response_tpl = "HTTP/1.1 101 Switching Protocols\r\n"\
    #                "Upgrade:websocket\r\n" \
    #                "Connection: Upgrade\r\n" \
    #                "Sec-WebSocket-Accept:%s\r\n" \
    #                "WebSocket-Location:ws://%s\r\n\r\n"
    # value = None
    # if headers.get('Sec-WebSocket-Key'):
    #     value = headers['Sec-WebSocket-Key'][0] + magic_string
    #
    # ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
    # response_str = response_tpl % (ac.decode('utf-8'), headers.get("Host"))
    # conn.sendall(bytes(response_str, encoding='utf-8'))
    #
    # while True:
    #     data_1 = conn.recv(8096)
    #     data_2 = parse_payload(data_1)
    #     print(data_2)
    #     send_msg(conn, b'text')
 
if __name__ == '__main__':
    server_socket()
```