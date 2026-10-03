from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

password = "monmotdepasse123"
hashed = pwd_context.hash(password)

print("Mot de passe original:", password)
print("Mot de passe hashé:", hashed)

print("Vérification correcte:", pwd_context.verify(password, hashed))
print("Vérification incorrecte:", pwd_context.verify("mauvais_mdp", hashed))