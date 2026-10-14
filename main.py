from controllers.controlador_profissional import ControladorProfissional
from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_tipo_atendimento import ControladorTipoAtendimento

profissionais = ControladorProfissional()
clinicas = ControladorClinica(profissionais)
tipos = ControladorTipoAtendimento()

profissionais.abre_tela()
clinicas.abre_tela()
tipos.abre_tela()