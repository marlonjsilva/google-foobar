import base64
import unicodedata
if __name__ == "__main__":
    msg = b'FkYBGQwNV0BDExkMTUYVHgoPRhQcFB5VAg0eCQ4JR1YXFAMWSgQBGAoLX1ZUExUWSgQUCgAcRkAX FAMWSggcDx0LVlpSWFwRQUFVDQwGW1ZGUVRTAxVVTFVOFUZeWFZVBgQWS0NOFUFRVltfGRJVTFVO FUBRUlwRQUFVCgABFRMKFB5BBA9TSxI='
    msg = base64.b64decode(msg).decode("utf-8")
    print(msg)