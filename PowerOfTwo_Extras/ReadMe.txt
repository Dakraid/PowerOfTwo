Introduction:
    PowerOfTwo is a simple utility checking for textures that do not conform to the power of two rule.
    GPUs can't use their automatic mip mapping and compression for non-power of two textures, which might cost a small amount of performance.
    
Usage:
    By default, PowerOfTwo.exe will try to scan all subdirectories within the directory it resides in. 
    It will only look for .dds files, nothing else. Also any interface, LOD or 1x1 textures will be ignored.
    
    You can either copy/extract all of the appliaction to the root directory of the subdirectories you want to check or you can use the bat.
    The bat file allows you to define a path to check using the -p parameter.
    
    Any textures that do not conform to the power of two rule are written into the results.txt.
    
    Example:
        To set the parameter you simply edit the PowerOfTwo_Custom.bat and it should look like this:
        PowerOfTwo -p "C:\YourPathHere"
        
        The "" aren't required as long as your path doesn't contain whitespaces.

Changelog:
    > 1.0.0: Initial Release