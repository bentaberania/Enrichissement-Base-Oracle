import cx_Oracle  #connecter à oracle
import pandas as pd  #Bib de python:manipuler et exporter données

#chaîne de cnx (DSN) à Oracle (nom du serveur Oracle, port par défaut D'Oracle, id de la base Oracle "$ORACLE_SID")
dsn = cx_Oracle.makedsn("oracle2", 1521, sid="oracle2") 

conn = cx_Oracle.connect(user="raniabentabe", password="oracle", dsn=dsn)
print("Connexion réussie à Oracle !!!")

#cursor pour exécuter les requêtes SQL
cursor = conn.cursor()

tables = ["VINR", "PRODUCTEURR", "RECOLTER"]

#liste des colonnes de la structure du dictionnaire
data_Dict = []

descriptions = {
    "NVIN": "Id unique du vin",
    "CRU": "Appellation du vin",
    "DEGRE": "Degré d'alcool (en % vol)",

    "NPROD": "Id du producteur",
    "NOM": "Nom du producteur",
    "PRENOM": "Prénom du producteur",
    "REGION": "Région viticole",

    "ANNEE": "Année de la récolte du vin",
    "QTE": "Quantité de vin récoltée (en litre)"
}

for table in tables:
	#1:structure de la table
    cursor.execute(f"""
        SELECT COLUMN_NAME, DATA_TYPE, DATA_LENGTH, NULLABLE
        FROM USER_TAB_COLUMNS
        WHERE TABLE_NAME = '{table}'
    """) 
	
    columns = cursor.fetchall()
	#2:primary key
    cursor.execute(f"""
        SELECT cols.COLUMN_NAME
        FROM all_constraints cons
        JOIN all_cons_columns cols
        ON cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner
        WHERE cons.constraint_type = 'P'
        AND cols.table_name = '{table}'
    """)
    pk_columns = {row[0] for row in cursor.fetchall()}

	#3:foreign key
    cursor.execute(f"""
        SELECT a.COLUMN_NAME, c_pk.TABLE_NAME AS REFERENCED_TABLE
        FROM all_cons_columns a
        JOIN all_constraints c
        ON a.owner = c.owner AND a.constraint_name = c.constraint_name
        JOIN all_constraints c_pk
        ON c.r_owner = c_pk.owner AND c.r_constraint_name = c_pk.constraint_name
        WHERE c.constraint_type = 'R'
        AND a.table_name = '{table}'
    """)
    fk_info = cursor.fetchall()
    fk_columns = {row[0]: row[1] for row in fk_info}

    for col in columns:
        column_name, data_type, data_length, nullable = col
        #liste pour stocker contraintes (PK, FK)
        constraint = []
        if column_name in pk_columns:
            constraint.append("PRIMARY KEY")
        if column_name in fk_columns:
            constraint.append(f"FOREIGN KEY -> {fk_columns[column_name]}")
        if nullable == 'N':
            constraint.append("NOT NULL")

        data_Dict.append({
            "Table": table,
            "Colonne": column_name,
            "Type": f"{data_type}({data_length})",
            "Clé / Contrainte": ", ".join(constraint),
            "Description": descriptions.get(column_name, "")
        })

df = pd.DataFrame(data_Dict)
df.to_csv("dictionnaire_donnees.csv", index=False)
#df.to_excel("dictionnaire_donnees.xlsx", index=False)

print(df.to_string(index=False))


