# def coletaDados(tipo):
#     # Dados Comuns
#     n_res = input('Número da Resolução: ')
#     data_res = Data.coletaData('da Resolução', True)
#     ad_referendum = input('Resolução Ad Referendum?(1. Sim, 2. Não): ')
#     data_reuniao = None
#     if ad_referendum == '1':
#         ad_referendum = True
#     else:
#         ad_referendum = False
#         data_reuniao = Data.coletaData('da Reunião', False)
#
#     # Dados específicos conforme tipo da resolução
#     if tipo == 1:# ***prorrogação de qualificação***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nivel_discente = converteNivelString(op_nivel)
#         nome = input('Nome do(a) discente: ')
#         ano_ingresso = input('Ano de ingresso do(a) discente: ')
#         data_limite = Data.coletaData('Limite Aprovada', False)
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, ano_ingresso, data_limite
#
#     elif tipo == 2:
#         nivel_discente = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         rga = input('Informe o RGA do(a) discente: ')
#         motivo = None
#         semestre = input('Informe o semestre de trancamento(ano/semestre): ')
#
#         print("Selecione uma opção: ")
#         print("1. Motivos particulares")
#         print("2. Motivos de saúde")
#         print("3. Motivos profissionais")
#         print("4. Motivos acadêmicos")
#         op = input('Informe o motivo do trancamento: ')
#
#         if op == '1':
#             motivo = 'motivos particulares'
#         elif op == '2':
#             motivo = 'motivos de saúde'
#         elif op == '3':
#             motivo = 'motivos profissionais'
#         elif op == '4':
#             motivo = 'motivos acadêmicos'
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, rga, semestre, motivo
#
#     elif tipo == 3:# *** Desligamento do Programa ***
#         cont_discentes = 0
#         discente = []
#         niveis_discentes = []
#         motivo = None
#         motivos = []
#
#         flag_discente = True
#         while flag_discente:
#             op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#             nome = input('Nome do(a) discente: ')
#             discente.append(nome)
#             nivel_discente = converteNivelString(op_nivel)
#             niveis_discentes.append(nivel_discente)
#
#             print("Selecione uma opção: ")
#             print("1. Solicitado pelo(a) discente")
#             print("2. Não realização de matrícula")
#             print("3. Outro")
#             op = input('Informe o motivo do desligamento: ')
#
#             if op == '1':
#                 motivo = 'Solicitado pelo(a) discente'
#             elif op == '2':
#                 semestre = input('Semestre em que não foi realizada matrícula(ano/semestre): ')
#                 motivo = 'Matrícula não realizada no semestre ' + semestre + '(item IV, artigo 45 do regulamento do PPGCTA de 2023)'
#             elif op == '3':
#                 motivo = input('Informe o motivo: ')
#
#             motivos.append(motivo)
#             cont_discentes += 1
#
#             inserir_nova = input('Incluir mais um aluno?(S/N)?: ')
#
#             if inserir_nova == 'N':
#                 break
#
#         return n_res, data_res, ad_referendum, data_reuniao, discente, cont_discentes, niveis_discentes, motivos
#
#     elif tipo == 4:# *** Cancelamento de Matricula em Disciplinas ***
#         cont_discentes = 0
#         discente = []
#         niveis_discentes = []
#         todas_disciplinas = []
#         todos_docentes = []
#
#         flag_discente = True
#         while flag_discente:
#             op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#             nome = input('Nome do(a) discente: ')
#             discente.append(nome)
#             nivel_discente = converteNivelString(op_nivel)
#             niveis_discentes.append(nivel_discente)
#             cont_discentes += 1
#             cont_disciplinas = 0
#             disciplinas = []
#             docentes = []
#
#             flag_disciplina = True
#             while flag_disciplina:
#
#                 disciplina = input(f'Informe a disciplina({nome}): ')
#                 docente = input(f'Informe o docente responsável({disciplina}): ')
#                 cont_disciplinas += 1
#
#                 inserir_nova = input('Inserir mais uma disciplina(S/N)?: ')
#                 if inserir_nova == 'S':
#                     disciplina = str(cont_disciplinas) + '. ' + disciplina + ', '
#                     disciplinas.append(disciplina)
#                     docente = str(cont_disciplinas) + '. ' + docente + ', '
#                     docentes.append(docente)
#                 if inserir_nova == 'N':
#                     disciplina = str(cont_disciplinas) + '. ' + disciplina
#                     disciplinas.append(disciplina)
#                     todas_disciplinas.append(disciplinas)
#                     docente = str(cont_disciplinas) + '. ' + docente
#                     docentes.append(docente)
#                     todos_docentes.append(docentes)
#
#                     flag_disciplina = False
#
#             inserir_nova = input('Incluir mais um aluno?(S/N)?: ')
#             if inserir_nova == 'N':
#                 break
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, discente, todas_disciplinas, todos_docentes, cont_discentes, niveis_discentes
#
#     elif tipo == 5:# *** Troca de Orientação ***
#         nivel_discente = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         orientador_atual = input('Orientador Atual: ')
#         novo_orientador = input('Novo Orientador: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, orientador_atual, novo_orientador
#
#     elif tipo == 6:
#         lista_res = []
#         flag = True
#
#         while flag:
#             res = input('Informe o número e ano da resolução ad referendum(numero-ano): ')
#             lista_res.append(res)
#
#             nova = input('Deseja Inserir mais uma resolução?(S/N): ')
#             if nova == 'N':
#                 flag = False
#
#             conj_res = ', '.join(res for res in lista_res)
#
#         return n_res, data_res, data_reuniao, lista_res, conj_res
#
#     elif tipo == 7:# *** Aprovação de Banca ***
#         nivel_discente = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         if nivel_discente == 'M':
#             tipo_trabalho = 'Dissertação'
#             nivel_discente = 'Mestrado'
#         else:
#             tipo_trabalho = 'Tese'
#             nivel_discente = 'Doutorado'
#
#         tipo_apresentacao = input('Informe o tipo de apresentação - 1. Qualificação || 2. Defesa: ')
#         if tipo_apresentacao == '1':
#             tipo_apresentacao = 'Qualificação'
#         else:
#             tipo_apresentacao = 'Defesa'
#
#         titulo_trabalho = input('Informe o nome do trabalho: ')
#         data_apresentacao = input('Informe a data de apresentação do trabalho: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, tipo_trabalho, titulo_trabalho, tipo_apresentacao, data_apresentacao
#
#     elif tipo == 8:# *** Calendario de Reunioes ***
#         cont_reunioes = 0
#         reunioes = []
#         data_reunioes = []
#         flag_reuniao = True
#
#         ano = input('Informe o ano vigente: ')
#
#         while flag_reuniao:
#             cont_reunioes += 1
#             reuniao = str(cont_reunioes) + 'ª Ordinária'
#             reunioes.append(reuniao)
#             data_agendada = Data.coletaData("de agendamento da reunião", False)
#             data_reunioes.append(data_agendada)
#
#             inserir_nova = input('Incluir mais uma reunião?(S/N)?: ')
#
#             if inserir_nova == 'N':
#                 flag_reuniao = False
#
#         return n_res, data_res, ad_referendum, data_reuniao, ano, cont_reunioes, reunioes, data_reunioes
#
#     elif tipo == 9:# *** Adiamento de reunião ***
#         n_reuniao = input('Informe qual reunião será adiada(número da reunião ordinária: ')
#         data_inicial = Data.coletaData('inicial que estava prevista a reunião', False)
#         resolucao = input('Segundo Resolução(número resolução): ')
#         data_res_original = Data.coletaData('da resolução', True)
#         previsao = input('A reunião possui nova data prevista?(1. Sim, 2. Não): ')
#         if previsao == '1':
#             data = Data.coletaData('nova da reunião', False)
#             previsao = ' para ' + data
#         else:
#             previsao = ', sine die, '
#
#         return n_res, data_res, ad_referendum, data_reuniao, n_reuniao, data_inicial, resolucao, data_res_original, previsao
#
#     elif tipo == 10:# *** Afastamento de discente ***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         nivel_discente = converteNivelString(op_nivel)
#
#         n_dias_afast = input('Informe o número de dias do afastamento: ')
#
#         data_inicio = Data.coletaData('de início do afastamento', False)
#         data_fim = Data.coletaData('de finalização do afastamento', False)
#
#         print("Selecione uma opção: ")
#         print("1. Motivos particulares")
#         print("2. Motivos de saúde")
#         print("3. Outros")
#         op = input('Informe o motivo do afastamento: ')
#
#         if op == '1':
#             motivo = 'motivos particulares do(a) discente.'
#         elif op == '2':
#             motivo = 'questões de saúde, comprovadas através de atestado médico apresentado.'
#         elif op == '3':
#             motivo = input('Informe o motivo: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, n_dias_afast, data_inicio, data_fim, motivo
#
#     elif tipo == 11:# *** Inclusão de coorientação ***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         nivel_discente = converteNivelString(op_nivel)
#
#         coorientador = input('Informe o nome do coorientador: ')
#         universidade = input('Informe o nome da universiade do coorientador: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, coorientador, universidade
#
#     elif tipo == 12:# *** Licença Maternidade ***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nome = input('Nome do(a) discente: ')
#         nivel_discente = converteNivelString(op_nivel)
#
#         ano_ingresso = input('Informe o ano de ingresso do(a) discente: ')
#         data_fim_lic = Data.coletaData('de finalização da licença maternidade', False)
#         data_ini_defesa = Data.coletaData('inicial para defesa', False)
#         data_lmt_defesa = Data.coletaData('atualizada para defesa', False)
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, ano_ingresso, data_fim_lic, data_ini_defesa, data_lmt_defesa
#
#     elif tipo == 13:# *** Aproveitamento de Exame de Suficiência ***
#         lingua = input('Informe a língua do exame de suficiência: ')
#         cont_discentes = 0
#         discentes= []
#         datas = []
#         resolucoes = []
#
#         flag_discente = True
#         while flag_discente:
#             nome = input('Nome do(a) discente: ')
#             discentes.append(nome)
#
#             data = Data.coletaData('de realização do exame', False)
#             resolucao = input('Informe a resolução que homologou essa aprovação(num. resolução/ano): ')
#             datas.append(data)
#             resolucoes.append(resolucao)
#             cont_discentes += 1
#
#             inserir_novo = input('Incluir mais um aluno?(S/N)?: ')
#             if inserir_novo == 'N':
#                 break
#
#         return n_res, data_res, ad_referendum, data_reuniao, lingua, discentes, cont_discentes, datas, resolucoes
#
#     elif tipo == 14:# *** Convalidação de Exame de Suficiência ***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nivel_discente = converteNivelString(op_nivel)
#         nome = input('Nome do(a) discente: ')
#
#         print("Selecione uma opção: ")
#         print("1. ITP-TOEFL")
#         print("2. Outro")
#         op = input('Informe o exame convalidade: ')
#
#         if op == '1':
#             exame = 'ITP-TOEFL'
#         elif op == '2':
#             exame = input('Informe o nome do exame: ')
#
#         print("Selecione uma opção: ")
#         print("1. Inglês")
#         print("2. Espanhol")
#         print("3. Outra")
#         op = input('Informe a língua convalidada: ')
#
#         if op == '1':
#             lingua = 'Inglês'
#         elif op == '2':
#             lingua = 'Espanhol'
#         elif op == '3':
#             lingua = input('Informe a língua: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, exame, lingua
#
#     elif tipo == 15:# *** Troca de Projeto de Pesquisa ***
#         op_nivel = input('Nível do(a) discente - M p/ Mestrado & D p/ Doutorado: ')
#         nivel_discente = converteNivelString(op_nivel)
#         nome = input('Nome do(a) discente: ')
#         projeto_atual = input('Título do projeto atual: ')
#         novo_projeto = input('Título do novo projeto: ')
#
#         return n_res, data_res, ad_referendum, data_reuniao, nivel_discente, nome, projeto_atual, novo_projeto
#
#     elif tipo == 16:# *** Composição de Comissão ***
#         cont_membros = 0
#         membros = []
#         tipos_part = []
#         flag_membro = True
#
#         comissao = input('Informe o nome da comissão: ')
#
#         while flag_membro:
#             nome_membro = input('Informe o nome do membro: ')
#             membros.append(nome_membro)
#             cont_membros += 1
#
#             tipo_part = ''
#             print("Selecione uma opção: ")
#             print("1. Presidente")
#             print("2. Membro Titular")
#             print("3. Membro Suplente")
#             op = input('Informe o tipo de participação: ')
#
#             if op == '1':
#                 tipo_part = 'Presidente'
#             elif op == '2':
#                 tipo_part = 'Membro Titular'
#             elif op == '3':
#                 tipo_part = 'Membro Suplente'
#
#             tipos_part.append(tipo_part)
#
#             inserir_nova = input('Incluir mais um membro?(S/N)?: ')
#
#             if inserir_nova == 'N':
#                 flag_membro = False
#
#         return n_res, data_res, ad_referendum, data_reuniao, comissao, cont_membros, membros, tipos_part
#

def converteNivelString(nivel): # Converte a seleção do nivel(M e D) para MESTRADO ou DOUTORADO
    nivel.upper()
    if nivel == 'M':
        nivel = 'Mestrado'
    else:
        nivel = 'Doutorado'

    return nivel

def encurtaNome(nome):
    partes = nome.split()
    # Verifica se há mais de uma palavra no nome
    if len(partes) > 1:
        nome_encurtado = partes[0] + ' ' + partes[-1]
        return nome_encurtado.upper()
    else:
        return partes[0].upper() # Caso o nome seja composto por apenas uma palavra

