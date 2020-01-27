def draw_market(height = 10):
    if(height == 0): 
        print("market height is invalid!")
        return
    print("market is here!")
    print("        _________________________")
    print("       /\                         \ ")
    print("      /  \      M A R K E T        \ ")
    print("     /    \                         \ ")
    print("    /______\_________________________\ ")

    
    for i in range(height-1):
        print("    |       |                  |     |")
    print("    |_______|__________________|_____|")
    return
