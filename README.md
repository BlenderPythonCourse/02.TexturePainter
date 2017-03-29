### Section 2 Introduction ###

+ Welcome to the project section.
+ What you'll learn.
+ Share your vision with fellow students.

### Project Setup & GitHub ###



### No Such Thing As Plain Text ###

+ There’s no such thing as plain text
+ Using Python’s **codecs** library 
+ Reading a CSV file in a cross-platform manner.

### Iterators and csv.reader() ###

+ The **with** keyword establishes a context
+ ...useful for managing file access & scope 
+ The **yield** keyword is subtle and beautiful 
+ The combination **dict(zip(header, row))**
+ Reading and printing our CSV header.

### Rendering Text To Images ###

+ Using the Pillow library
+ This is a fork of the Python Image Library (**PIL**) 
+ How to use **Image**, **ImageDraw** and **ImageFont**
+ Rendering text to an image file in Python.

### Rendering 1000s Of Images ###

+ Adjusting our image size
+ Making the filename variable 
+ Iterating to quickly create 1000s of image files.

### Using raise For Exceptions ###

+ Reading about exception handling in Python
+ How the **raise** keyword works
+ It’s a bit like return but if not handled in caller…
+ … then eventually the program will quit and error
+ Also using **bpy.context.selected_objects**

### Placing Text On Our Object ###

+ Learn how to place our text image onto a model.
+ We are going to use Blender Render.
+ We’ll have a prototype ready to repeat a few times!

### Duplicating Objects ###

+ How to select objects in Python
+ Using **bpy.ops.object.duplicate_move()** to duplicate objects, with a fixed offset.

### Calculating Object Offsets ###

+ How to use Docstrings to comment your code
+ How the **%** operator works in Python
+ Remember the **//** integer division operator 
+ Calculating offset from our prototype.

### Using enumerate In Loops ###

+ Our csv file already has “backer numbers”
+ However, we shouldn’t rely on this data 
+ How about if it doesn’t start at 0? 
+ How about if there are duplicates or gaps? 
+ Let’s use Python’s **enumerate** to take charge.

### Refactoring and Integrating ###

+ Changing our file naming
+ Refactoring our code structure.

### Blender Render Material Data ###

+ Each object can have multiple material slots
+ Each material slot may have a material 
+ Materials have texture slots 
+ Each texture slot can have a texture 
+ Textures image names and paths.

### Finishing Our Code ###

+ How to open an image in Blender Python
+ How to assign a new texture with Blender render 
+ Copying materials and textures.

### Setting Up Our Names ###

+ Define the spacing of the names
+ Render out all our names
+ Setup the camera
+ Key your animation ready for the final scene.

### Compositing The Final Credits ###

+ Using the compositor to finalise our scene
+ Make it have an interesting background.

### Setting The Material For Cycles ###

+ Configure 1 Material for Blender Render and Cycles.
+ Test render our final scene.
+ Then we’ll be ready to adjust our script to work.

### Cycles Material Data ###

+ The data structure for Cycles starts similar to Blender Render
+ However rather than looking at texture slots, we need to investigate the **node_tree**
+ From there we look at **nodes[name].image**

### Section 2 Wrap-Up ###

Please share what you have created with other students.

---
Find out more about our [Automate Blender with Python Course](https://www.udemy.com/blenderpython/?couponCode=GitHubDiscount).
