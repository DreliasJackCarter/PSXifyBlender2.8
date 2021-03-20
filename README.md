# PSXifyBlender2.8
Give a PS1 appearance for your Blender 2.8+ renders !

This script is greatly inspired by Komojo's work from the following thread :
https://blenderartists.org/t/playstation-1-jittery-texture-effect-not-for-a-game/1167818

# Presentation
### Jittery models
This Python script rounds all vertex coordinates as seen from camera and creates a whole duplicata of the scene with those new coordinates taken into account.
### Affine textures
![Affine texture preview](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Affine.jpg)

The texture distorsion is obtained by twisting polygons. The solution is to render the scene from perspective to orthogrpahic camera's point of view.
# Preview
![PSXify preview at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/RenderPreviews.gif)

# Limitations :
* The script was currently tested on Blender 2.91. I mentionned Blender 2.8 to talk about recent versions of Blender.
* Walls, Floor and any long models passing behind the camera need to be subdivided at least a little.
* Objects must be Modifier free. Mirror, Array and such interfere with number of vertex.
* Ensure to backup your Blender file to prevent any damage.
