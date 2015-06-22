import os

home ='/home/lmpizarro/Proyectos/blender-2.70a-linux-glibc211-x86_64/'
filename = os.path.join(os.path.abspath(home+'./scripts_ex'), "nodes-blur.py")

print (filename)

exec(compile(open(filename).read(), filename, 'exec'))