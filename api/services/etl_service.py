import re
import pandas as pd
import unidecode 
import numpy as np

NAMES_EQUIVALENCE = {'bicepscurl': 'maquina bicepscurl',
'maquina de tira multiuso': 'maquina tira multiuso',
'mancuernas bicep': 'mancuernas biceps',
'barra bicep':'barra biceps',
'maquina del fondo': 'maquina del fondo 1',
'maquina bicep predicador': 'biceps predicador',
'barras en agarre neutro x 5': 'barras con agarre neutro x 5',
'barras agarre neutro x 5': 'barras con agarre neutro x 5',
'sentadillas con peso': 'sentadilla con peso',
'maquina tira multi uso triceps': 'maquina tira multiuso triceps',
'maquina tira multi uso': 'maquina tira multiuso',
'barra en agarre neutro x 5': 'barras con agarre neutro x 5',
'barra agarre neutro x 5': 'barras con agarre neutro x 5',
'maquina tira multiuso bicep': 'maquina tira multiuso biceps',
'mancuerna biceps': 'mancuernas biceps',
'maquina tira multiuso tricep': 'maquina tira multiuso triceps',
'mancuerna bicep': 'mancuernas biceps',
'mancuerna hombro':'mancuernas hombro',
'reno con peso': 'remo con peso',
'calentismiento medio': 'calentamiento medio',
'calentamiento': 'calentamiento medio',
'barra con agarre neutro x 5': 'barras con agarre neutro x 5',
'barras en agarre supino': 'barras con agarre supino',
'maquina tira multiuso bicep.': 'maquina tira multiuso biceps',
'maquina  bicepscurl': 'maquina bicepscurl',
'barras en agarre neutro x 6': 'barras con agarre neutro x 6',
'barra en agarre neutro x 6': 'barras con agarre neutro x 6',
'barra con agarre neutro x 6': 'barras con agarre neutro x 6',
'barra con agarre en prona x 6': 'barras con agarre prono x 6',
'barras agarre neutro x 6': 'barras con agarre neutro x 6', 
'barra 6 en subida con peso': 'barras 6 en subida con peso',
'barras con agarre neutro x6': 'barras con agarre neutro x 6',
'barra con agarre neutro x 5': 'barras con agarre neutro x 5',
'biceps con barra': 'barra biceps',
'bicep': 'biceps',
'tricep y espalda': 'espalda y triceps', 
'triceps y espalda': 'espalda y triceps'
}

def from_brackets_extracter(line: str):
    lower_bound, upper_bound, unit = 0, 0, ""
    
    if len(re.findall(r"\[(.+),", line)) >= 1:
        lower_bound = re.findall(r"\[(.+),", line)[0] 

    if len(re.findall(r",\s?([\d\.]+)\]", line)) >= 1:
        upper_bound = re.findall(r",\s?([\d\.]+)\]", line)[0]

    if len(re.findall(r"\]([\w]+)", line)) >= 1:
        unit = re.findall(r"\]([\w]+)", line)[0]

    return float(lower_bound), float(upper_bound), unit

def intern_name_and_weight_extractor(line: str):
    name, weight, lower_bound, upper_bound, failure, unit = "", None, 0, 0, False, ""

    results = line.split("-")

    name = results[0].strip()
    
    if len(results) >= 2:
        name = results[0].strip()
        weight = results[1].strip()
        
        if line.find("[") != -1:
            lower_bound, upper_bound, unit = from_brackets_extracter(line)
            weight = (lower_bound + upper_bound) / 2

        else:
            if len(re.findall(r"-\s?([\d\.])+", line)) >= 1:
                weight = re.findall(r"-\s?([\d\.]+)", line)[0]
                unit = re.findall(r"-\s?[\d\.]+([\w]+)", line)[0]
            else:
                unit = None

    failure = line.lower().find("falla") != -1

    return name, weight, lower_bound, upper_bound, failure, unit                


def general_data_extractor(year):
    trainig_data = {
        "date": [],
        "exercise_day": [],
        "name": [],
        "weight": [],
        "lower_bound": [],
        "upper_bound": [],
        "failure": [],
        "unit": []
    }

    exercise_day = ""
    
    with open(f"Datos de entreno {year}.txt", "r", encoding="utf-8") as file:
        date = np.nan
        
        for line in file.readlines():
            result = re.search(r"\d{1,2}\/\d{1,2}\/" + str(year), line)

            if result:
                date = result.group()
                
                if line.find("-") != -1:
                    exercise_day = line.split("-")[1].strip()
                    
            else:
                name, weight, lower_bound, upper_bound, failure, unit = intern_name_and_weight_extractor(line)
                
                trainig_data["date"].append(date)
                trainig_data["exercise_day"].append(exercise_day)
                trainig_data["name"].append(name)
                trainig_data["weight"].append(weight)
                trainig_data["lower_bound"].append(lower_bound)
                trainig_data["upper_bound"].append(upper_bound)
                trainig_data["failure"].append(failure)
                trainig_data["unit"].append(unit)
                        
    return pd.DataFrame(trainig_data)

def dataframe_cleaning(dataframe: pd.DataFrame):
    partial_dataframe = dataframe[~dataframe["date"].isna()]
    final_dataframe = partial_dataframe[partial_dataframe["name"] !=""]

    return final_dataframe

def dtypes_transformation(dataframe: pd.DataFrame):
    dataframe["weight"] = dataframe["weight"].astype(float)
    dataframe["date"] = pd.to_datetime(dataframe["date"], dayfirst=True)

    return dataframe

def names_homologation(dataframe: pd.DataFrame):
    dataframe["exercise_day"] = dataframe["exercise_day"].map(lambda x: unidecode.unidecode(x.lower()))
    dataframe["name"] = dataframe["name"].map(lambda x: unidecode.unidecode(x.lower()))

    return dataframe.replace(NAMES_EQUIVALENCE)