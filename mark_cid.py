import pandas as pd
import numpy as np
import zipfile
import streamlit as st
from datetime import date

#  qual exame não pode ser feito por  um diabético?

st.set_page_config(
    page_title="Blue AI - Klivo",
    page_icon="🔬"
)

zf_2 = zipfile.ZipFile('df_porto.zip') 

@st.cache_data() #Ler base de procedimentos por beneficiários
def get_data():
	return pd.read_csv(zf_2.open("df_porto.csv"))
df = get_data()

st.title('🔬 Teste de classificação de diabetes por procedimentos passados')
st.caption('Feito com 🧠 por [Blue AI](https://blueai.com.br/)')
Intro, Group_1, Group_2, Group_3, Docs = st.tabs(["Intro", "Grupo de teste 1", "Grupo de teste 2", "Grupo de teste 3", "Documentação"])

df['id_pessoa'] = df['id_pessoa'].astype(str)

with Intro:
	st.info('Este app demonstra classificações de diabetes para beneficiários de planos de saúde através do histórico de procedimentos realizados por cada um. Comece selecionando um grupo de teste acima para avaliar as respectivas classificações, anote os seus comentários, sugestões e principalmente os seus feedbacks. **Toda inteligência artificial um dia começou a partir de uma inteligência humana, dessa forma, junto com a [Klivo](https://www.klivo.com/), a Blue está na segunda versão de um modelo de *machine learning* para diabetes**. \n\n Ainda, na última aba acima, você encontrará a descrição de variáveis e suas combinações usadas para a construção do classificador de diabetes, assim como fontes e *benchmarks* de publicações científicas similares.')

with Group_1:
	df['id_pessoa'].replace({'36651': 'Indivíduo 1', '109256':'Indivíduo 2', '211794':'Indivíduo 3'}, inplace=True)

	# lista_pessoa = ['-']
	# for x in df['id_pessoa'].unique():
	# 	lista_pessoa.append(x)

	# lista_pessoa.sort()

	lista_pessoa = ['Indivíduo 1', 'Indivíduo 2', 'Indivíduo 3']
	pessoa = st.selectbox('Selecione o beneficiário para avaliar o seu histórico:', lista_pessoa, index=0, format_func=str, key="Group_1")

	if pessoa != '-':
		df_aux = df[df['id_pessoa'] == pessoa]

		# visual = st.selectbox('Visualizar:', ['Subgrupos', 'Procedimentos', 'Histórico'], index=0, format_func=str, key="Group_1_Options")
		
		# if visual == 'Subgrupos':
		# 	st.subheader('Subgrupos únicos:')
		# 	st.table(df_aux['Subgrupo'].unique())
		# elif visual == 'Procedimentos':
		# 	st.subheader('Procedimentos únicos:')
		# 	st.table(df_aux['DescricaoProcedimentoFinal'].unique())
		# elif visual == 'Histórico':
		st.markdown('\n\n')
		# today = pd.Timestamp("today")
		# df['dt_nascimento'] =  (today - pd.to_datetime(df['dt_nascimento']))/365

		st.write('##### Histórico completo:')
		st.table(df_aux[['dt_nascimento', 'dt_utilizacao', 'proc_tuss']].sort_values('dt_utilizacao', ascending = False))

	else:
		pass

with Group_2:
	df['id_pessoa'].replace({'48658': 'Indivíduo 4', '49886':'Indivíduo 5', '173960':'Indivíduo 6'}, inplace=True)

	# lista_pessoa = ['-']
	# for x in df['id_pessoa'].unique():
	# 	lista_pessoa.append(x)

	# lista_pessoa.sort()

	lista_pessoa = ['Indivíduo 4', 'Indivíduo 5', 'Indivíduo 6']
	pessoa = st.selectbox('Selecione o beneficiário para avaliar o seu histórico:', lista_pessoa, index=0, format_func=str, key="Group_2")

	if pessoa != '-':
		df_aux = df[df['id_pessoa'] == pessoa]

		# visual = st.selectbox('Visualizar:', ['Subgrupos', 'Procedimentos', 'Histórico'], index=0, format_func=str, key="Group_2_Options")
		
		# if visual == 'Subgrupos':
		# 	st.subheader('Subgrupos únicos:')
		# 	st.table(df_aux['Subgrupo'].unique())
		# elif visual == 'Procedimentos':
		# 	st.subheader('Procedimentos únicos:')
		# 	st.table(df_aux['DescricaoProcedimentoFinal'].unique())
		# elif visual == 'Histórico':
		st.markdown('\n\n')
		st.write('##### Histórico completo:')
		st.table(df_aux[['dt_nascimento', 'dt_utilizacao', 'proc_tuss']].sort_values('dt_utilizacao', ascending = False))

	else:
		pass

with Group_3:
	df['id_pessoa'].replace({'111633': 'Indivíduo 7', '73137':'Indivíduo 8', '83784':'Indivíduo 9'}, inplace=True)

	# lista_pessoa = ['-']
	# for x in df['id_pessoa'].unique():
	# 	lista_pessoa.append(x)

	# lista_pessoa.sort()

	lista_pessoa = ['Indivíduo 7', 'Indivíduo 8', 'Indivíduo 9']
	pessoa = st.selectbox('Selecione o beneficiário para avaliar o seu histórico:', lista_pessoa, index=0, format_func=str, key="Group_3")

	if pessoa != '-':
		df_aux = df[df['id_pessoa'] == pessoa]

		# visual = st.selectbox('Visualizar:', ['Subgrupos', 'Procedimentos', 'Histórico'], index=0, format_func=str, key="Group_2_Options")
		
		# if visual == 'Subgrupos':
		# 	st.subheader('Subgrupos únicos:')
		# 	st.table(df_aux['Subgrupo'].unique())
		# elif visual == 'Procedimentos':
		# 	st.subheader('Procedimentos únicos:')
		# 	st.table(df_aux['DescricaoProcedimentoFinal'].unique())
		# elif visual == 'Histórico':
		st.markdown('\n\n')
		st.write('##### Histórico completo:')
		st.table(df_aux[['dt_nascimento', 'dt_utilizacao', 'proc_tuss']].sort_values('dt_utilizacao', ascending = False))

	else:
		pass

with Docs:
	st.write(
        """
		Para a construção das variáveis usamos análise descritiva, incluindo frequência, medida de taxa de realização de um novo procedimento, porcentagem, média e soma de cada informação descrita na lista abaixo. Ainda, consideremos também protocolos retirados de artigos ciêntíficos publicadas que ilustram mais sobre o perfil de utilização de um diabético.
		""")
	
	st.markdown('\n\n')
	st.warning('**Protocolos de utilização de um paciente de diabetes**', icon="🩺")
	st.write(
        """
		```
		Hemoglobina glicada         Se diabetes controlada, a cada 6 meses. Se fora de controle, 3 meses. 
		Microalbuminúria            A cada 6 meses.
		Colesterol total            A cada 12 meses.
		LDL                         A cada 12 meses.
		HDL                         A cada 12 meses.
		Glicose                     A cada 12 meses.
		Creatinina                  A cada 12 meses.
		Triglicerídeos              A cada 12 meses.
		Retinografia monocular      A cada 12 meses.

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Procedimentos TUSS**', icon="🔬")
	st.write(
        """
		```
		40302075	Hemoglobina glicada (a1 total) - pesquisa e/ou dosagem
		40302733	Hemoglobina glicada (fração a1c) - pesquisa e/ou dosagem
		40301150	Ácido úrico - pesquisa e/ou dosagem
		40302580	Uréia - pesquisa e/ou dosagem
		40311171	Microalbuminúria
		40302385	Proteínas totais albumina e globulina - pesquisa e/ou dosagem
		40301630	Creatinina - pesquisa e/ou dosagem
		40302040	Glicose - pesquisa e/ou dosagem
		40301605	Colesterol total - pesquisa e/ou dosagem
		40301591	Colesterol (LDL) - pesquisa e/ou dosagem. Veja como é fácil consultar a Terminologia Unificada da Saúde Suplementar …
		40302750	Perfil lipídico / lipidograma (lípidios totais, colesterol, triglicerídios e eletroforese lipoproteínas)
		40302032	Glicemia após sobrecarga com dextrosol ou glicose - pesquisa e/ou dosagem
		40302024	Gasometria + Hb + Ht + Na + K + Cl + Ca + glicose + lactato (quando efetuado no gasômetro) - pesquisa e/ou dosagem
		10101012	Consulta em consultório (no horário normal ou preestabelecido)
		10101039	Consulta em pronto socorro
		40814220	TROMBECTOMIA
		40302709	Teste oral de tolerância à glicose - 2 dosagens
		41301439	Fundoscopia sob medríases - binocular
		41301315	Retinografia (só honorário) monocular

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Grupo por obejetivo de análise**', icon="🔬")
	st.write(
        """
		```
		Exames de Hemoglobina Glicada	40302075; 40302733
		Exames de Saúde Renal	        40301150; 40302580; 40311171; 40302385; 40301630
		Exames de Colesterol	        40301605; 40301591; 40302750
		Exames de Açúcar no Sangue      40302040

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Gupo por modo de realização de exames**', icon="🔬")
	st.write(
        """
		```
		Por Urina                       40301150; 40311171
		Por Coleta de Sangue	        40302075; 40302733; 40302385; 40301630; 40301605; 40301591; 40302750; 40302040
		Por Coleta de Sangue e Urina	40302580

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Subgrupos TUSS**', icon="🔬")
	st.write(
        """
		```
		Consultas
		Consulta em Pronto Socorro
		REABILITAÇÕES - SESSÕES DE PROCEDIMENTOS AMBULATORIAIS
		MONITORIZAÇÕES AMBULATORIAIS
		AVALIAÇÕES / ACOMPANHAMENTOS AMBULATORIAIS
		TERAPIA CLÍNICA AMBULATORIAL
		AVALIAÇÕES / ACOMPANHAMENTOS DE PROCEDIMENTOS CLÍNICOS HOSPITALARES
		MONITORIZAÇÕES DE PROCEDIMENTOS CLÍNICOS HOSPITALARES
		REABILITAÇÕES - SESSÕES DE PROCEDIMENTOS CLÍNICOS HOSPITALARES
		TERAPIA CLÍNICA HOSPITALAR
		BOCA
		NERVOS PERIFÉRICOS
		VAGINA
		RIM, BACINETE E SUPRA-RENAL
		PÂNCREAS
		PÉ
		PERNA
		TORNOZELO
		CIRURGIA VENOSA
		CIRURGIA ARTERIAL
		ACESSOS VASCULARES
		RENAL
		BIOQUÍMICA
		URINÁLISE
		SISTEMA URINÁRIO

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Grupos TUSS**', icon="🔬")
	st.write(
        """
		```
		CONSULTAS
		PROCEDIMENTOS CLÍNICOS AMBULATORIAIS
		PROCEDIMENTOS CLÍNICOS HOSPITALARES
		PELE E TECIDO CELULAR SUBCUTÂNEO ANEXOS
		OLHOS
		SISTEMA MÚSCULO ESQUELÉTICO E ARTICULAÇÕES
		SISTEMA CÁRDIO- CIRCULATÓRIO
		SISTEMA URINÁRIO
		SISTEMA NERVOSO - CENTRAL E PERIFÉRICO
		MEDICINA LABORATORIAL
		CABEÇA E PESCOÇO
		SISTEMA DIGESTIVO E ANEXOS
		SISTEMA GENITAL E REPRODUTOR FEMININO

		```
		"""
			)
	
	st.markdown('\n\n')
	st.warning('**Fontes**', icon="📚")
	st.markdown("""
	*"Diabetes was associated with an 87% increase in outpatient visits, a 52% increase in hospital admissions and a 33% increase in accident and emergency department attendances."* \n\n
	• [Health service utilization and related costs attributable to diabetes](https://sci-hub.se/https://onlinelibrary.wiley.com/doi/10.1111/dme.13806) \n\n \n\n
	*"People with diabetes were less likely to report no emergency department visits in the last year than the general population (70% vs. 80%) "* \n\n
	• [Health Care Utilization and Costs of Diabetes](https://www.ncbi.nlm.nih.gov/books/NBK567979/) \n\n
	*"Participants with diabetes complications had 2 times higher odds of specialist visit(OR: 2.55; CI: 2.05–3.16),5 times higher odds of ER visit (OR: 5.63; CI: 3.79–8.37), and 3 times higher odds of hospitalization (OR: 3.68; CI: 2.84–4.73) than participants without diabetes complications"* \n\n
	• [Patient-perceived service needs and health care utilization in people with type 2 diabetes](https://journals.lww.com/md-journal/fulltext/2020/05220/patient_perceived_service_needs_and_health_care.71.aspx)""")



# if st.button('Salvar resposta'):
# 	st.balloons()
# 	st.success('Resposta salva!')



