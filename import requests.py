import requests
from PIL import Image
from io import BytesIO

def get_pokemon_sprite(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    r = requests.get(url)
    if r.status_code != 200:
        print("❌ Pokémon bulunamadı!")
        return

    data = r.json()
    sprite_url = data["sprites"]["other"]["official-artwork"]["front_default"]

    if sprite_url is None:
        print("❌ Bu Pokémon'un resmi bulunmuyor.")
        return

    print("📥 Sprite indiriliyor:", sprite_url)
    img_data = requests.get(sprite_url).content

    image = Image.open(BytesIO(img_data))
    image.show()  # OS görüntüleyicisinde açar
    print("✔ Görsel açıldı!")

# --- Kullanım ---
pokemon_name = input("Pokemon ismi girin: ")
get_pokemon_sprite(pokemon_name)
