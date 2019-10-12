## 🔮 Directory structure
A simple bash script that makes a good directory structure for C projects.

### 🏁 Why is it useful ?
If you have many files, it may also be a good idea to further subdivide your project directory. For instance, one subdirectory for the sources file of your application, one for the headers, etc.
1. src/ 
	
    ➡️ source for the application
2. include/
  
  	➡️ interface for the library *.h
3. doc/
  
  	➡️  project documentation
4. bin/
  
  	➡️ 	final executable file
5. build/
  
  	➡️ where the generated .o files will be
6. git
  
  	➡️ initialize empty Git repository
7. .gitignore 
  
  	➡️ to determine which files and directories to ignore before you make commit like files in the bin and build directories
8. Makefile 
  
  	➡️ compiling the source code files can be tiring. Makefiles are the solution to simplify this task.

