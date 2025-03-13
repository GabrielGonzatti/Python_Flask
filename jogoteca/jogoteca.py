from flask import Flask, render_template, request, redirect, session, flash, url_for

class jogo:
  def __init__(self, nome, categoria, console):
    self.nome=nome
    self.categoria=categoria
    self.console=console
    
jogo1 = jogo('Tetris', 'Puzzle', 'Atari') # definindo o objeto 'jogo1' da classe jogo com seus atributos.
jogo2 = jogo('God Of War', 'Rack n Slash', 'PS2')
jogo3 = jogo('Mortal Kombat', 'Luta', 'PS2')
lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__) #SIGNIFICA: Cria uma instância do Flask onde podemos criar uma rota com nome do html:
app.secret_key = 'alura'
@app.route('/') # definir rota para o servidor
def index(): # definir função para executar com a rota
    return render_template('lista.html', titulo="Jogos", jogos = lista_jogos)
@app.route('/novo')
def novo():
    if 'logado' not in session or session['logado'] == None:
        print("Usuário não logado, redirecionando para login...")
        flash('É necessário fazer o login!')
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo') 
@app.route('/criar', methods = ['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo_novo = jogo(nome, categoria, console)
  lista_jogos.append(jogo_novo)
  return redirect(url_for('index')) #redireciona para uma rota.

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
  if 'alohomora' == request.form['senha']:
    session['logado'] = request.form['usuario'] 
    proxima_pagina = request.form['proxima'] 
    return redirect(proxima_pagina)
  else:
    flash(f"Error - {session.get('logado', 'Usuário não logado')}")
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  flash(f"Usuário {session.get('logado', 'Usuário não logado')} deslogado com sucesso!")
  session['logado'] = None
  return redirect(url_for('index'))

app.run(debug=True) #RUN para rodar o servidor e rota