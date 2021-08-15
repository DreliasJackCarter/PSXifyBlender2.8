# PSXifyBlender2.8
Give a PS1 appearance for your Blender 2.8+ renders !

This script is greatly inspired by Komojo's work from the following thread :
https://blenderartists.org/t/playstation-1-jittery-texture-effect-not-for-a-game/1167818

current version : V1.2

* V1.2 Manages vertex groups.
* V1.1 Handles lights according to Komojo's logic. see 'Lighting' part of Readme for more info.

## Presentation
![Combine Ordinal](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/CombineOrdinal.gif)
#### Jittery models
This Python script rounds all vertex coordinates as seen from camera and creates a whole duplicata of the scene with those new coordinates taken into account.
#### Affine textures
PS1 is known for its texture distorsion due to lack of precision in perspective, or as a famous French Youtuber said : "The walls that are not yet finished cooking" :

![Affine texture preview](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/Affine.jpg)

The texture distorsion is obtained by twisting polygons. The solution is to render the scene from perspective to orthographic camera's point of view :

![Polygon distorsion](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/PreviewOfOrthoCameraRender.gif)

## Preview
#### Helmet :
![Medieval helmet script preview](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/PreviewHelmet.gif)
#### Aircraft model :
![PSXify preview at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/RenderPreviews.gif)
#### Merciless fight :
![Mordhau fight at different resolutions](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/PreviewOnMordhauScene.gif)
#### Early test with a main cube, floor and walls :
![Test of cube in a room](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/EarlyTestCubeInRoom.gif)

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
* Hide all the collection but the PSXCollection :

![What you have to tick and untick](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/HideFromRenderAndViewport.jpg)

* ?????
* Profit !

## Lighting

In order to add light sources to your PSXified models, some modifications are necessary.

First, add vertex colors to each mesh you want light to apply :

![Add vertex colors](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/AddVertexColor.jpg)

Then multiply the output of your texture by the Attribute 'Col' :

![AttributeCol](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/MaterialModifications.jpg)

Vertex will now be affected by light source exposure. However, only the light object orientation count. Light strength is determined by 'sun' and 'shadow' variables in the script.
Here are previews of some different values combinations :

![Preview of light strength](https://github.com/DreliasJackCarter/PSXifyBlender2.8/blob/main/Previews/LightPreview.jpg)

## Limitations :

I noticed some issues that I'm trying to fix :
* The script was currently tested on Blender 2.91. I mentionned Blender 2.8 to talk about recent versions of Blender.
* Walls, Floor and any long models passing behind the camera need to be subdivided at least a little (For instance, the early test room walls and floor have been tiled).
* Objects must be Modifier free. Mirror, Array and such interfere with number of vertex.
* Ensure to backup your Blender file to prevent any damage.
* Eevee rendering is fast but randomly crashes. Cycles seems more stable but renders a bit slower.
* ~~Light sources are not handled yet.~~
* Background textures and skyboxes are not handled.
* ~~Soft armatures are not handled properly (see sword trail). It may be due to persistent vertex groups.~~
* This script is made for rendering. Script execution is inappropriate for real time 3D.

## Feedback
I would also be very happy to see if my script works well on other people's work. Contact me via Reddit or GitHub.
This is my first hosted project on GitHub, I'll try to use this platform properly for further versions.
