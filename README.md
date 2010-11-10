AutoWrite
Semi-automatic output paths in [The Foundry's Nuke](http://www.thefoundry.co.uk/products/nuke/). A tool by [Tim BOWMAN](http://netherlogic.com).

#The gist: 
Create output paths by parsing the Nuke script name and path.

#The theory:
Most of the information needed for the output of a Nuke script is contained in it's name. We can reduce manual name changing on behalf of the artists and simultaneously increase consistency by creating a Write node that creates (and updates) it's own output path by parsing the script's name.

#The details:
Most projects at most facilities will have a common set of path fragments. My list includes: project root, sequence name (or abbreviation), shot name. We will create a new tab  on the Write node to help us isolate each fragment so we can easily re-assemble them for the output path. This tab will contain knobs for each path fragment. 

Since each facility creates their own file structure, I will set it up for my structure and then leave it to you how to parse your own path for each fragment.

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