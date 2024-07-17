from PIL import Image

# Abre una imagen
imagen = Image.open('./assets/inicio.png')

# Redimensiona la imagen
nueva_imagen = imagen.resize((800, 1076))

# Guarda la nueva imagen
nueva_imagen.save('./assets/new_inicio.jpg')