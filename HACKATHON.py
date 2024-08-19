# Mock data for crops, soil types, and diseases
crop_data = {
    "wheat": {"soil": "loam", "season": "winter", "pH_range": (6.0, 7.5)},
    "rice": {"soil": "clay", "season": "rainy", "pH_range": (5.0, 6.5)},
    "maize": {"soil": "sandy_loam", "season": "summer", "pH_range": (5.5, 7.0)},
}

soil_data = {
    "loam": {"pH": 6.8, "water_retention": "medium"},
    "clay": {"pH": 5.8, "water_retention": "high"},
    "sandy_loam": {"pH": 6.2, "water_retention": "low"},
}

# Sample function to suggest crops based on soil type and pH level
def suggest_crops(soil_type, soil_pH):
    suggestions = []
    for crop, data in crop_data.items():
        if data["soil"] == soil_type and data["pH_range"][0] <= soil_pH <= data["pH_range"][1]:
            suggestions.append(crop)
    return suggestions if suggestions else "No suitable crops found."

# Example function to manage soil, suggesting improvements if pH is out of range
def manage_soil(soil_type, soil_pH):
    if soil_type not in soil_data:
        return "Unknown soil type. Please enter a valid soil type."
    
    soil_info = soil_data[soil_type]
    if soil_pH < soil_info["pH"]:
        return f"Increase soil pH by adding lime."
    elif soil_pH > soil_info["pH"]:
        return f"Decrease soil pH by adding sulfur."
    else:
        return "Soil pH is optimal."

# Sample function for disease identification based on symptoms (mock data)
disease_data = {
    "yellowing_leaves": "Nitrogen deficiency",
    "brown_spots": "Fungal infection",
}

def identify_disease(symptoms):
    return disease_data.get(symptoms, "No disease found for the given symptoms.")

# Main function to simulate farmer interaction
def farmer_assistant(soil_type, soil_pH, symptoms=None):
    print("Crop and Soil Management System")
    print("------------------------------")
    
    print(f"\nSoil Type: {soil_type}")
    print(f"Soil pH: {soil_pH}")
    
    # Crop suggestions
    print("\nSuggested Crops:")
    crops = suggest_crops(soil_type, soil_pH)
    print(crops)
    
    # Soil management advice
    print("\nSoil Management Advice:")
    advice = manage_soil(soil_type, soil_pH)
    print(advice)
    
    # Disease identification (if symptoms are provided)
    if symptoms:
        print("\nDisease Identification:")
        disease = identify_disease(symptoms)
        print(disease)

# Example usage of the system
farmer_assistant("loam", 6.8, symptoms="yellowing_leaves")
