import numpy as np
import keras
import sys

# Load the models.
acr  = keras.models.load_model("acr.h5")
bdsp = keras.models.load_model("bdsp.h5")
mrgp = keras.models.load_model("mrgp.h5")
rwat = keras.models.load_model("rwat.h5")
ten  = keras.models.load_model("ten.h5")
ybl  = keras.models.load_model("ybl.h5")

def acres(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return acr.predict(inputs).argmax(1)[0]

def beds(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return bdsp.predict(inputs).argmax(1)[0]

def mortgage(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return mrgp.predict(inputs)[0][0]

def has_water(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return rwat.predict(inputs).argmax(1)[0]

def tenure(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return ten.predict(inputs).argmax(1)[0]

def years_built(
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship):
    inputs = np.array([[
        age, marital_status, num_family_members, wage, educational_attainment,
        vehicle_to_work, sex, race, num_vehicles, has_disability,
        has_family_income, citizenship]])
    return ybl.predict(inputs).argmax(1)[0]

if __name__ == "__main__":
    # inputs = (35, 2, 3, 35000, 6, 1, 1, 2, 1, 1, 1, 1)
    # print("Number of acres: {}".format(acres(*inputs)))
    # print("Number of beds: {}".format(beds(*inputs)))
    # print("Mortgage: {}".format(mortgage(*inputs)))
    # print("Has Running Water: {}".format(has_water(*inputs)))
    # print("Tenure {}".format(tenure(*inputs)))
    # print("Years built: {}".format(years_built(*inputs)))
    inputList = []
    for i in range(1,13):
        inputList.append((sys.argv[i]))
    inputs = tuple(inputList)
    v1 = acres(*inputs)
    v2 = beds(*inputs)
    v3 = mortgage(*inputs)
    v4 = has_water(*inputs)
    v5 = tenure(*inputs)
    v6 = years_built(*inputs)
    print("{}, {}, {}, {}, {}, {}".format(v1, v2, v3, v4, v5, v6))
