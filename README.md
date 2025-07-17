

<h1 align="center">🏡 ImmoTaxManager</h1>

<p align="center">
  <img src="https://img.shields.io/badge/langage-python-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/POO-Oriented-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/status-done-yellow?style=flat-square" />
</p>

<p align="center">
  <em>Projet Python orienté objet pour la gestion intelligente des <strong>impôts immobiliers</strong>.</em>
</p>

---

## 🌟 Aperçu du projet

> **ImmoTaxManager** est une application en Python conçue pour une agence immobilière fictive.  
> Elle permet de gérer les logements des propriétaires et de calculer automatiquement les impôts selon leur type.

---

## 🎯 Fonctionnalités

- 📌 Gestion des **logements** : `Villa` & `Appartement`
- 🧮 Calcul automatique des **impôts**
- 👤 Gestion des **propriétaires**
- 🏢 Système d’**agence immobilière** contenant plusieurs propriétaires
- ⚙️ **Tri dynamique** des propriétaires selon le nombre de logements
- ✅ Respect des **contraintes métiers**

---

## 🧠 Logique orientée objet

```mermaid
classDiagram
    class Logement {
        +int numero
        +float surface
        +modifSurface(v)
        +eq(other)
    }

    class Villa {
        +float jardin
        +impot()
    }

    class Appartement {
        +int etage
        +impot()
    }

    Logement <|-- Villa
    Logement <|-- Appartement

    class Proprietaire {
        +int idprop
        +ajoutLog(lg)
        +modifLog(lg, v)
        +calculimpot()
    }

    class Agence {
        +List props
        +ajoutProp(p)
        +ajoutLogProp(p, lg)
        +trierProp()
    }

    Proprietaire --> Logement
    Agence --> Proprietaire
````

---

## 💡 Calculs d'impôt

| Type               | Formule                                 |
| ------------------ | --------------------------------------- |
| 🏡 **Villa**       | `impôt = surface × 180 + jardin × 40`   |
| 🏢 **Appartement** | `impôt = surface × (100 / (étage + 1))` |

---

## 🧪 Exemple d'utilisation

```python
V1 = Villa(1001, 350, 10)
A1 = Appartement(1546, 110, 5)

P1 = Proprietaire(101, "Aya", "Ben Mabrouk")
P1.ajoutLog(V1)
P1.ajoutLog(A1)

AG = Agence()
AG.ajoutProp(P1)

print(AG)
```

---

## 📂 Arborescence

```bash
.
├── index.py             # Code principal
├── README.md           # Documentation du projet
└── test.txt     # un test de fonctionnement
```

---

## 🔧 Contraintes implémentées

* ✅ Surface ≤ 1000 m²
* ✅ Surface jardin ≤ 50% surface villa
* ✅ Étages entre 0 et 20
* ✅ Max 20 logements par propriétaire

---

## 🧑‍💻 Auteur

**Aya Ben Mabrouk**
💼 Ingénieur Logiciel Junior
📍 Douz, Tunisie
🌐 [GitHub](https://github.com/BenMabroukAya)

---

## 📈 Statistiques GitHub

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=BenMabroukAya&show_icons=true&theme=react" height="150" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=BenMabroukAya&layout=compact&theme=react" height="150" />
</p>

---

## 📜 Licence

Ce projet est open-source.
Utilisation commerciale interdite sans autorisation.

---

> 🧠 *"La POO au service d’une gestion fiscale efficace."*


