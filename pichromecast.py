import ssl
import json
import socket
import struct

# https://github.com/eigenein/protobuf/blob/2699b92fafc212ab3e7278aaa3931e9f4d326308/pure_protobuf/serializers/__init__.py#L452
def calc_variant(value):
    byte_list = []
    while value > 0x7F:
        byte_list += [value & 0x7F | 0x80]
        value >>= 7
    return bytes(byte_list + [value])

def play_url(url, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, 15, 1)
    sock.settimeout(30)
    sock.connect((host, 8009))
    sock = ssl.wrap_socket(sock)
    sock.write(b'\x00\x00\x017\x08\x00\x12\x08sender-0\x1a\nreceiver-0"(urn:x-cast:com.google.cast.tp.connection(\x002\xf0\x01{"type": "CONNECT", "origin": {}, "userAgent": "PyChromecast", "senderInfo": {"sdkType": 2, "version": "15.605.1.3", "browserVersion": "44.0.2403.30", "platform": 4, "systemVersion": "Macintosh; Intel Mac OS X10_10_3", "connectionType": 1}}')
    sock.write(b'\x00\x00\x00g\x08\x00\x12\x08sender-0\x1a\nreceiver-0"#urn:x-cast:com.google.cast.receiver(\x002&{"type": "GET_STATUS", "requestId": 1}')
    sock.write(b'\x00\x00\x00e\x08\x00\x12\x08sender-0\x1a\nreceiver-0"\'urn:x-cast:com.google.cast.tp.heartbeat(\x002 {"type": "PING", "requestId": 2}')
    sock.read(struct.unpack(">I", sock.read(4))[0])
    sock.read(struct.unpack(">I", sock.read(4))[0])
    sock.write(b'\x00\x00\x00x\x08\x00\x12\x08sender-0\x1a\nreceiver-0"#urn:x-cast:com.google.cast.receiver(\x0027{"type": "LAUNCH", "appId": "CC1AD845", "requestId": 3}')
    transport_id = sock.read(struct.unpack(">I", sock.read(4))[0]).split(b'"transportId"')[1].split(b'"')[1]
    sock.write(b'\x00\x00\x01Q\x08\x00\x12\x08sender-0\x1a$%s"(urn:x-cast:com.google.cast.tp.connection(\x002\xf0\x01{"type": "CONNECT", "origin": {}, "userAgent": "PyChromecast", "senderInfo": {"sdkType": 2, "version": "15.605.1.3", "browserVersion": "44.0.2403.30", "platform": 4, "systemVersion": "Macintosh; Intel Mac OS X10_10_3", "connectionType": 1}}' % transport_id)
    sock.write(b'\x00\x00\x00~\x08\x00\x12\x08sender-0\x1a$%s" urn:x-cast:com.google.cast.media(\x002&{"type": "GET_STATUS", "requestId": 4}' % transport_id)
    payload = json.dumps({"media": {"contentId": url, "streamType": "BUFFERED", "contentType": "audio/mp3", "metadata": {}}, "type": "LOAD", "autoplay": True, "customData": {}, "requestId": 5, "sessionId": transport_id})
    msg = (b'\x08\x00\x12\x08sender-0\x1a$%s" urn:x-cast:com.google.cast.media(\x002' % transport_id) + calc_variant(len(payload)) + payload
    sock.write(struct.pack(">I", len(msg)) + msg)
    sock.read(struct.unpack(">I", sock.read(4))[0])
    sock.read(struct.unpack(">I", sock.read(4))[0])
    sock.read(struct.unpack(">I", sock.read(4))[0])
    sock.close()
