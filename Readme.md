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


# Update Log
## 0.0.1.3.1
- add Vision Hub (  cmd  ): init project
## 0.0.1.2 to 0.0.1.3
- add 'isTouched' method in Rectangle return True/False
- add 'button' class in Gui
# Future Update
- Vision Hub (  gui  )
    * GUI
    * script
- Vision Hub (  cmd  )
    * init project
- Engine
    * Method of Human
    * Single Script ( Run When Satisfied Condition, Run On A Thread )
    * Update_Function Method of Rectangle ( Argv is rectangle, run with 'display.Update()' )