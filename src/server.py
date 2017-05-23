import web
import demjson
import Heartbeat
import uuid

urls = ('/(.*.txt)', 'StaticFile',
		'/cal', 'Cal')

class Cal:

	ustr = None

	def POST(self):
		data = demjson.decode(web.input()['data'])
		freq = float(web.input()['freq'])
		web.header('content-type','application/json')
		heartbeat = Heartbeat.cal(data, freq)
		print 'heartbeat is ', heartbeat
		return demjson.encode({'heartbeat':heartbeat})

	def GET(self):
		if Cal.ustr is None:
			Cal.ustr = uuid.uuid1()
		return Cal.ustr


class StaticFile:  
    def GET(self, file):
    	print file
        web.seeother('/static/' + file);

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()