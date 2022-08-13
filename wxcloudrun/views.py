from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from . import receive
from . import reply
from . import taobaoke


@csrf_exempt
def autoreply(request):
    try:
        wxData = request.body
        print("Handle POST wxData is: ", wxData)

        recMsg = receive.parse_xml(wxData)
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                content = recMsg.Content.decode('utf-8')
                content = taobaoke.TbkRetuMsg(content)
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return  HttpResponse(replyMsg.send())
            if recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return HttpResponse(replyMsg.send())
            else:
                return HttpResponse(reply.Msg().send())
        else:
            print("暂不处理")
            # return "success"
            return HttpResponse(reply.Msg().send())

    except Exception as e:
        print(e)

