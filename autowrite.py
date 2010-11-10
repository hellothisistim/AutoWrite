# Create the Write Node
w= nuke.createNode('Write', inpanel=False)
# Rename it to AutoWrite
# (Also, deal with the number problem)
w.knob('name').setValue("Auto" + w.knob('name').value())

# Add the tab to hold the variables containing path fragments so we can have a less messy file path.
t = nuke.Tab_Knob("Path Fragments")
w.addKnob(t)
w.addKnob(nuke.EvalString_Knob('proj_root', 'Project Root', '[value root.name]'))




t.setVisible(False)