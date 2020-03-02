"""
Just nu funkar denna om man lägger in egen textrad på vad som skall krypteras
/dekrypteras, se rad 30 och 94 i kryp och dekryp. 
har lagt en textkod mellan rad 13 till 20 i kryp 
resp rad 87 till 94 i dekryp som skall lösa detta
men de funkar ej på bärbara pga virtuell miljö fel
ska pröva på stationära ikväll
2/3-2020


"""
def kryp (file):
    
    
    lista = [] # lagrar varje rad i filen till listan
    """
    with open(file, "r") as g:
        line = g.readlines()

        for i in line:
            i.lower
            # dessa rader lagrar varje rad i filen till en lista, gör även om varje rad till små bokstäver
            lista.append(i)
    print(lista)
    """

    
    key = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g",
    "g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o",
    "o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w",
    "w":"x","x":"y","y":"z","z":"a",
    0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
    #en dictionary som krypterar alla bokstäver a-z och alla nummer 0-9
    
    lista = ["abc defg hijk","abc"] # lista där alla bokstäver sparas i innan kryptering
    
    lista2 = []
    
    #print(key)
    for i in lista:
        # tar fram varje ord ur listan
        for letter in i:
        # sparar alla bokstäverna i ordet till en ny lista
            if letter == " ":

                pass

            else:
                lista2.append(letter)
                
    print(lista2)
    
    krypted = [] # lista där alla krypterade bokstäver sparas i
    for l in lista2:
        krypted.append(key[l])
        # matchar bokstaven med den krypterade bokstaven och 
        # lagrar det till krypted
    #print(krypted)
    
    space_counter = 0 # håller koll på när ett mellanslag skall läggas till
    
    cryp_final = []
    for i in lista:
        cryp_final.append(" ")
        for g in i:
        #lagrar den dekrypterade bokstaven och matcher ihop med mellanslag från input
            if g.isspace() == False:
                #om den inte hittar ett mellanslag
                cryp_final.append(krypted[space_counter])
                #då lägger den till rätt bokstav på rätt plats från krypten
                space_counter +=1
            else:
                #här hittar den ett mellanslag på rätt plats ---> lägger till et mellanslag till ny
                cryp_final.append(" ")
                
        
    for letter in cryp_final:
        print(letter, end="")
              

def dekryp (file):
    
    key = {"a":"z","b":"a","c":"b","d":"c","e":"d","f":"e",
    "g":"f","h":"g","i":"h","j":"i","k":"j","l":"k","m":"l","n":"m",
    "o":"n","p":"o","q":"p","r":"q","s":"r","t":"s","u":"t","v":"u",
    "w":"v","x":"w","y":"x","z":"a",
    0:9,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,1:0}

    """
    with open(file, "r") as g:
        line = g.readlines()

        for i in line:
            i.lower
            # dessa rader lagrar varje rad i filen till en lista, gör även om varje rad till små bokstäver
            lista.append(i)
    print(lista)
    """
    lista = ["bcd efgh ijkl bcd"] # lista där alla bokstäver sparas i innan dekryptering
    
    lista2 = []
    
    #print(key)
    for i in lista:
        # tar fram varje ord ur listan
        for letter in i:
        # sparar alla bokstäverna i ordet till en ny lista
            if letter == " ":

                pass

            else:
                lista2.append(letter)
    
    
    krypted = [] # lista där alla krypterade bokstäver sparas i
    for l in lista2:
        krypted.append(key[l])
        # matchar bokstaven med den krypterade bokstaven och 
        # lagrar det till krypted
    #print(krypted)
    
    space_counter = 0 # håller koll på när ett mellanslag skall läggas till
    
    cryp_final = []
    for i in lista:
        cryp_final.append(" ")
        for g in i:
        #lagrar den dekrypterade bokstaven och matcher ihop med mellanslag från input
            if g.isspace() == False:
                #om den inte hittar ett mellanslag
                cryp_final.append(krypted[space_counter])
                #då lägger den till rätt bokstav på rätt plats från krypten
                space_counter +=1
            else:
                #här hittar den ett mellanslag på rätt plats ---> lägger till et mellanslag till ny
                cryp_final.append(" ")
                
        
    for letter in cryp_final:
        print(letter, end="")

dekryp ("bla.txt")