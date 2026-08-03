# 🌙 NetflixSuspender

> Sabe quando o filme acaba, bate aquela preguiça de levantar pra
> desligar o PC e você acaba dormindo com ele ligado a noite toda?
> Isso acabou. 😴

Esse app simples com interface gráfica suspende (ou desliga) o seu PC
automaticamente assim que o tempo do filme/série termina.

<img width="419" height="438" alt="image (2)" src="https://github.com/user-attachments/assets/eda7e6d5-50f9-40ee-8e8c-31a26ebc1daf" />


Você digita a duração, escolhe a ação, aperta **Iniciar** — e pode
dormir tranquilo sabendo que o PC vai se cuidar sozinho.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Plataforma](https://img.shields.io/badge/plataforma-Windows-lightgrey)
![Licença](https://img.shields.io/badge/licença-MIT-green)

## ✨ Funcionalidades

- ⏱️ Defina a duração em horas e minutos
- 🌙 Escolha entre **Suspender** ou **Desligar** o PC
- ⏸️ Pause e retome a contagem a qualquer momento (útil se pausar o filme)
- ❌ Cancele o temporizador quando quiser
- 🪶 Zero dependências externas — usa só bibliotecas padrão do Python

## 🖥️ Como usar

### Pré-requisitos
- Python 3 instalado ([python.org](https://www.python.org/downloads/))

### Passo a passo
```bash
# clone o repositório
git clone https://github.com/seu-usuario/NetflixSuspender.git
cd NetflixSuspender

# rode o app
python temporizador.py
```

Na janela que abrir:
1. Digite as horas e minutos de duração do filme
2. Escolha **Suspender** ou **Desligar**
3. Clique em **Iniciar**
4. Aproveite o filme — o resto é com o app 🍿

<img width="2560" height="1440" alt="Cópia de PortifólioProjeto - Github - gknobeat" src="https://github.com/user-attachments/assets/4c954877-87de-40e5-a978-1686c4b65f7e" />


## 🛠️ Como funciona

O app usa `tkinter` (interface gráfica nativa do Python) para a contagem
regressiva e comandos nativos do Windows para suspender ou desligar:

- **Suspender**: `rundll32.exe powrprof.dll,SetSuspendState 0,1,0`
- **Desligar**: `shutdown /s /t 0`

## 🗺️ Próximos passos (ideias futuras)

- [ ] Detecção automática do fim do filme via extensão de navegador
- [ ] Suporte a Mac/Linux
- [ ] Notificação com contagem regressiva dos últimos segundos, com opção de cancelar

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, modificar
e distribuir.
