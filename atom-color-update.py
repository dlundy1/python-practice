import os

def main():
    #Defines main Method
    ToDirectory()

def ToDirectory():
    #Navigates to appropriate Directory
    print("Method Test 'navigateToDirectory'")
    os.system("""
    cd /; cd ~/.atom; ls; gedit styles.less
    """)

def updateCommentColor():
    #Updates Atom's Comment Color
    print("updateCommentColor")

if __name__ == '__main__':
     main()
