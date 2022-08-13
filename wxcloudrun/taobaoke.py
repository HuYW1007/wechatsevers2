import top.api  #淘宝的API
from decimal import *  #小数的计算（避免价格不是整数）
import re

appkey = "33936806"
secret = "55b0dc2f82174ccfd44495eccde1d8fb"
adzone_id = "112720550151"

salename = '瑜伽紧身衣'

def TbkDgMaterialOptional(title): #查找商品的详细信息
    req = top.api.TbkDgMaterialOptionalRequest(domain='gw.api.taobao.com', port=80)
    req.set_app_info(top.appinfo(appkey, secret))
    req.adzone_id = adzone_id
    req.platform = 2
    req.q = title
    try:
         resp = req.getResponse()
         return resp
    except Exception as e:
        print(e)


def TbkCouponGet(item_id,activity_id): #查找商品的有无淘宝客对应的优惠券
    req = top.api.TbkCouponGetRequest(domain='gw.api.taobao.com', port=80)
    req.set_app_info(top.appinfo(appkey, secret))
    req.item_id = int(item_id)
    req.activity_id = str(activity_id)
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)

def TbkTpwdCreate(title,url): #有淘宝客对应优惠券的商品生成短链接
    req = top.api.TbkTpwdCreateRequest(domain='gw.api.taobao.com', port=80)
    req.set_app_info(top.appinfo(appkey, secret))
    req.text = title
    req.url = url
    try:
        resp = req.getResponse()
        return resp
    except Exception as e:
        print(e)

def TbkRetuMsg(salename):
	#给出要查询的商品名字
    response = TbkDgMaterialOptional(salename)
    map_data = response['tbk_dg_material_optional_response']['result_list']['map_data'][0]
    if map_data.get('coupon_share_url') is None:
        print('没有发现优惠券')
    else:
        title = map_data.get('title')  #得到商品的名称
        itemid = map_data.get('item_id')  #得到商品的id
        activityid = map_data.get('coupon_id')  #得到优惠券的id
        onsale = map_data.get('zk_final_price') #商品的原始价格
        orderimg = map_data['pict_url'] # 商品图片
        share_url = "https:" + map_data.get('coupon_share_url')
        priceresponse = TbkCouponGet(itemid,activityid)
        price = priceresponse['tbk_coupon_get_response']['data']
        discount = price.get('coupon_amount')#商品的优惠券额度
        difference = str(float(Decimal(onsale) - Decimal(discount)))  #优惠后的价格
        Shortlink = TbkTpwdCreate(title,share_url)
        link = Shortlink['tbk_tpwd_create_response']['data']['model'] #得到编码+短链接+标题
        link = link.split(' ')[1]#过滤出短链接
        message = '''/:gift{name}\n/:rose【在售价】{orderprice}元\n/:heart【券后价】{conponprice}元\n/:cake 【抢购链接】{link_short}\n-----------------\n复制这条信息\n{token}打开【手机淘宝】，即可查看\n------------------\n
            '''.format(name=title, orderprice=onsale, conponprice=difference, token="", link_short=link)
        print(message)
    try:
        return message
    except Exception as e:
        print(e)