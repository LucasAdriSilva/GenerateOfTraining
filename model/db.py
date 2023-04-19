
import sqlite3
from model.response import Response
import os, datetime
import time, json


DATABASE = 'database.db'

class Db:
    def save(data):
        start_time = time.time()
        response = Response()
        try:
           conn = sqlite3.connect(DATABASE)
           c = conn.cursor()
           c.execute("INSERT INTO user(ip) VALUES (?)", (data["ip"],))
           conn.commit()
           response.data = c.lastrowid
           c.close()
        except Exception as e:
            end_time = time.time()
            print(f"Tempo gasto em save(): {end_time - start_time} segundos ---- ERR: {e}")
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em save(): {end_time - start_time} segundos")
        return response

    def get_ip(ip):
        start_time = time.time()
        response = Response()
        try:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute("SELECT * FROM user WHERE ip = ?", (ip,))
            data = c.fetchone()
            c.close()
            response.data = data
        except Exception as e:
            end_time = time.time()
            print(f"Tempo gasto em get_ip(): {end_time - start_time} segundos ---- ERR: {e}")
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em get_ip(): {end_time - start_time} segundos")
        return response
     
    def get(param, value):
        start_time = time.time()
        response = Response()
        try:
           conn = sqlite3.connect(DATABASE)
           c = conn.cursor()
           c.execute("SELECT * FROM user WHERE {param} = ?", (value,))
           data = c.fetchone()
           c.close()
           response.data = data
        except Exception as e:
            end_time = time.time()
            print(f"Tempo gasto em get(): {end_time - start_time} segundos ---- ERR: {e}")
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em get(): {end_time - start_time} segundos")
        return response

    def update_user(ip, newUser):
        start_time = time.time()
        #instancia uma classe de resposta
        response = Response()
        print(newUser)
        try:
            verification_ip = Db.get_ip(ip).data

            if verification_ip != None:
                conn = sqlite3.connect(DATABASE)
                c= conn.cursor()               
                treino_str = json.dumps(newUser['Treino'])
                c.execute("""
                            INSERT INTO user(ip, Treino, days, pairedSets)
                            VALUES (?,?,?,?)
                            ON CONFLICT(ip) DO UPDATE SET
                            Treino = ?,
                            days = ?,
                            pairedSets = ?
                        """, (ip, treino_str, newUser['days'], newUser['pairedSets'], treino_str, newUser['days'], newUser['pairedSets']))
                conn.commit()
                c.close()           
        except Exception as e:
            end_time = time.time()
            print(f"Tempo gasto em update_user(): {end_time - start_time} segundos ---- ERR: {e}")
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em update_user(): {end_time - start_time} segundos")
        return response
    
    def update_data(ip, paran, value):
        start_time = time.time()
        #instancia uma classe de resposta
        response = Response()
        try: 
            conn = sqlite3.connect(DATABASE)
            c= conn.cursor()     
            if isinstance(value, list):
                value = json.dumps(value)
            elif isinstance(value, dict):
                value = json.dumps(value)
            c.execute("UPDATE user SET {} = ? WHERE ip = ? ".format(paran), (value, ip))
            conn.commit()
            c.close()           
        except Exception as e:
            end_time = time.time()
            print(f"Tempo gasto em update_user(): {end_time - start_time} segundos ---- ERR: {e}")
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em update_user(): {end_time - start_time} segundos")
        return response
    
    def createTable(name):
        # Conecte-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        # Crie um cursor
        c = conn.cursor()
        # Verifique se a tabela já existe
        c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        result = c.fetchone()
        # Se a tabela não existe, crie-a
        if not result:
            c.execute(f'''CREATE TABLE {name} (
                        IP TEXT UNIQUE,
                        Treino TEXT,
                        days INTEGER,
                        pairedSets TEXT,
                        Training TEXT,
                        chosenTraining TEXT,
                        historyTraining TEXT
                        )''')

        # Salve as mudanças
        conn.commit()
        # Feche a conexão
        conn.close()
