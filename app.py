from flask import Flask, request, jsonify, send_from_directory
import sqlite3, os
app=Flask(__name__,static_folder='public',static_url_path='/assets')
DB=os.environ.get('DB_PATH','candidaturas.sqlite3')
with sqlite3.connect(DB) as c:
 c.execute('CREATE TABLE IF NOT EXISTS candidaturas(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, celular TEXT, email TEXT, area TEXT, missao TEXT, modalidade TEXT, criado TEXT DEFAULT CURRENT_TIMESTAMP)')
@app.get('/')
def home(): return send_from_directory('public','index.html')
@app.get('/<path:path>')
def assets(path): return send_from_directory('public',path)
@app.post('/api/candidaturas')
def cadastro():
 d=request.get_json(silent=True) or {}
 keys=['nome','idade','celular','email','area','missao','modalidade']
 try:
  if not all(str(d.get(k,'')).strip() and len(str(d[k]))<=150 for k in keys) or not 18<=int(d['idade'])<=100 or '@' not in d['email'] or d.get('consentimento')!='on' or d['area'] not in ['logistica','medico','enfermeiro','outro'] or d['missao'] not in ['Nacionais','Internacionais','Ambas'] or d['modalidade'] not in ['Voluntariado','Emprego remunerado']: raise ValueError()
 except (ValueError,TypeError): return jsonify(message='Confira os dados e o consentimento.'),400
 with sqlite3.connect(DB) as c: c.execute('INSERT INTO candidaturas(nome,idade,celular,email,area,missao,modalidade) VALUES(?,?,?,?,?,?,?)',tuple(d[k] for k in keys))
 return jsonify(message='Candidatura registrada com sucesso.'),201
if __name__=='__main__': app.run(host='127.0.0.1',port=8000)
