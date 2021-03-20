# PSXifyBlender2.8
Give a PS1 appearance for your Blender 2.8+ renders !

This script is greatly inspired by Komojo's work from the following thread :
https://blenderartists.org/t/playstation-1-jittery-texture-effect-not-for-a-game/1167818

## Preview
#### Aircraft model :
![PSXify preview at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/RenderPreviews.gif)
#### Merciless fight :
![Mordhau fight at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/PreviewOnMordhauScene.gif)
#### Early test with a main cube, floor and walls :
![Test of cube in a room](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/EarlyTestCubeInRoom.gif)

## Presentation
#### Jittery models
This Python script rounds all vertex coordinates as seen from camera and creates a whole duplicata of the scene with those new coordinates taken into account.
#### Affine textures
PS1 is known for its texture distorsion due to lack of precision in perspective, or as a famous French Youtuber said : "The walls that are not yet finished cooking" :

![Affine texture preview](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Affine.jpg)

The texture distorsion is obtained by twisting polygons. The solution is to render the scene from perspective to orthographic camera's point of view :

![Polygon distorsion](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/PreviewOfOrthoCameraRender.gif)

# Limitations :
* The script was currently tested on Blender 2.91. I mentionned Blender 2.8 to talk about recent versions of Blender.
* Walls, Floor and any long models passing behind the camera need to be subdivided at least a little (For instance, the early test room walls and floor have been tiled).
* Objects must be Modifier free. Mirror, Array and such interfere with number of vertex.
* Ensure to backup your Blender file to prevent any damage.
* Eevee rendering is fast but randomly crashes. Cycles seems more stable but renders a bit slower.
* Light sources are not handled yet.
