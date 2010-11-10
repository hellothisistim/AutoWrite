# Create the Write Node
w= nuke.createNode('Write', inpanel=False)
# Rename it to AutoWrite
# (Also, deal with the number problem)
count = 1
while nuke.exists('AutoWrite' + str(count)):
    count += 1
w.knob('name').setValue('AutoWrite' + str(count))

# Add the tab to hold the variables containing path fragments so we can have a less messy file path.
t = nuke.Tab_Knob("Path Fragments")
w.addKnob(t)
w.addKnob(nuke.EvalString_Knob('proj_root', 'Project Root', '[join [lrange [split [value root.name] / ] 0 4 ] / ]'))
w.addKnob(nuke.EvalString_Knob('seq', 'Sequence', ''))
w.addKnob(nuke.EvalString_Knob('shot', 'Shot Name', ''))
w.addKnob(nuke.EvalString_Knob('script', 'Script Name', '[file tail [value root.name] ]'))



t.setVisible(False)