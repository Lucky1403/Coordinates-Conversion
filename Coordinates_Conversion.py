import math

def start():
    print("Select the Coordinates from which you want to convert.")
    print("1) Cartesian to Polar \n2) Cartesian to Spherical \n3) Cartesian to Cylindrical\n4) Polar to Cartesian\n5) Polar to Spherical\n6) Polar to Cylindrical\n7) Spherical to Cartesian\n8) Spherical to Polar\n9) Spherical to Cylindrical\n10) Cylindrical to Cartesian\n11) Cylindrical to Polar\n12) Cylindrical to Spherical")

def Cartesian_to_Polar():
    #Cartesian to Polar Coordinates
    print("Enter the value of x in Cartesian Coordinates: ")
    x = float(input())

    print("Enter the value of y in Cartesian Coordinates: ")
    y = float(input())

    r = math.sqrt(x**2+y**2)
    theta = math.atan2(y, x) * (180/(math.pi))

    print("Polar coordinates are ",r,",",theta)



def Cartesian_to_Spherical():
    #Cartesian to Spherical Coordinates
    print("Enter the value of x in Cartesian Coordinates: ")
    x = float(input())

    print("Enter the value of y in Cartesian Coordinates: ")
    y = float(input())

    print("Enter the value of z in Cartesian Coordinates: ")
    z = float(input())

    r = math.sqrt(x**2+y**2)
    theta = math.atan2(y, x) * (180/(math.pi))
    z = z

    print("Cylinrical  coordinates are ",r,",",theta,",",z)
    
    
      
def Cartesian_to_Cylindrical():
    #Cartesian to Cylindrical Coordinates
    print("Enter the value of x in Cartesian Coordinates: ")
    x = float(input())

    print("Enter the value of y in Cartesian Coordinates: ")
    y = float(input())

    print("Enter the value of z in Cartesian Coordinates: ")
    z = float(input())

    p = math.sqrt(x**2+y**2+z**2)
    theta = math.atan2(y, x) * (180/(math.pi))
    phi = math.atan2(math.sqrt(x**2+y**2),z) * (180/(math.pi))

    print("Cylindrical  coordinates are ",p,",",theta,",",phi) 
    
def Polar_to_Cartesian():
    print("Enter the value of r: ")
    r = float(input())

    print("Enter the value of theta: ")
    theta = float(input())
    theta = math.radians(theta)
    
    x = r * math.cos(theta)

    y = r * math.sin(theta)

    print("Cartesian Coordinates are ",x," and ",y)
 

def Polar_to_Spherical():
    print("Enter the value of r: ")
    r = float(input())
    
    print("Enter the value of theta: ")
    theta = float(input())
    
    #Spherical Coordinates will be 
    p = r
    theta = theta
    phi = (math.pi)/2
    
    print("Spherical Coordinates are ",p,",",theta," and ",phi)
    

def Polar_to_Cylindrical():
    print("Enter the value of r: ")
    r = float(input())
    
    print("Enter the value of theta: ")
    theta = float(input())
    
    #Cylindrical Coordinates will be
    r = r
    
    theta = theta
    
    z = 0  #Z will be zero if the point lies on the x-y planes
    
    print("Here z is equal to zero because it is considered that tha point lies in the x-y plane.")
    print("Cylindrical coordinates are ",r," , ",theta," and ",z)
    
    
def Spherical_to_Cartesian():
    print("Enter the value of p: ")
    p = float(input())
    
    print("Enter the value of theta: ")
    theta = float(input())
    
    print("Enter the value of phi: ")
    phi = float(input())
    
    #Cartesian Coordinates will be 
    x = p * math.sin(phi) * math.cos(theta)
    
    y = p * math.sin(phi) * math.sin(theta)
    
    z = p * math.cos(phi)
    
    print("Cartesian Coordinates will be ",x," , ",y," and ",z)
    
    
def Spherical_to_Polar():
    print("Enter the value of p: ")
    p = float(input())
    
    print("Enter the value of theta: ")
    theta = float(input())
    
    print("Enter the value of phi: ")
    phi = float(input())
    
    #Polar coordinates will be
    r = p * math.sin(phi)
    
    theta = theta
    
    print("Polar Coordinates are ",r," and ",theta)
    
    
def Spherical_to_Cylindrical():
    print("Enter the value of p: ")
    p = float(input())
    
    print("Enter the value of theta: ")
    theta = float(input())
    
    print("Enter the value of phi: ")
    phi = float(input())
    
    #Cylindrical Coordinates will be
    r = p * math.sin(phi)
    
    theta = theta
    
    z = p * math.cos(phi)
    
    print("Cylindrical Coordinates will be ",r," , ",theta," and ",z)
    
    
def Cylindrical_to_Cartesian():
    print("Enter the values of r : ")
    r = float(input())
    
    print("Enter the value of theta : ")
    theta = float(input())
    
    print("Enter the value of z: ")
    z = float(input())
    
    
    #Cartesian Coordinates will be
    x = r * math.cos(theta)
    
    y = r * math.sin(theta)
    
    z = z
    
    print("Cartesian Coordinates will be ",x," , ",y," and ",z)
    

def Cylindrical_to_Polar():
    print("Enter the values of r : ")
    r = float(input())
    
    print("Enter the value of theta : ")
    theta = float(input())
    
    print("Enter the value of z: ")
    z = float(input())
    
    #Polar Coordinates will be 
    r = r
    
    theta = theta
    
    print("Polar Coordinates will be ",r," and ",theta)
    
    
def Cylindrical_to_Spherical():
    print("Enter the values of r : ")
    r = float(input())
    
    print("Enter the value of theta : ")
    theta = float(input())
    
    print("Enter the value of z: ")
    z = float(input())
    
    #Spherical Coordinates will be
    p = math.sqrt(r**2 + z**2)
    
    theta = theta
    
    phi = math.atan2(r,z)

start()
print("\nPlease select the type of conversion you'd like to perform by entering a number\n")
user_input = input()

match user_input:
    case "1":
        Cartesian_to_Polar();
        print("\n")
        start();
    case "2":
        Cartesian_to_Spherical();
        print("\n")
        start();
    case "3":
        Cartesian_to_Cylindrical();
        print("\n")
        start();
    case "4":
        Polar_to_Cartesian();
        print("\n")
        start();
    case "5":
        Polar_to_Spherical();
        print("\n")
        start();
    case "6":
        Polar_to_Cylindrical();
        print("\n")
        start();
    case "7":
        Spherical_to_Cartesian();
        print("\n")
        start();
    case "8":
        Spherical_to_Polar();
        print("\n")
        start();
    case "9":
        Spherical_to_Cylindrical();
        print("\n")
        start();
    case "10":
        Cylindrical_to_Cartesian();
        print("\n")
        start();
    case "11":
        Cylindrical_to_Polar();
        print("\n")
        start();
    case "12":
        Cylindrical_to_Spherical();
        print("\n")
        start();
    case default :
        print("Please select a valid number.");
        print("\n")
        start();