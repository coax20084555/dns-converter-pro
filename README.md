# DNS-Converter Pro

DNS Converter Pro est une application de bureau Python qui convertit les noms de domaine en adresses IP et les adresses IP en noms d'hôte à l'aide d'une interface Tkinter moderne.

## 📸 Captures d'écran

### Domaine → IP

![Domain to IP](Images/convertisseur.png)

### IP → Nom d'hôte

![IP to Hostname](Images/ip-hostname.png)

---

# 🚀 Installation

## Prérequis

- Python 3.10 ou supérieur
- pip

Vérifiez que Python est installé :

```bash
python --version
```

ou

```bash
python3 --version
```

---

# ▶️ Lancer l'application

1. Clonez le dépôt :

```bash
git clone https://github.com/coaxial20084555/dns-converter-pro.git
```

2. Accédez au dossier :

```bash
cd dns-converter-pro
```

3. Lancez le programme :

```bash
python main.py
```

ou

```bash
python3 main.py
```

---

# 🪟 Utilisation sous Windows

### Avec Python installé

Ouvrez **Invite de commandes (CMD)** ou **PowerShell**, puis :

```cmd
git clone https://github.com/coaxial20084555/dns-converter-pro.git
cd dns-converter-pro
python main.py
```

Si `python` ne fonctionne pas :

```cmd
py main.py
```

---

### Depuis l'exécutable (.exe)

Si une version compilée est disponible :

1. Téléchargez `DNS-Converter-Pro.exe`.
2. Double-cliquez sur le fichier.
3. L'application démarre sans installation de Python.

---

# 💻 Utilisation

## Domaine → Adresse IP

1. Saisissez un nom de domaine ou une URL.
2. Cliquez sur **Convertir**.
3. L'adresse IP s'affiche.
4. Cliquez sur **Copier** pour copier le résultat.

## Adresse IP → Nom d'hôte

1. Saisissez une adresse IP.
2. Cliquez sur **Convertir**.
3. Le nom d'hôte associé s'affiche.
4. Cliquez sur **Copier** pour copier le résultat.

---

# 📦 Compilation en exécutable

Pour générer un exécutable Windows :

```bash
pip install pyinstaller
pyinstaller main.spec
```

L'exécutable sera créé dans le dossier :

```
dist/
```

---

# 📄 Licence

Ce projet est distribué sous licence MIT.
