# python-video-downloader

App simples em Python pra baixar música/áudio do YouTube e de centenas de outros sites, convertendo direto pra mp3.

## Requisitos

- Python 3.9+
- Não precisa instalar ffmpeg no sistema — ele já vem embutido via `imageio-ffmpeg`.

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
