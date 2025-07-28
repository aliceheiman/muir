# constants.py

# Todo: add all models
BIOPHYSICAL_DB_LUCODE_LABEL = "lucode"
BIOPHYSICAL_DB_COLUMNS = {
    "AnnualWaterYield": [
        "usle_c",
        "usle_p",
        "load_p",
        "eff_p",
        "crit_len_p",
        "root_depth",
        "Kc",
        "LULC_veg"
    ],
    "Carbon": [ 
        "C_above",
        "C_below",
        "C_soil",
        "C_dead"
    ],
    "CoastalBlueCarbon": [
        "is_coastal_blue_carbon_habitat"
    ],
    "ForestCarbonEdgeEffect": [
        "is_tropical_forest",
        "C_above",
        "C_below",
        "C_soil",
        "C_dead",
    ],
    "NDR": [
        "load_type_p",
        "load_p",
        "eff_p",
        "crit_len_p",
        "load_type_n",
        "load_n",
        "eff_n",
        "crit_len_n",
        "proportion_subsurface_n",
    ],
    "Pollination": [
        "nesting_cavity_availability_index",
        "nesting_ground_availability_index",
        "floral_resources_spring_index",
        "floral_resources_summer_index"
    ],
    "SDR": [
        "usle_c",
        "usle_p",
    ],
    "SeasonalWaterYield": [
        "Kc_1",
        "Kc_2",
        "Kc_3",
        "Kc_4",
        "Kc_5",
        "Kc_6",
        "Kc_7",
        "Kc_8",
        "Kc_9",
        "Kc_10",
        "Kc_11",
        "Kc_12",
        "CN_A",
        "CN_B",
        "CN_C",
        "CN_D"
    ],
    "UrbanCooling": [
        "Shade",
        "Kc",
        "Albedo",
        "Green_area",
        "building_intensit"
    ],
}