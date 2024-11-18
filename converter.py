from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

block_pick = 1  
blocks = {
    1: color.rgb(128, 128, 128), 
    2: color.rgb(34, 139, 34),   
    3: color.rgb(139, 69, 19),    
    4: color.rgb(128, 128, 128),  
    5: color.rgb(255, 255, 255), 
    6: color.rgb(255, 69, 0),     
    7: color.rgb(0, 0, 255),     
}

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube', 
            origin_y=0.5,
            texture='white_cube',
            color=blocks[block_pick],  # Blokning rangi tanlangan bo'ladi
            highlight_color=color.lime,
            collider='box',
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal)  # Blok qo'yish
            elif key == 'right mouse down':
                destroy(self)  # Blokni yo'q qilish

# Asosiy funksiya, dastlabki bloklarni yaratish
for z in range(20):
    for x in range(20):
        Voxel(position=(x, 0, z))  # Yerdagi bloklarni yaratish

# O'yinchini yaratish (1-shaxs ko'rinishidagi harakat boshqaruvi)
player = FirstPersonController()

def input(key):
    global block_pick
    if key == '1':
        block_pick = 1  # To'pg'ir tosh
    elif key == '2':
        block_pick = 2  # O't yashil
    elif key == '3':
        block_pick = 3  # Tuproq jigarrang
    elif key == '4':
        block_pick = 4  # Kulrang tosh
    elif key == '5':
        block_pick = 5  # Qor oq
    elif key == '6':
        block_pick = 6  # Lava qizil
    elif key == '7':
        block_pick = 7  # Suv moviy

app.run()
