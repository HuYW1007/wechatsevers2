'''
Created by auto_sdk on 2021.09.27
'''
from top.api.base import RestApi
class TbkDgVegasTljStopRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.rights_id = None

	def getapiname(self):
		return 'taobao.tbk.dg.vegas.tlj.stop'
