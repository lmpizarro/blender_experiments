import bpy
import math

# switch on nodes
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree
links = tree.links

# clear default nodes
for n in tree.nodes:
    tree.nodes.remove(n)

home = '/home/lmpizarro'
path1 = home + '/Videos/MP4/quebranta/plano02/0435.png'
path2 = home + '/Videos/MP4/quebranta/plano02/0450.png'
paths = [path1, path2]
imgs=[]

def append_image(path):
    try:
        imgs.append(bpy.data.images.load(path))
    except:
        raise NameError("Cannot load image %s", path)

for p in paths:
    append_image (p)


image  = tree.nodes.new("CompositorNodeImage")

image.location = 0,0
image.hide=True


blur = tree.nodes.new("CompositorNodeBlur")
blur.filter_type = 'FLAT'
blur.use_variable_size = True
blur.use_gamma_correction = True

blur.size_x = 10
blur.size_y = 10
blur.location = 100,0
blur.hide=True

links.new(image.outputs[0], blur.inputs[0])

composite = tree.nodes.new("CompositorNodeComposite" )
composite.location = 200,100
composite.hide = True

links.new(blur.outputs[0], composite.inputs[0])

viewer = tree.nodes.new("CompositorNodeViewer" )
viewer.location = 200,0
viewer.hide = True
links.new(blur.outputs[0], viewer.inputs[0])

f_output = tree.nodes.new("CompositorNodeOutputFile")
f_output.location = 200,-100 
f_output.hide = True
f_output.base_path = "//maFolder/"
links.new(blur.outputs[0], f_output.inputs[0])

bpy.data.scenes["Scene"].render.use_overwrite = False

image.image = imgs[0]

bpy.data.scenes["Scene"].render.resolution_x = image.image.size[0]
bpy.data.scenes["Scene"].render.resolution_y = image.image.size[1]

bpy.data.scenes["Scene"].render.resolution_percentage = 100
bpy.data.scenes["Scene"].frame_start = 1
bpy.data.scenes["Scene"].frame_end = 1
bpy.data.scenes["Scene"].frame_step = 1

bpy.data.scenes["Scene"].render.filepath = f_output.base_path + 'vr_shot_%d.png' % 1
# Render still image, automatically write to output path
bpy.ops.render.render(write_still=True)

image.image = imgs[1]

bpy.data.scenes["Scene"].render.resolution_x = image.image.size[0]
bpy.data.scenes["Scene"].render.resolution_y = image.image.size[1]

bpy.data.scenes['Scene'].render.filepath = f_output.base_path + 'vr_shot_%d.png' % 2
bpy.ops.render.render(write_still=True)


