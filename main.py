from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    Gender: str
    HeightCm: int
    WeightKg: int

class ItemList(BaseModel):
    __root__: List[Item]

class PersonBmiHealthIndex(BaseModel):
    Gender: str
    HeightCm: int
    WeightKg: int
    BmiResult: float
    BmiCategory: str
    HealthRisk: str

class ListPersonBmiHealthIndex(BaseModel):
    personListDetails: List[PersonBmiHealthIndex]
    overweightCount: int

app = FastAPI()

@app.post("/")
async def bmi_calculator(item: ItemList):
    if item is not None:
        listPerson = []
        overweightCount = 0
        bmiCategory = ""
        healthRisk = ""
        for i in item.__root__:
            bmiIndex = round((float(i.WeightKg)/float((i.HeightCm/100)**2)), 2)
            if bmiIndex <= 18.4:
                bmiCategory = "Underweight"
                healthRisk = "Malnutrition risk"
            elif bmiIndex >=18.5 and bmiIndex <= 24.9:
                bmiCategory = "Normal weight"
                healthRisk = "Low risk"
            elif bmiIndex >=25 and bmiIndex <= 29.9:
                bmiCategory = "Overweight"
                healthRisk = "Enhanced risk"
                overweightCount +=1
            elif bmiIndex >=30 and bmiIndex <= 34.9:
                bmiCategory = "Moderately obese"
                healthRisk = "Medium risk"
            elif bmiIndex >=35 and bmiIndex <= 39.9:
                bmiCategory = "Severely obese"
                healthRisk = "High risk"
            elif bmiIndex >=40:
                bmiCategory = "Very severely obese"
                healthRisk = "Very high risk"
            else:
                bmiCategory = "Undefined"
                healthRisk = "Undefined"

            personDetails = PersonBmiHealthIndex(
                Gender = i.Gender,
                WeightKg = i.WeightKg,
                HeightCm = i.HeightCm,
                BmiResult = bmiIndex,
                BmiCategory = bmiCategory,
                HealthRisk = healthRisk
                )
            listPerson.append(personDetails)
        listPersonDetails= ListPersonBmiHealthIndex(personListDetails=listPerson,overweightCount=overweightCount)

    return listPersonDetails