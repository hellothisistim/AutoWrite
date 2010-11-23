AutoWrite

Semi-automatic output paths in [The Foundry's Nuke](http://www.thefoundry.co.uk/products/nuke/). A tool by [Tim BOWMAN](http://netherlogic.com).

#The gist: 
Create output paths by parsing the Nuke script name and path.

#The theory:
Most of the information needed for the output of a Nuke script is contained in it's name. We can reduce manual name changing on behalf of the artists and simultaneously increase consistency by creating a Write node that creates (and updates) it's own output path by parsing the script's name.

#The details:
Most projects at a facility will use a standardized file hierarchy, which means that a Nuke script's name and path on the filesystem will often contain all the information needed to define the output destination for it's render. As an example, here is a path from one of my comp scripts:

/Volumes/PICO/show/testproj/abc/abc123/nuke/abc123_comp_v01.nk

From this path, we can see that I have a project called "testproj" that has a sequence with an abbreviation "abc" and that there is a shot called "abc123" in that sequence. I am working on composite version #1 on that shot.

What I do to create an AutoWrite is add a tab to the Write node where I break down these path elements in four knobs: project root, sequence name (or abbreviation), shot name and script name. These knobs are then re-assembled to create the AutoWrite's output path.

Since each facility creates their own file structure, I have set it up for my own structure and I leave it to you to parse your own paths.

# LICENSE
Copyright (c) 2010 Tim BOWMAN

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.