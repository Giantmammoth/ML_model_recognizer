from PIL import Image

# Fonction pour découper l'image en parties individuelles
def split_image(image):
    symbols = []
    width, height = image.size
    left = 0
    right = 0
    top = 0
    bottom = height

    while right < width:
        # Recherche de la colonne contenant du contenu
        while right < width and is_empty_column(image, right):
            right += 1
        
        # Détection de la colonne vide suivante
        left = right
        while right < width and not is_empty_column(image, right):
            right += 1

        # Découpage de la partie contenant un symbole
        if left < right:
            symbol = image.crop((left, top, right, bottom))
            symbols.append(symbol)

    return symbols

# Fonction pour vérifier si une colonne de l'image est vide
def is_empty_column(image, column_index):
    width, height = image.size
    for y in range(height):
        pixel = image.getpixel((column_index, y))
        if pixel != 255:  # Vérifier si le pixel est noir
            return False
    return True

# Charger l'image de l'équation
image = Image.open('equation.png')

# Convertir en niveaux de gris
image = image.convert('L')

# Seuillage pour extraire les symboles noirs
threshold = 128
image = image.point(lambda x: 0 if x < threshold else 255, '1')

# Découper l'image en parties individuelles
symbols = split_image(image)

# Afficher les parties découpées
for i, symbol in enumerate(symbols):
    symbol.show()

for i, symbol in enumerate(symbols):
    symbol.save(f"symbole_{i}.png")

