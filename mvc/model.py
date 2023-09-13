class ZipCodeModel:
    @staticmethod
    def process_zip(zip_code):
        # Simulate processing logic for the zip code
        return {"result": "Processed data for zip code: " + zip_code}
    
    @staticmethod
    def process_appliances(selected_appliances):
        # Simulate processing logic for selected appliances
        appliance_list = ", ".join(selected_appliances)
        return {"result": "Processed selected appliances: " + appliance_list}
