import os 
def main(): 
    i = 0
      
    for filename in os.listdir("target"): 
        dst ="prefix" + str(i) + ".jpg"
        src = 'target/'+filename 
        dst ='target/'+ dst 
          
        os.rename(src, dst) 
        i += 1
  
if __name__ == '__main__': 
    main()
    
