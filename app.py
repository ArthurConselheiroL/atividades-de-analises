#--------------------------------------------------------------------------------------------------------------------
# ATIVIDADE 1 

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Baixa os recursos necessários para a tokenização do NLTK
nltk.download('punkt_tab', quiet=True)

# Configuração da interface do Streamlit
st.title("Tokenização de Texto em Português")
st.write("Insira um texto abaixo para dividi-lo em palavras individuais (tokens).")

# Campo para o usuário digitar o texto em português
texto_usuario = st.text_area("Digite seu texto aqui:", "O processamento de linguagem natural é incrível!")

# Botão para executar a tokenização
if st.button("Tokenizar Texto"):
    
    # Executa a tokenização por palavras usando o NLTK
    tokens = word_tokenize(texto_usuario, language='portuguese')
    
    # Exibe o resultado e a lista de tokens gerada
    st.write("---")
    st.subheader("Resultado da Tokenização:")
    st.write(f"**Total de tokens encontrados:** {len(tokens)}")
    st.write(tokens)



#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 2 

import streamlit as st
from collections import Counter
import re

# Configuração da interface do Streamlit
st.title("Análise de Frequência de Palavras")
st.write("Insira um texto em português para contar a frequência de cada palavra.")

# Campo para o usuário digitar o texto
texto_usuario = st.text_area("Digite seu texto aqui:", "O processamento de linguagem natural é muito legal. O aprendizado é constante!")

# Botão para executar a análise de frequência
if st.button("Analisar Frequência"):
    
    # Converte o texto para minúsculas para padronizar a contagem
    texto_minusculo = texto_usuario.lower()
    
    # Usa expressão regular para remover pontuações e extrair apenas as palavras
    palavras = re.findall(r'\b\w+\b', texto_minusculo)
    
    # Utiliza o Counter para contar a ocorrência de cada palavra automaticamente
    frequencia = Counter(palavras)
    
    # Exibe o resultado na tela de forma organizada
    st.write("---")
    st.subheader("Resultado da Frequência:")
    
    # Transforma o resultado em um dicionário legível e exibe no Streamlit
    st.write(dict(frequencia.most_common()))


#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 3

import streamlit as st

# Configuração básica da interface do Streamlit
st.title("Identificador de Palavras Negativas")
st.write("Digite um texto em português para verificar se ele contém termos negativos predefinidos.")

# Campo para o usuário digitar o texto
texto_usuario = st.text_area("Digite seu texto aqui:", "O sistema apresentou um erro terrível e o resultado foi ruim.")

# Botão para iniciar a verificação
if st.button("Verificar Texto"):
    
    # Converte o texto para minúsculas para facilitar a busca exata
    texto_minusculo = texto_usuario.lower()
    
    # Lista estática de palavras negativas para buscar no texto
    palavras_negativas = ["ruim", "péssimo", "pessimo", "erro", "terrível", "terrivel", "falha", "pior"]
    
    # Cria uma lista para armazenar os termos negativos encontrados
    encontradas = []
    
    # Varre a lista de termos e verifica se cada um está presente no texto
    for palavra in palavras_negativas:
        if palavra in texto_minusculo:
            encontradas.append(palavra)
            
    # Exibe o resultado com base na presença ou ausência de termos negativos
    st.write("---")
    if encontradas:
        st.subheader("⚠️ Alerta de Mensagem Negativa")
        st.write(f"Foram identificadas as seguintes palavras negativas: **{', '.join(encontradas)}**")
    else:
        st.subheader("✅ Mensagem Limpa")
        st.write("Nenhuma palavra negativa comum foi identificada no texto analisado.")

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 4

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Baixa os recursos necessários para tokenização e stopwords
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Configuração da interface do Streamlit
st.title("Remoção de Stopwords em Português")
st.write("Remova palavras comuns (artigos, preposições, etc.) para limpar seu texto.")

# Campo de entrada para o usuário digitar o texto em português
texto_usuario = st.text_area("Digite seu texto aqui:", "O processamento de linguagem natural é uma área com muito futuro.")

# Botão para processar o texto
if st.button("Remover Stopwords"):
    
    # Define a lista de palavras vazias (stopwords) em português
    palavras_vazias = set(stopwords.words('portuguese'))
    
    # Divide o texto do usuário em tokens (palavras individuais)
    tokens = word_tokenize(texto_usuario, language='portuguese')
    
    # Filtra os tokens, mantendo apenas os que não estão na lista de stopwords
    # Converte para minúsculas apenas para a comparação correta
    tokens_limpos = [palavra for palavra in tokens if palavra.lower() not in palavras_vazias]
    
    # Reconstrói o texto unindo os tokens limpos por espaços
    texto_limpo = " ".join(tokens_limpos)
    
    # Exibe os resultados na tela
    st.write("---")
    st.subheader("Texto Limpo (Sem Stopwords):")
    st.write(texto_limpo)
    
    st.subheader("Tokens Removidos:")
    removidos = [palavra for palavra in tokens if palavra.lower() in palavras_vazias]
    st.write(list(set(removidos)))

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 5

import streamlit as st

# Configuração da interface do Streamlit
st.title("Classificador Simples de Sentimento")
st.write("Digite um comentário em português para classificá-lo como Positivo, Negativo ou Neutro.")

# Campo de entrada para o texto do usuário
texto_usuario = st.text_area("Seu comentário:", "Este produto é muito bom e o atendimento foi excelente!")

# Botão para iniciar a classificação
if st.button("Classificar Sentimento"):
    
    # Converte o texto para minúsculas para padronizar a busca
    texto_minusculo = texto_usuario.lower()
    
    # Listas básicas de palavras de referência
    palavras_positivas = ["bom", "ótimo", "otimo", "excelente", "maravilhoso", "gostei", "feliz", "recomendo"]
    palavras_negativas = ["ruim", "péssimo", "pessimo", "horrível", "horrivel", "odiei", "reclamar", "erro"]
    
    # Contadores de pontuação
    score_positivo = 0
    score_negativo = 0
    
    # Conta quantas palavras positivas estão no texto
    for palavra in palavras_positivas:
        if palavra in texto_minusculo:
            score_positivo += 1
            
    # Conta quantas palavras negativas estão no texto
    for palavra in palavras_negativas:
        if palavra in texto_minusculo:
            score_negativo += 1
            
    # Lógica condicional para definir o sentimento final
    if score_positivo > score_negativo:
        resultado = "Positivo"
        cor = "green"
    elif score_negativo > score_positivo:
        resultado = "Negativo"
        cor = "red"
    else:
        resultado = "Neutro"
        cor = "gray"
        
    # Exibe o resultado formatado na tela
    st.write("---")
    st.subheader(f"Sentimento Identificado: :{cor}[{resultado}]")
    st.write(f"**Palavras positivas encontradas:** {score_positivo}")
    st.write(f"**Palavras negativas encontradas:** {score_negativo}")

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 6

import streamlit as st

# Configuração da interface do Streamlit
st.title("Roteador de Atendimento Automatizado")
st.write("Digite sua dúvida ou problema em português para ser direcionado ao setor correto.")

# Campo para o usuário digitar a mensagem
mensagem_usuario = st.text_area("Digite sua mensagem:", "Quero cancelar minha assinatura e ver o boleto de pagamento.")

# Botão para processar a mensagem e direcionar o atendimento
if st.button("Enviar Mensagem"):
    
    # Converte o texto para minúsculas para padronizar a busca pelas palavras-chave
    mensagem_minusculo = mensagem_usuario.lower()
    
    # Cria uma lista para guardar os setores responsáveis identificados
    setores = []
    
    # Condicional para verificar palavras-chave do setor de Cancelamento
    if "cancelar" in mensagem_minusculo or "cancelamento" in mensagem_minusculo or "excluir" in mensagem_minusculo:
        setores.append("❌ **Setor de Retenção e Cancelamentos**")
        
    # Condicional para verificar palavras-chave do setor de Suporte Técnico
    if "erro" in mensagem_minusculo or "falha" in mensagem_minusculo or "quebrou" in mensagem_minusculo or "bug" in mensagem_minusculo:
        setores.append("🛠️ **Suporte Técnico**")
        
    # Condicional para verificar palavras-chave do setor Financeiro
    if "pagamento" in mensagem_minusculo or "boleto" in mensagem_minusculo or "cartão" in mensagem_minusculo or "fatura" in mensagem_minusculo:
        setores.append("💰 **Setor Financeiro**")
        
    # Exibe a resposta com o direcionamento correto
    st.write("---")
    if setores:
        st.subheader("Encaminhando seu atendimento:")
        for setor in setores:
            st.write(f"Sua mensagem foi enviada para o {setor}.")
    else:
        # Caso nenhuma palavra-chave seja encontrada, envia para o atendimento geral
        st.subheader("Encaminhando seu atendimento:")
        st.write("🤖 Nenhuma palavra-chave específica foi detectada. Direcionando para o **Atendimento Geral / Atendente Humano**.")

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 7 

import streamlit as st
from collections import Counter
import re

# Configuração da interface do Streamlit
st.title("Termos Mais Frequentes em Reclamações")
st.write("Cole o texto da reclamação em português para identificar as palavras mais repetidas.")

# Campo de entrada para o texto do cliente
texto_usuario = st.text_area("Texto da reclamação:", "O produto veio com defeito. O produto não liga e o suporte não responde.")

# Botão para processar a frequência
if st.button("Analisar Palavras"):
    
    # Converte tudo para minúsculas para evitar duplicidade (ex: "O" e "o")
    texto_minusculo = texto_usuario.lower()
    
    # Usa expressão regular para extrair apenas palavras, descartando pontuações
    palavras = re.findall(r'\b\w+\b', texto_minusculo)
    
    # Contabiliza a frequência de cada palavra de forma automática
    contador = Counter(palavras)
    
    # Obtém a lista de palavras ordenadas da mais frequente para a menos frequente
    palavras_ordenadas = contador.most_common()
    
    # Exibe os resultados na tela
    st.write("---")
    st.subheader("Ranking de Palavras Mais Frequentes:")
    
    # Loop simples para exibir cada palavra e sua respectiva contagem
    for palavra, frequencia in palavras_ordenadas:
        st.write(f"• **{palavra}**: apareceu {frequencia}x")

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 8

import streamlit as st

# Configuração da interface do Streamlit
st.title("Classificador de Mensagens de Clientes")
st.write("Digite a mensagem em português para classificá-la na categoria correta.")

# Campo para o usuário digitar a mensagem
mensagem_usuario = st.text_area("Mensagem do cliente:", "Não consigo acessar minha conta, a página dá erro.")

# Botão para executar a classificação
if st.button("Classificar Mensagem"):
    
    # Converte o texto para minúsculas para padronizar a busca pelas palavras-chave
    mensagem_minusculo = mensagem_usuario.lower()
    
    # Listas de palavras-chave para cada categoria
    chaves_suporte = ["erro", "senha", "acesso", "sistema", "login", "bug", "lentidão", "site"]
    chaves_financeiro = ["boleto", "pagamento", "fatura", "cartão", "cobrança", "reembolso", "preço"]
    
    # Variável para armazenar a categoria final
    categoria = "Outro"
    
    # Verifica se há alguma palavra-chave de Suporte Técnico na mensagem
    for palavra in chaves_suporte:
        if palavra in mensagem_minusculo:
            categoria = "Suporte Técnico"
            break  # Interrompe o loop se encontrar correspondência
            
    # Se ainda for 'Outro', verifica se há alguma palavra-chave de Financeiro
    if categoria == "Outro":
        for palavra in chaves_financeiro:
            if palavra in mensagem_minusculo:
                categoria = "Financeiro"
                break
                
    # Exibe o resultado da classificação na tela
    st.write("---")
    st.subheader("Resultado da Classificação:")
    
    if categoria == "Suporte Técnico":
        st.info(f"Categoria: 🛠️ **{categoria}**")
    elif categoria == "Financeiro":
        st.success(f"Categoria: 💰 **{categoria}**")
    else:
        st.warning(f"Categoria: 📬 **{categoria}** (Encaminhado para triagem geral)")

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 9

import streamlit as st
import string

# Configuração da interface do Streamlit
st.title("Limpeza Básica de Texto")
st.write("Insira um texto em português para remover pontuações e padronizar tudo em minúsculas.")

# Campo para o usuário digitar o texto
texto_usuario = st.text_area("Digite seu texto aqui:", "Olá, Mundo! Este é um teste: funcionando 100%, certo?")

# Botão para processar a limpeza do texto
if st.button("Limpar Texto"):
    
    # Converte todo o texto para letras minúsculas
    texto_minusculo = texto_usuario.lower()
    
    # Cria uma tabela de mapeamento para remover todos os caracteres de pontuação
    # string.punctuation contém caracteres como: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    tabela_limpeza = str.maketrans('', '', string.punctuation)
    texto_limpo = texto_minusculo.translate(tabela_limpeza)
    
    # Exibe o resultado limpo na tela
    st.write("---")
    st.subheader("Texto Processado:")
    st.write(texto_limpo)

#--------------------------------------------------------------------------------------------------------------------
#ATIVIDADE 10

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Baixa os recursos necessários para a tokenização do NLTK
nltk.download('punkt', quiet=True)

# Configuração da interface do Streamlit
st.title("Tokenização + Análise de Sentimento")
st.write("Digite um texto em português para tokenizar e classificar o sentimento.")

# Campo para o usuário digitar o texto
texto_usuario = st.text_area("Digite seu texto aqui:", "O dia está lindo e eu estou muito feliz!")

# Botão para iniciar o processamento
if st.button("Analisar Texto"):
    
    # Realiza a tokenização do texto em português
    tokens = word_tokenize(texto_usuario, language='portuguese')
    
    # Listas básicas de palavras para referência de sentimento
    palavras_positivas = ["bom", "ótimo", "otimo", "excelente", "maravilhoso", "feliz", "lindo", "legal"]
    palavras_negativas = ["ruim", "péssimo", "pessimo", "horrível", "horrivel", "triste", "erro", "pior"]
    
    # Contadores para os sentimentos
    score_positivo = 0
    score_negativo = 0
    
    # Percorre cada token encontrado para verificar o sentimento
    for token in tokens:
        token_minusculo = token.lower() # Padroniza o token em minúsculo
        if token_minusculo in palavras_positivas:
            score_positivo += 1
        elif token_minusculo in palavras_negativas:
            score_negativo += 1
            
    # Lógica condicional para definir a classificação final
    if score_positivo > score_negativo:
        resultado = "Positivo"
        cor = "green"
    elif score_negativo > score_positivo:
        resultado = "Negativo"
        cor = "red"
    else:
        resultado = "Neutro"
        cor = "gray"
        
    # Exibe os resultados na tela
    st.write("---")
    
    # Exibe a lista de tokens gerada
    st.subheader("Tokens Encontrados:")
    st.write(tokens)
    
    # Exibe o veredito final do sentimento
    st.subheader(f"Sentimento Final: :{cor}[{resultado}]")
    st.write(f"Contagem — Positivas: {score_positivo} | Negativas: {score_negativo}")