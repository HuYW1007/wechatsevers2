'''
Created by auto_sdk on 2022.06.09
'''
from top.api.base import RestApi
class TbkDgCpaActivityDetailRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.event_id = None
		self.indicator_alias = None
		self.page_no = None
		self.page_size = None
		self.query_type = None

	def getapiname(self):
		return 'taobao.tbk.dg.cpa.activity.detail'
