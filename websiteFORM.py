import streamlit as st
import webbrowser
from io import BytesIO
import requests
import pandas as pd

st.set_page_config(
     page_title="Formulário de Cadastro e Interesses Cursos - ACT SP",
     page_icon=":date:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'mailto:informacoes.actsp@gmail.com',
         'Report a bug': "mailto:informacoes.actsp@gmail.com",
         'About': "#### Desenvolvedor: Massaki de O. Igarashi"
     }
 )

new=2
url = 'https://docs.google.com/forms/d/e/1FAIpQLScQyVpejEuPYzqCzUR9gF7lnRbz4UNF6rl8AOV8KNc3o84V4g/formResponse?&submit=Submit?usp=pp_url&entry.884978944= - '

caminhoCursos = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMMr7n2xkeFdK0eg_izhe1NN1QfgaLZ9OpBHrTMqgJ7ybMheGVvfrHcENYdl_68rh5_GNanRVutN0p/pub?gid=202745307&single=true&output=csv')
data = caminhoCursos.content
df = pd.read_csv(BytesIO(data), index_col=0)
df.columns = ['Descricao','SituacaoCurso','Responsavel', 'DataInicio','DataTermino','CargaHoraria','HoraSEG','HoraTER','HoraQUA','HoraQUI','HoraSEX','HoraSAB','HoraDOM','OBScurso']

#st.write(df.head())
st.title('Cadastre seu interesse em cursos - ACT SP ')
st.subheader('Entraremos em contato com você em breve!')

EmBreve = df['SituacaoCurso']=='Em breve'
df01 = df[EmBreve]
option = st.multiselect('Selecione o(s) curso(s) desejado(s):',df01['Descricao']+ '( Início: ' + df01['DataInicio'] + ', término: ' + df01['DataTermino'] + ')' )
if option:     
    st.write('Você selecionou o(s) curso(s): ')
    st.write(option)
    url = url + '&entry.1816236222=' + str(option)

txtNome = st.text_input("Digite seu nome completo 👇")
if txtNome:
    url= url + '&entry.924147543=' + txtNome
txtMAIL = st.text_input("Digite seu e-mail 👇")
if txtMAIL:
    url = url + '&entry.2042220506=' + txtMAIL
txtCPF = st.text_input("Digite seu CPF 👇")
if txtCPF:
    url = url + '&entry.1192625439=' + txtCPF
sliderIDADE = st.slider('Selecione sua idade', 1, 100, 16)
if sliderIDADE:
    url = url + '&entry.2103631409=' + str(sliderIDADE) + '&entry.2013928071=Lead'
txtFONE = st.text_input("Digite seu Telefone Celular (DDD) 99999-9999 👇")
if txtFONE:
    url = url + '&entry.1286066518=' + txtFONE
    #+'&entry.198265004='  + str(txtOBS)
    #+'&entry.374343962='  + str(txtPIX)
    #+'&entry.1226253104=' + str(txtPGTO)    
if st.button('Confirmar 👇'):
    webbrowser.open(url,new=new)

