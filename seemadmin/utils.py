# -*- coding:utf-8 -*-
import settings
from qiniu import Auth, put_data


def qiniu_upload(file_bytes, bucket_name, save_path):
    """七牛上传文件
    save_path 直接包含文件名，故此字段请在外部生成
    返回 url, 应该等于 save_path
    """
    q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
    token = q.upload_token(bucket_name, save_path)
    ret, info = put_data(token, save_path, file_bytes, check_crc=True)
    if info.exception:
        raise info.exception
    return settings.PREFIX_PIC_URL + '/' + ret['key']


# -*- coding: utf-8 -*-
"""
返回处理
"""
import json
from django.http import HttpResponse
import datetime

class QFRET:
    OK = "0000"
    DBERR = "2000"
    THIRDERR = "2001"
    SESSIONERR = "2002"
    DATAERR = "2003"
    IOERR = "2004"
    LOGINERR = "2100"
    PARAMERR = "2101"
    USERERR = "2102"
    ROLEERR = "2103"
    REQERR = "2200"
    IPERR = "2201"
    NODATA = "2300"
    DATAEXIST = "2301"
    UNKOWNERR = "2400"


# 增强型json编码器
class ExtendedEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) == datetime.date:
            return o.strftime('%Y-%m-%d')
        elif type(o) == datetime.datetime:
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder(self, o)


error_map = {
    QFRET.OK: u"成功",
    QFRET.DBERR: u"数据库查询错误",
    QFRET.THIRDERR: u"第三方系统错误",
    QFRET.SESSIONERR: u"用户未登录",
    QFRET.DATAERR: u"数据错误",
    QFRET.IOERR: u"文件读写错误",
    QFRET.LOGINERR: u"用户登录失败",
    QFRET.PARAMERR: u"参数错误",
    QFRET.USERERR: u"用户不存在或未激活",
    QFRET.ROLEERR: u"用户身份错误",
    QFRET.REQERR: u"非法请求或请求次数受限",
    QFRET.IPERR: u"IP受限",
    QFRET.NODATA: u"无数据",
    QFRET.DATAEXIST: u"数据已存在",
    QFRET.UNKOWNERR: u"未知错误",
}


def error(errcode, respmsg='', resperr='', data=None, escape=False, encoder=ExtendedEncoder, param=None):
    if not respmsg:
        respmsg = error_map[errcode]
    if not resperr:
        resperr = respmsg
    if not data:
        data = {}
    ret = {"respcd": errcode, "resperr": resperr, "respmsg": respmsg, "data": data}
    return HttpResponse(json.dumps(ret, ensure_ascii=escape, cls=encoder, separators=(',', ':')),
                        content_type='application/json')


def success(data, respmsg='', resperr='', escape=False, encoder=ExtendedEncoder, param=None):

    if not respmsg:
        respmsg = "成功"
    ret = {"respcd": "0000", "resperr": resperr, "respmsg": respmsg, "data": data}
    return HttpResponse(json.dumps(ret, ensure_ascii=escape, cls=encoder, separators=(',', ':')),
                        content_type='application/json')
