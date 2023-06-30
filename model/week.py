# classe para tratar as semanas
class week:
    def __init__(self, week = ["Segunga", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]):
        self.week = week

    def daysOfWeek():
        return ["Segunga", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    
    def convertDays(array):
        new_array = []
        for day in array:
            if day == "Seg":
                new_array.append('Segunda')
            if day == "Ter":
                new_array.append('Terça')
            if day == "Quar":
                new_array.append('Quarta')
            if day == "Quin":
                new_array.append('Quinta')
            if day == "Sex":
                new_array.append('Sexta')
            if day == "Sab":
                new_array.append('Sábado')
            if day == "Dom":
                new_array.append('Domingo')

                 
