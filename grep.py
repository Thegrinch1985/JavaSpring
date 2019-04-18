import re
filename = "build.gradle"
pattern = re.compile(r"dependencies", re.IGNORECASE)
with open(filename, "rt") as in_file:
 for line in in_file:
  if pattern.search(line) != None:
      for line in in_file:
          #print(line)
        
            
      
      
       print(line, end='')
