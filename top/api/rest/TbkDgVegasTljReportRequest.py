'''
Created by auto_sdk on 2021.12.20
'''
from top.api.base import RestApi
class TbkDgVegasTljReportRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.rights_id = None

	def getapiname(self):
		return 'taobao.tbk.dg.vegas.tlj.report'
