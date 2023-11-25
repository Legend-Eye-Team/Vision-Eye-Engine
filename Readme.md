# Document
## Setup 
Create A Project
```
VisionE init <Name>
cd <Name>
python Run.py
```
## Code 
### Zone
In 'Main.py', have some zone. There are:
* Import (Import library and Engine)
* Initial (Create variable, Block, Gui, ...)
* Functional (Create function)
* Main (Main Function)
    - 'display.Input()' get data input
    - 'display.Update' update everything
    - 'Code' this is zone for function, code, ...
    - 'display.Render' render Block, Gui
### Create a block

#### Rectangle
##### Initial
```
name_of_block = Rectangle(display,x_pos,y_pos,width,height)
```

##### Method
```
block = Rectangle(display,250,250,100,100)

# Change new size
block.Transform(50,50) 

# Change new position
block.setPoint(100,100)

# Check Human is touched
block.isTouched(player)

# Set attribute
# isFlat: Create flat by block 
block.SetAttribute("IsFlat")
```
#### Image
```
image = Image.Image(display,x_pos,y_pos,source)

# Change new size
image.Transform(100,100)
```
#### Human
```
player = Human.Human(Rectangle | Image)

# Note: To access Rectangle Use
# player.Rectangle

# Move Human
player.MoveTo(HUMAN_DIRECTION_RIGHT | HUMAN_DIRECTION_LEFT)

# Jump Human
player.JumpActive()

# Take Health
player.TakeHealth(damage)
```
#### id of Rectangle
In a rectangle, image they are have a id. And you can get it by
```
rect = Rectangle(display,10,10,100,50)
id_rect = rect.getId()
```
Note: Gui has its own id
