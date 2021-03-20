# PSXifyBlender2.8
Give a PS1 appearance for your Blender 2.8+ renders !

This script is greatly inspired by Komojo's work from the following thread :
https://blenderartists.org/t/playstation-1-jittery-texture-effect-not-for-a-game/1167818

## Presentation
#### Jittery models
This Python script rounds all vertex coordinates as seen from camera and creates a whole duplicata of the scene with those new coordinates taken into account.
#### Affine textures
PS1 is known for its texture distorsion due to lack of precision in perspective, or as a famous French Youtuber said : "The walls that are not yet finished cooking" :

![Affine texture preview](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Affine.jpg)

The texture distorsion is obtained by twisting polygons. The solution is to render the scene from perspective to orthographic camera's point of view :

![Polygon distorsion](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/PreviewOfOrthoCameraRender.gif)

## Preview
#### Aircraft model :
![PSXify preview at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/RenderPreviews.gif)
#### Merciless fight :
![Mordhau fight at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/PreviewOnMordhauScene.gif)
#### Early test with a main cube, floor and walls :
![Test of cube in a room](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/EarlyTestCubeInRoom.gif)

## Tutorial
* Copy the content of PSXify.py script, not need to download the repo.
* Backup your Blender file just in case.
* In the 'Script' tab, create a new script and paste the content.
* Some settings are necessary :
1. Write the camera name,
2. The collection containing all the objects you want to PSXify,
3. The resolution of the grid you want vertex to snap to,
4. The delays between each objects and frame computing (to prevent glitches),
5. The depth relative to PSX camera,
6. The PSX camera FOV (you have to set it manually for now).
* Launch the script.
* Hide all the collection but the PSXCollection.
* ?????
* Profit !

# Limitations :
* The script was currently tested on Blender 2.91. I mentionned Blender 2.8 to talk about recent versions of Blender.
* Walls, Floor and any long models passing behind the camera need to be subdivided at least a little (For instance, the early test room walls and floor have been tiled).
* Objects must be Modifier free. Mirror, Array and such interfere with number of vertex.
* Ensure to backup your Blender file to prevent any damage.
* Eevee rendering is fast but randomly crashes. Cycles seems more stable but renders a bit slower.
* Light sources are not handled yet.
* Background textures are not handled.
* Soft armatures are not handled properly (see sword trail). It may be due to persistent vertex groups.
