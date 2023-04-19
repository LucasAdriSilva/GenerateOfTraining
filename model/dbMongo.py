
from pymongo import MongoClient
from model.response import Response
import os, datetime
import time
client = MongoClient(os.environ.get('MONGO_DB'))

db = client.BWDesenv


class Db:
    def save(data):
        start_time = time.time()
        response = Response()
        try:
            response.data = db.user.insert_one(data)
        except Exception as e:
            response.message = f"Erro no banco de dados ---> {e}"
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em save(): {end_time - start_time} segundos")
        return response

    def get_ip(ip):
        start_time = time.time()
        response = Response()
        try:
            response.data = db.user.find_one({"ip": ip})
        except Exception as e:
            response.message = f"Erro de banco de dados ---> {e}"
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em get_ip(): {end_time - start_time} segundos")
        return response
      
    def get(param, value):
        start_time = time.time()
        response = Response()
        try:
            response.data = db.user.find_one({param: value})
        except Exception as e:
            response.message = f"Erro de banco de dados ---> {e}"
            response.ok = False
            return response
        end_time = time.time()
        print(f"Tempo gasto em get(): {end_time - start_time} segundos")
        return response

    def update_user(ip, newUser):
        #instancia uma classe de resposta
        response = Response()
        try:
            verification_ip = Db.get_ip(ip).data

            if verification_ip != None:
                response.data = db.user.find_one_and_update(
                    {'ip': verification_ip['ip']}, 
                    {"$set": newUser}
                )
        except Exception as e:
            #Erro no banco
            response.ok = False 
            response.message = f"Erro de banco de dados ---> {e}"
            return response
        return response
    





