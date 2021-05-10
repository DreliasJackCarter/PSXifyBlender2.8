# 05/2021
# PSXify script by Lucas Fierfort
# V1.1
# IMPORTANT : Please make sure to make a backup of your file before launching this script, just in case.

import bpy
import math
import mathutils
import bpy_extras.object_utils
from time import sleep

#-----------------------------------MANDATORY SETTINGS----------------------------------------------

cameraName = 'Camera'               # Camera from which meshes will be PSXified in render

collectionToPSXify = 'Collection'   # Name of the Collection you want the script to apply.

PSXRenderWidth = 160                # PSX grid width resolution
PSXRenderHeight = 120               # PSX grid height resolution


delayBetweenFrames = 0.1            # Delay in seconds between each frame rendering, seems to prevent some glitches
delayBetweenObjects = 0.1           # Delay between objects calculation in the same frame

depth = 0.2                         # Relative distance from PSX camera
PSXcameraScale = 1.33               # PSX camera FOV, set it manually to fit the orginal camera

lightName = 'Sun'                   # Name of the light source you want to use
#--------------------------------------LIGHT SETTINGS-----------------------------------------------
useLights = True                    # True if you want to simulate lights

sun = 1.0                           # Light source strength. Script takes only light source orientation.
shadow = 0.85                       # Quantity of light on the opposite

g_lightColor = mathutils.Vector([sun, sun, sun])                # Sun color (white)
g_ambientColor = mathutils.Vector([shadow, shadow, shadow])     # Ambient color (lightness of shadows)
#---------------------------------------------------------------------------------------------------


scene = bpy.context.scene
camera = scene.objects[cameraName]
light = scene.objects[lightName]

# Get concerned collection and duplicate every objects inside into a dedicated new collection
def CreateWholeFakeScene(collectionSourceName, collectionDestName, scene):
    print("entering CreateWholeFakeScene")
    
    try :
        bpy.context.active_object.select_set(False) # Deselect everything
        print(" Deselecting active objects.") 
    except :
        print(" Nothing was selected.")
    
    PSXCreateCollection(collectionDestName, scene)
    
    originalCollection = bpy.data.collections[collectionSourceName]
    PSXcollection = bpy.data.collections[PSXcollectionName]
    
    objectsToPSXify = originalCollection.all_objects
    
    print(" objects found in collection \"", collectionSourceName, "\" :")
    for objectToPSXify in objectsToPSXify :
        print("  ",objectToPSXify.name)
    
    for objectToPSXify in objectsToPSXify:
        print(" Checking if ", objectToPSXify.name, " could be PSXified...")
        if objectToPSXify.type == 'MESH':
            print(" ", objectToPSXify.name, "is a mesh. Copy into PSXCollection !")
            PSXifiedObject = objectToPSXify.copy()
            PSXifiedObject.data = objectToPSXify.data.copy()
            PSXifiedObject.name = objectToPSXify.name + '.PSXified'
            PSXifiedObject.animation_data_clear()
            PSXifiedObject.rotation_euler = (0.0, 0.0, 0.0)
            PSXifiedObject.location = (0.0, 0.0, 0.0)
            PSXifiedObject.scale = (1.0, 1.0, 1.0)
            PSXifiedObject.parent = None
            PSXifiedObject.constraints.clear()
            PSXcollection.objects.link(PSXifiedObject)
            
            print("")
        else:
            print(" ", objectToPSXify.name, "is not a mesh. Ignoring it.")
            print("")
    
    # Create PSX camera
    PSXcamera_data = bpy.data.cameras.new(name='PSXCamera')
    PSXcamera_object = bpy.data.objects.new('PSXCamera', PSXcamera_data)
    PSXcamera_object.data.type = 'ORTHO'
    PSXcamera_object.data.ortho_scale = PSXcameraScale
    PSXcollection.objects.link(PSXcamera_object)
    
    # Set active camera
    scene.camera = PSXcamera_object
    
    # Hide original collection
    originalCollection.hide_render = True
    
    print("exiting CreateWholeFakeScene")






def PSXCreateCollection(collectionName, scene):
    print(" Checking if PSXCollection exists...")
    
    if collectionName in bpy.data.collections:
        print("  PSX collection already exists.")
        PSXcollection = bpy.data.collections[collectionName]
        obj = [o for o in PSXcollection.objects if o.users == 1]
        while obj:
            bpy.data.objects.remove(obj.pop())   # removing everything from PSXCollection
    else :
        print("  PSX collection does not exist ! creating it.")
        bpy.ops.collection.create(name = collectionName)
        bpy.context.scene.collection.children.link(bpy.data.collections[collectionName]) # just creating PSXCollection
        
    
    


def PSXifyCollection(camera, collection, scene):
    for object in collection.all_objects :
        if object.type == 'MESH':
            targetObject = scene.objects[object.name+'.PSXified']
            
            # Object data  
            mesh = object.data
            targetMesh = targetObject.data
            matrix = object.matrix_world
            rotationQuat = object.rotation_euler.to_quaternion()
            
            colors = targetMesh.vertex_colors.get('Col')
            lightDir = light.rotation_euler.to_quaternion() @ mathutils.Vector([0,0,1])
            
            print("snapping",targetObject.name, "from",object.name, "coordinates...")
            for vert,targetVert in zip(mesh.vertices,targetMesh.vertices):
                
                absPos = matrix @ vert.co

                snappedPos = PSXifyCoords(camera,absPos,scene)
                targetVert.co = snappedPos
                print('.', end='')
            print(targetObject.name, "snapped.")
            
            if useLights == True :
                try :
                    colorOffset = 0
                    for poly in mesh.polygons:
                        for idx in poly.vertices:
                            
                            normal = rotationQuat @ poly.normal
                            totalLightColor = mathutils.Vector([1,1,1])
                            brightness = max(lightDir.dot(normal), 0)
                            totalLightColor = g_ambientColor + (g_lightColor * brightness)
                    
                            colors.data[colorOffset].color = [totalLightColor[0], totalLightColor[1], totalLightColor[2], 1]
                            colorOffset += 1
                    print("Fake lighting applied.")
                except :
                    print("Fake lighting not applied, possibly because of no vertex colors declared on object")
            
            print("")
            
            sleep(delayBetweenObjects)
    
    
    
    
# Inspired from world_to_camera_view() function and Komojo script.
# Steps :
# - Get coordinates of given vertice as seen from camera
# - Calculates its X,Y as % position in camera,
# - Rounding the coords to snap it on a low res grid
# - Scaling and arranging the final output
def PSXifyCoords(obj, coord, scene):
    from mathutils import Vector
    
    # Get vertice coord from camera POV
    co_local = obj.matrix_world.normalized().inverted() @ coord
    
    # Z remains the same (distance of vertice from camera center)
    z = co_local.z
    
    camera = obj.data
    frame = [v for v in camera.view_frame(scene=scene)[:3]]
    
    # Calculate to frame corners location
    if camera.type != 'ORTHO':
     if z == 0.0:
         return Vector((0.5, 0.5, 0.0))
     else:
         frame = [-(v / (v.z / z)) for v in frame]
    
    # Get the four camera corner coords
    min_x, max_x = frame[2].x, frame[1].x
    min_y, max_y = frame[1].y, frame[0].y
    
    #Calculate X,Y of vertice as percentage position on screen
    x = (co_local.x - min_x) / (max_x - min_x) - 0.5 # -0.5 to center it
    y = (co_local.y - min_y) / (max_y - min_y) - 0.5 # -0.5 to center it
    
    # Snapping vertex to desired PSX resolution by rounding coords
    x = -(int)(x * PSXRenderWidth)/PSXRenderWidth
    y = -(int)(y * PSXRenderHeight)/PSXRenderHeight
    
    # Stretch X coord to adapt it to the camera frame
    x *= (PSXRenderWidth/PSXRenderHeight)
    
    # Fixes the "behind the camera" glitch :
    # When object get behind camera, the PSX mesh teleports at opposite side of axis, causing
    # visual glitch.
    # Solution : when they get behind the camera (= positive side), they stay at the same axis side
    if z > 0.0:
        x = -x
        y = -y
    
    # Depth scaling from camera
    z *= depth

    return Vector((x, y, z))





# Called everytime the frame changes
def updateHandler(dummy):
    sleep(delayBetweenFrames)
    PSXifyCollection(camera, PSXcollection, scene)


print("-----------------LAUNCHING SCRIPT-----------------")

# Set a callback to update the transform when the frame changes
bpy.app.handlers.frame_change_post.clear()  # Warning: This might also delete other callbacks
bpy.app.handlers.frame_change_post.append(updateHandler)

# Update now
PSXcollectionName = 'PSXCollection'
CreateWholeFakeScene(collectionToPSXify, PSXcollectionName, scene)
if PSXcollectionName in bpy.data.collections :
    PSXcollection = bpy.data.collections[collectionToPSXify]
    print("entering PSXify")
    PSXifyCollection(camera, PSXcollection, scene)
