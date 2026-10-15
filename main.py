from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_profissional import ControladorProfissional
from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_tipo_atendimento import ControladorTipoAtendimento
from controllers.controlador_atendimento import ControladorAtendimento
from controllers.controlador_procedimento import ControladorProcedimento
from controllers.controlador_pagamento import ControladorPagamento

paciente = ControladorPaciente()
profissional = ControladorProfissional()
clinica = ControladorClinica(profissional)
tipo = ControladorTipoAtendimento()
atendimento = ControladorAtendimento(clinica, paciente, profissional, tipo)
procedimento = ControladorProcedimento(atendimento, profissional)
pagamento = ControladorPagamento(atendimento)

menus = {1: paciente, 2: profissional, 3: clinica, 4: tipo,
         5: atendimento, 6: procedimento, 7: pagamento}

while True:
    entrada = input("\n1-Paciente 2-Profissional 3-Clínica 4-Tipo "
                    "5-Atendimento 6-Procedimento 7-Pagamento 0-Sair: ")
    if entrada == "0":
        break
    if entrada.isdigit() and int(entrada) in menus:
        menus[int(entrada)].abre_tela()