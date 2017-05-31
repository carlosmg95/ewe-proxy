#!/usr/bin/python
import time
from daemon import runner
import json,requests
class ReminderDaemon():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/tmp/foo.pid'
		self.pidfile_timeout = 5
	def run(self):
		while True:
			print(time.ctime())
			url = "http://test.ewetasker.cluster.gsi.dit.upm.es//controllers/eventsManager.php"
			t=time.strftime("%X")
			t=t[:5]
			d=time.strftime("%x")+" "+t
			print(t)
			print(d)
			event="@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>. @prefix string: <http://www.w3.org/2000/10/swap/string#>. @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/#>. @prefix ewe-time: <http://gsi.dit.upm.es/ontologies/ewe-time/ns/#>. ewe-time:Clock rdf:type ewe-time:TimeHasCome. ewe-time:Clock ewe-time:Hour '"+t+"'."
			payload = {"user": "admin","inputEvent":event}
			data= requests.post(url, data=payload).json()
			print(data)
			event="@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>. @prefix string: <http://www.w3.org/2000/10/swap/string#>. @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/#>. @prefix ewe-date: <http://gsi.dit.upm.es/ontologies/ewe-date/ns/#>. ewe-date:Moment rdf:type ewe-date:DateHasCome. ewe-date:Moment ewe-date:Day '"+d+"'."
			payload = {"user": "admin","inputEvent":event}
			data= requests.post(url, data=payload).json()
			print(data)
			time.sleep(60)

reminder = ReminderDaemon()
daemon_runner = runner.DaemonRunner(reminder)
daemon_runner.do_action()
