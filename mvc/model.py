class ZipCodeModel:
    @staticmethod
    def process_data(zip_code, selected_appliances):
        print("Received zip_code:", zip_code)
        print("Received selected_appliances:", selected_appliances)
    # Your processing logic here
        result = "Processed data for zip code: " + zip_code
        appliances = selected_appliances
        return {"result": result, "appliances": appliances}
    #@staticmethod
    #def process_zip(zip_code):
    # Simulate processing logic for the zip code
    #    result = "Processed data for zip code: " + zip_code
    #    print("Result:", result)  # Add this line for debugging
    #    return {"result": result}
    
    #@staticmethod
   # def process_appliances(selected_appliances):
        # Simulate processing logic for selected appliances
    #    appliance_list = ", ".join(selected_appliances)
    #    return {"result": "Processed selected appliances: " + appliance_list}
