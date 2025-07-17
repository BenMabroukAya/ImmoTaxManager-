class Logement:
    def __init__(self, n, s):
        self.numero = n
        self.surface = min(s, 1000) # Limiting surface to 1000m2

    def __str__(self):
        return f"NumLog: {self.numero} ; Surface: {self.surface} m2"

    def modifSurface(self, v):
        if 0 <= v <= 1000:
            self.surface = v

    def eq(self, other):
        return self.numero == other.numero


class Villa(Logement):
    def __init__(self, n, s, jardin):
        super().__init__(n, s)
        self.jardin = min(jardin, s / 2) # Limiting jardin to half of the surface

    def impot(self):
        return self.surface * 180 + self.jardin * 40

    def __str__(self):
        return f"NumLog: {self.numero} ; Surface: {self.surface} m2 ; Surface du jardin: {self.jardin} m2"


class Appartement(Logement):
    def __init__(self, n, s, etage):
        super().__init__(n, s)
        self.etage = max(0, min(etage, 20)) # Limiting etage between 0 and 20

    def impot(self):
        return self.surface * (100 / (self.etage + 1))

    def __str__(self):
        return f"NumLog: {self.numero} ; Surface: {self.surface} m2 ; NumEtage: {self.etage}"

class Proprietaire:
    def __init__(self, _id, n, p):
        self.idprop = _id
        self.nom = n
        self.prenom = p
        self.logements = {}

    def __str__(self):
        prop_str = f"Proprietaire : {self.idprop} - {self.nom} {self.prenom}\n"
        logements_str = "\n".join([str(logement) for logement in self.logements.values()])
        return prop_str + "Liste des Logements : " + logements_str
    def ajoutLog(self, lg):
        if len(self.logements) >= 20:
            raise Exception("Deppassement")
        else:
            self.logements[lg.numero] = lg

    def modifLog(self, lg, v):
        if lg.numero in self.logements:
            self.logements[lg.numero].modifSurface(v)

    def calculimpot(self):
        total_impot = sum([logement.impot() for logement in self.logements.values()])
        return total_impot

class Agence:
    def __init__(self, L=None):
        self.props = L if L is not None else []

    def contains(self, idp):
        return any(prop.idprop == idp for prop in self.props)

    def ajoutProp(self, p):
        if p.idprop not in [prop.idprop for prop in self.props] and p.logements:
            self.props.append(p)
        else:
            return "Erreur: Proprietaire deja  enregistré ou aucun logement disponible."

    def ajoutLogProp(self, p, lg):
        if p.idprop in [prop.idprop for prop in self.props]:
            p.ajoutLog(lg)

    def trierProp(self):
        return [prop.idprop for prop in sorted(self.props, key=lambda x: len(x.logements))]

    def __str__(self):
        prop_info = [f"{prop} ; Impots : {prop.calculimpot()}" for prop in self.props]
        return "\n".join(prop_info)
