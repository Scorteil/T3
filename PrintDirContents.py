def print_dir_contents(strPath):
    """
    Print strPath's contents and its childrens'
	
    """
    
    import os
    
    if not os.path.isdir(strPath):
        
        print(strPath + " is not a valid path.")
    
    else:
        
        for strFileName in os.listdir(strPath):
            
            strChildPath=os.path.join(strPath,strFileName)
    
            if os.path.isdir(strChildPath):
                
                print_dir_contents(strChildPath)
            
            else:
                
                print(strPath)


