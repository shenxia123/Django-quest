#coding=utf-8

from redishelper.timeline_util import get_unread_message_count

def message_processor(request):
    "添加未读消息数量"
    if request.user.is_authenticated():
        return {"unread_message":get_unread_message_count(request.user.id)}
    return {"unread_message":0}
