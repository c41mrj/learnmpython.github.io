from PIL import Image

# Abre una imagen
imagen = Image.open('./assets/conecta.png')

# Redimensiona la imagen
nueva_imagen = imagen.resize((300, 400))

# Guarda la nueva imagen
nueva_imagen.save('./assets/new_conecta.jpg')