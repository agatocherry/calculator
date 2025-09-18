# Code-o-dachi 💻✨
*September 2025 Codédx Challenge: Vibe Coding Challenge*

Un Tamagotchi orienté programmation créé avec Python Tkinter - Votre compagnon de code virtuel !

## 🎮 Qu'est-ce que Code-o-dachi ?

Code-o-dachi est un Tamagotchi virtuel unique conçu spécialement pour les développeurs et les passionnés de programmation. Contrairement aux Tamagotchis traditionnels, votre animal de compagnie virtuel prospère grâce au code, au débogage et à l'apprentissage de nouveaux langages de programmation !

### ✨ Fonctionnalités

- **🐾 Compagnon de code virtuel** : Un adorable animal ASCII qui évolue avec vos activités de programmation
- **📊 Statistiques de développeur** : Énergie, Connaissance, Compétences de débogage, Créativité, Niveau de café, Bonheur
- **💻 Activités de codage** : Sessions de programmation, débogage, apprentissage de nouveaux langages
- **☕ Système de soins** : Donnez du café, laissez votre pet se reposer, maintenez son bonheur
- **🌟 Évolution** : Votre pet apprend de nouveaux langages de programmation et gagne de l'expérience
- **💾 Sauvegarde automatique** : Vos progrès sont automatiquement sauvegardés
- **🎨 Interface graphique intuitive** : Interface Tkinter simple et élégante

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.6 ou supérieur
- Tkinter (généralement inclus avec Python)

### Installation

1. **Clonez le repository** :
   ```bash
   git clone https://github.com/agatocherry/code-o-dachi.git
   cd code-o-dachi
   ```

2. **Installez tkinter** (si nécessaire) :
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tk
   
   # CentOS/RHEL/Fedora
   sudo yum install tkinter
   # ou
   sudo dnf install python3-tkinter
   
   # macOS (avec Homebrew)
   brew install python-tk
   
   # Windows
   # Tkinter est généralement inclus avec Python
   ```

3. **Lancez l'application** :
   ```bash
   python3 code_o_dachi.py
   # ou utilisez le launcher
   python3 launcher.py
   ```

## 🎯 Comment jouer

### Statistiques de votre Pet

- **⚡ Énergie** : Nécessaire pour coder et déboguer. Diminue avec les activités.
- **🧠 Connaissance** : Augmente avec les sessions de code et l'apprentissage. Nécessaire pour apprendre de nouveaux langages.
- **🐛 Compétences de débogage** : S'améliore en déboguant du code. Essentiel pour résoudre les problèmes complexes.
- **🎨 Créativité** : Booste l'innovation et les solutions élégantes.
- **☕ Niveau de café** : Carburant essentiel pour coder ! Nécessaire pour les sessions de programmation.
- **😊 Bonheur** : État général de bien-être de votre pet. Affecte toutes les autres activités.

### Actions disponibles

#### ☕ Donner du café
- Augmente l'énergie et le niveau de café
- Booste légèrement le bonheur
- Essential pour maintenir la productivité !

#### 💻 Session de codage
- Principale activité pour gagner de l'expérience
- Augmente la connaissance et le bonheur
- Consomme de l'énergie et du café
- Messages motivants aléatoires

#### 🐛 Déboguer du code
- Améliore les compétences de débogage
- Donne de l'expérience et du bonheur
- Nécessite plus d'énergie que le codage normal
- Débloque avec l'expérience

#### 📚 Apprendre un langage
- Ajoute de nouveaux langages de programmation à votre collection
- Augmente significativement la connaissance
- Nécessite un niveau de connaissance minimum
- Langages disponibles : JavaScript, Java, C++, C#, Go, Rust, TypeScript, Ruby, PHP, Swift, Kotlin

#### 😴 Se reposer
- Restaure l'énergie
- Améliore légèrement le bonheur
- Remet à zéro les états d'activité (coding, debugging, learning)

#### 💾 Sauvegarder
- Sauvegarde manuelle de votre progression
- La sauvegarde automatique se fait toutes les 30 secondes

### États de votre Pet

Votre Code-o-dachi change d'apparence selon son état :

- **😴 Fatigué** : Besoin de repos ou de café
- **☕ Besoin de café** : Prêt à coder mais manque de caféine
- **💻 En train de coder** : Dans sa zone de confort, créant du code
- **🐛 Débogage** : Concentré sur la résolution de problèmes
- **📚 Apprentissage** : Absorbant de nouvelles connaissances
- **😰 Stressé** : Bonheur faible, besoin d'attention
- **✨ Heureux** : État optimal, prêt pour toutes les activités

## 🛠️ Structure du projet

```
code-o-dachi/
├── code_o_dachi.py      # Application principale
├── launcher.py          # Script de lancement avec vérifications
├── requirements.txt     # Dépendances (uniquement stdlib)
├── README.md           # Cette documentation
└── pet_data.json       # Fichier de sauvegarde (créé automatiquement)
```

## 🎨 Caractéristiques techniques

- **Interface** : Python Tkinter avec thème moderne
- **Persistance** : Sauvegarde JSON automatique
- **Architecture** : Classes séparées pour la logique (CodeODachi) et l'interface (CodeODachiGUI)
- **Compatibilité** : Python 3.6+ sur Windows, macOS, Linux
- **Dépendances** : Aucune ! Utilise uniquement la bibliothèque standard Python

## 🐛 Résolution de problèmes

### Problèmes courants

1. **"ModuleNotFoundError: No module named 'tkinter'"**
   - Installez tkinter pour votre distribution Python
   - Voir les instructions d'installation ci-dessus

2. **L'application ne se lance pas**
   - Vérifiez votre version Python : `python3 --version`
   - Utilisez le launcher : `python3 launcher.py`

3. **La sauvegarde ne fonctionne pas**
   - Vérifiez les permissions d'écriture dans le dossier
   - Le fichier `pet_data.json` sera créé automatiquement

## 🤝 Contribution

Ce projet a été créé pour le Codédx Challenge de septembre 2025. Les contributions sont les bienvenues !

### Idées d'améliorations

- 🎵 Sons et effets sonores
- 🏆 Système d'achievements
- 📈 Graphiques de progression
- 🌟 Nouveaux langages et technologies
- 🎨 Thèmes et customisation
- 🔗 Intégration avec des IDEs
- 📊 Statistiques avancées

## 📝 Licence

Ce projet est open source. Créé avec ❤️ pour la communauté des développeurs.

---

**Amusez-vous bien avec votre Code-o-dachi ! 🎮💻✨**

*N'oubliez pas : un développeur heureux fait un pet heureux !*