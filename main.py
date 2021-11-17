from ursina import *
from ursina.prefabs.first_person_controller import *

#def

def update():
    print(player.position)
    if player.y <-1:
        player.position = (-16,0,18)

#enddef

application.development_mode = True #Turn off Development mode
app = Ursina() #Call Ursina Engine for the first time
window.exit_button.enabled = False #Disable exit button
window.fps_counter.enabled = False #Disable FPS Counter
window.cog_button.enabled = False #Disable Dev menu
window.fullscreen = True #Fullscreen
window.borderless = True #Borderless

#beginbody

maze = Entity(model='maze',
              texture='brick',
              scale=20,
              collider='mesh'
              )

sky = Entity(model='sky_dome',
             scale=999,
             color=rgb(51,187,255),
             )

#endbody

player = FirstPersonController(position=(-16,0,18)) #Vec3(-16.1705, 0, 18.828)

app.run()
