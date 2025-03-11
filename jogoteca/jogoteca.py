from flask import Flask, render_template, request, redirect

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
@app.route('/') # definir rota para o servidor
def index(): # definir função para executar com a rota
    return render_template('lista.html', titulo="Jogos", jogos = lista_jogos)

@app.route('/criar', methods = ['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo_novo = jogo(nome, categoria, console)
  lista_jogos.append(jogo_novo)
  return redirect('/') #redireciona para uma rota.

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo='Novo Jogo')    
app.run(debug=True) #RUN para rodar o servidor e rota