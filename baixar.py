
import urllib.request
import ssl

# Ignorar a verificação de segurança (SSL) da rede
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Link mestre atualizado
url = "https://commons.wikimedia.org/wiki/Special:FilePath/Brazil_Blank_Map.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

print("A descarregar o código puro do mapa...")
with urllib.request.urlopen(req, context=ctx) as response:
    texto_svg = response.read().decode('utf-8')
    with open("mapa_limpo.txt", "w", encoding="utf-8") as f:
        f.write(texto_svg)
        
print("SUCESSO! O ficheiro 'mapa_limpo.txt' foi criado na sua pasta.")