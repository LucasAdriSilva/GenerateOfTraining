
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
                Training = json.dumps(newUser['Training'])
                BaseTraining = json.dumps(newUser['BaseTraining'])
                Requireds = json.dumps(newUser['Requireds'])

                c.execute("""
                            INSERT INTO user(
                                ip, Login, Password, UserData, BaseTraining, TrainingDays, Requireds, Training, 
                                 ChosenTraining, HistoryTraining
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ON CONFLICT(ip) DO UPDATE SET
                                Login = ?,
                                Password = ?,
                                UserData = ?,
                                BaseTraining = ?,
                                TrainingDays = ?,
                                Requireds = ?,
                                Training = ?,
                                ChosenTraining = ?,
                                HistoryTraining = ?
                        """, (ip, None, None, None, BaseTraining, newUser['TrainingDays'], Requireds,   Training,  None, None, None, None, None, BaseTraining, 
                            newUser['TrainingDays'], Requireds, Training, 
                            None, None))

                            # ChosenTraining = ?,
                            # HistoryTraining = ?
                # 'ip': session['ip'], 'BaseTraining': allTreinos, 'TrainingDays': days,'Requireds': requireds, 'PairedSets': pairedSets, 'Training': allTreinos['regularTraining'], 'TrainingPairedSets': allTreinos['pairedSetsTraining'], 
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
                        Login TEXT,
                        Password TEXT,
                        UserData TEXT,
                        BaseTraining TEXT,
                        TrainingDays INTEGER,
                        Requireds TEXT,
                        Training TEXT,
                        ChosenTraining TEXT,
                        HistoryTraining TEXT
                        )''')

        # Salve as mudanças
        conn.commit()
        # Feche a conexão
        conn.close()
