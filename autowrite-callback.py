# autowrite.py

"""Useful for keeping output names consistent with Nuke script names.

At [unspecified studio], the project structure puts Nuke scripts in a directory like this:
S:/Active_Projects/13-XXX-PROJECT_NAME/2D/NUKE_PROJECTS/SH010/

The 2D renders go in a directory like this one:
S:/Active_Projects/13-XXX-PROJECT_NAME/2D/RENDERS/SH010/SH010_comp_v001

This module sets up a callback that is triggered by saving a script that will update the output path for any Write node whose name starts with 

"AutoWrite" to match the naming and placement of the source script. The type of file rendered is controlled by the "file type" pulldown.
"""

import nuke
import os.path

## Globals
debug = True

def debug_msg(msg):
    print msg
    nuke.tprint(msg)

def mark_warning(node):
    """Change the node color to orange to signal that it was not updated by autowrite (probably due to a non-standard script path or name.)"""

    color = 0xff330000
    node.knob('tile_color').setValue(color)

def mark_notify(node):
    """Change the node color to green to signal that it was updated by autowrite."""

    color = 0x33ff0000
    node.knob('tile_color').setValue(color)

def mark_normal(node):
    """Return the node color to default."""

    node.knob('tile_color').setValue(0)


def update_path(node):
    """Rebuild the output path for the given Write node using the name/path from the current Nuke script."""

    # Sanity checking.
    if node.Class() != 'Write': 
        nuke.tprint('Not setting Autowrite for ' + node.name())
        mark_warning(node)
        return
    if not node.name().startswith('AutoWrite'):
        nuke.tprint('Not setting AutoWrite for ' + node.name())
        mark_warning(node)
        return

    # Build output file path.
    script = nuke.root().name()
    chunks = script.split('/')
    if len(chunks) != 7: 
        nuke.tprint("Nonstandard path. Not setting AutoWrite for " + node.name())
        mark_warning(node)
        return
    drive = chunks[0]
    activeproj = chunks[1]
    project = chunks[2]
    dept = chunks[3]
    sub = chunks[4]
    shot = chunks[5]
    scriptname = os.path.splitext(chunks[6])[0]
    outpath = '/'.join([drive, activeproj, project, dept, 'RENDERS', shot, scriptname])
    
    # Build output file name.
    # Get extension from "file type" knob.
    ext = node.knob('file_type').value()
    # Default to EXR if nothing is chosen.
    if ext.isspace():
        ext = 'exr'
    # 3-letter file extensions, please.
    if ext == 'jpeg':
        ext = 'jpg'
    elif ext == 'targa':
        ext = 'tga'
    elif ext == 'tiff':
        ext = 'tif'
    outfile = scriptname + '.%04d.' + ext
    fullpath = outpath + '/' + outfile
    print 'Setting output on ', node.name(), 'to', fullpath

    if fullpath != node.knob('file').value():
        node.knob('file').setValue(fullpath)
        mark_notify(node)
    else:
        mark_normal(node)
    

def update_all():
    """Update paths in all AutoWrites. 
    
    To be used in the onScriptSave callback.
    """

    print "autowrite.update_all starting."
    for n in nuke.allNodes('Write'):
        if n.name().startswith('AutoWrite'):
            print "Updating output path in ", n.name()
            update_path(n)

def update_one():
    """For use in the knobChanged callback. Update the path when the file type is changed."""

    debug_msg('autowrite.update_one: triggered.')
    if nuke.thisKnob().name() == 'file_type' and nuke.thisNode().name().startswith('AutoWrite'):
        node = nuke.thisNode()
        debug_msg('autowrite.update_one: calling update_path for ' + node.name())
        update_path(node)
    else:
        return


# Add callbacks
nuke.tprint('AutoWrite adding callbacks.')
nuke.addOnScriptSave(update_all)
nuke.addKnobChanged(update_one, nodeClass='Write')
