# Password Manager

Aplicação desktop desenvolvida em Python com Tkinter para gerir palavras‑passe de forma simples e rápida. Permite gerar *strong passwords*, guardar credenciais localmente e pesquisar entradas existentes.

## ✨ Funcionalidades

- **Geração de passwords** com letras, números e símbolos  
- **Cópia automática** da password para o clipboard  
- **Armazenamento local** de credenciais num ficheiro JSON  
- **Pesquisa rápida** por website e email/username  
- **Pop‑ups de validação** para avisos e confirmações  
- Interface gráfica simples construída com Tkinter

## 📁 Estrutura dos dados

As credenciais são guardadas num ficheiro JSON dentro da pasta `data/`, organizadas por website, contendo email/username e password associados.

## 🖥️ Interface

A interface inclui:
- Campos para website, email/username e password  
- Botões para gerar password, adicionar credenciais e pesquisar  
- Logótipo exibido através de um canvas Tkinter

## 🚀 Como funciona

1. O utilizador introduz o website e email/username.  
2. Pode gerar uma *strong password* automaticamente.  
3. Ao guardar, os dados são confirmados via pop‑up e armazenados no ficheiro JSON.  
4. A pesquisa verifica se existe uma entrada correspondente e mostra os dados num pop‑up.

## 🔒 Nota

As credenciais são guardadas **localmente**. Não existe qualquer envio de dados para serviços externos.