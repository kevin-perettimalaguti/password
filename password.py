import hashlib
import json

# L'utilisateur choissie le mot de passe 
def definir_mdp():
    return input("Veuillez entrer votre mot de passe : ")


# On vérifie si les exigences demandé pour le mot de passe
def verification_password(value):
    special_caracteres = "!@#$^&*"
    
    if len(value) < 8:
        return False
    
    has_upper = any(char.isupper() for char in value)
    has_lower = any(char.islower() for char in value)
    has_digit = any(char.isdigit() for char in value)
    has_special = any(char in special_caracteres for char in value)
    
    return has_upper and has_lower and has_digit and has_special

# Hachage du mot de passe 
def crypter_password(password):    
    mdp_hache = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return mdp_hache


# Liste pour stocker les mots de passe
passwords = []

# Boucle qui se répète 3 fois maximum
for _ in range(5):  # Répétez les étapes 2 à 4 jusqu'à 3 tentatives
    password = definir_mdp()
        
    # Si le mot de passe est validé, ca affiche un message et ca coupe la boucle
    if verification_password(password):
        password_crypte = crypter_password(password)
        print(f"Le mot de passe est valide. Bienvenue, votre mot de passe haché est : {crypter_password(password)}")
        passwords.append(password_crypte)
        break
    
    # Sinon l'utilisateur doit réssaissir un nouveau mot de passe 
    else:
        print("Le mot de passe est invalide. Il doit avoir au minimum : une majuscule, une minuscule, un chiffre et un caractère spécial.")
else:
    print("Vous n'avez pas saisi un mot de passe valide après 3 tentatives. Programme terminé.")


# Pour aller plus loin...
# Les mots de passe doivent être hachés avant d’être enregistrés dans un fichier.
# Le programme doit permettre à l’utilisateur d’ajouter de nouveaux mots de passe ou d’afficher ces derniers.
# Pour ce bonus, il est nécessaire d’utiliser la bibliothèque “Json” de python.


# Fonction pour sauvegarder les mots de passe dans un fichier JSON
def save_file():
    global passwords
    
    with open('stockage_mdp.json', 'w') as file:
        json.dump(passwords, file)
    print("Mots de passe enregistrés dans le fichier.")
    
# Appeler la fonction save_file pour enregistrer le mot de passe
save_file()