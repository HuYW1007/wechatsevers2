'''
Created by auto_sdk on 2021.11.26
'''
from top.api.base import RestApi
class TopAuthTokenRefreshRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refresh_token = None

	def getapiname(self):
		return 'taobao.top.auth.token.refresh'
