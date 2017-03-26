import time
import TencentYoutuyun

appid = '10062981'
secret_id = 'AKIDuaDVNhQ3KoHlDkzCPd9wD5z9XnOuNPEQ'
secret_key = 'XvMvaMNVj9gJufYaYt4hYVdvW2eNY3cb'
userid = '1234567'
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT 

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.FaceCompare('psb5.jpg','psb4.jpg')
#ret is a dict

print ret
