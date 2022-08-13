import xml.etree.ElementTree as ET

def parse_xml(webData):
    if len(webData) == 0:
        return None

    Data = ET.fromstring(webData)
    msg_type = Data.find('MsgType').text

    if msg_type == 'text':
        return Text(Data)
    elif msg_type == 'image':
        return Image(Data)

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

class Text(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode('utf-8')


class Image(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text





