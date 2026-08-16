# audio-from-video-downloader

App simples em Python pra baixar música/áudio do YouTube e de centenas de outros sites, convertendo direto pra mp3.

## Requisitos

- Python 3.9+
- Não precisa instalar ffmpeg no sistema — ele já vem embutido via `imageio-ffmpeg`.

### Instalando o Python

**Windows**

1. Baixe o instalador em [python.org/downloads](https://www.python.org/downloads/).
2. Ao abrir o instalador, marque a opção **"Add python.exe to PATH"** antes de clicar em Install.
3. Confirme a instalação abrindo um novo terminal (PowerShell) e rodando:

```powershell
python --version
```

**Linux**

A maioria das distribuições já vem com Python. Se precisar instalar/atualizar:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

Confirme com:

```bash
python3 --version
```

> Nos exemplos de uso abaixo, no Linux use `python3` no lugar de `python`.

## Instalação

```bash
git clone <url-do-repo>
cd python-video-downloader
pip install -r requirements.txt
```

## Uso

Passando o link direto:

```bash
python main.py "https://www.youtube.com/watch?v=..."
```

Ou rodando sem argumento (ele pede o link):

```bash
python main.py
```

O mp3 é salvo em `downloads/`, na raiz do projeto.

## Sites suportados

Qualquer site suportado pelo [yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) (YouTube, SoundCloud, Instagram, TikTok, Vimeo, etc).

## Observações

- Sem instalação de runtime JS (Deno/Node/Bun): o app funciona normalmente, mas o yt-dlp pode ocasionalmente avisar que alguns formatos do YouTube ficaram indisponíveis por não conseguir resolver o desafio de JS do site. Não é necessário pra uso normal.
- Playlists: o app baixa só o vídeo/música do link informado, não a playlist inteira.
