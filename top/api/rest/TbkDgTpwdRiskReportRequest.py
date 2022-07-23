'''
Created by auto_sdk on 2021.12.29
'''
from top.api.base import RestApi
class TbkDgTpwdRiskReportRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.offset = None
		self.pid = None

	def getapiname(self):
		return 'taobao.tbk.dg.tpwd.risk.report'
