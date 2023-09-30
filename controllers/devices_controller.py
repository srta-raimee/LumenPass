from flask import request, render_template, Blueprint, redirect, url_for
from models import *

dispositivos = Blueprint("dispositivos", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

  

@dispositivos.route("/registrar_dispositivo", methods=["POST"])
def registrar_dispositivo():
    nome = request.form.get('nome', None)
    descricao = request.form.get('descricao', None)
    statuss = request.form.get('status', None)
    
    # Verificar o valor do status
    if statuss == 'ligado':
        status = True
    else:
        status = False

    Dispositivo.adicionar_dispositivo(nome, descricao, status)
  
    return redirect(url_for('render.listar_dispositivos'))