class ZipCodeModel:
    def __init__(self):
        self.zip_code = None
        self.selected_appliances = []

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def add_appliance(self, appliance):
        self.selected_appliances.append(appliance)

    def get_zip_code(self):
        return self.zip_code

    def get_selected_appliances(self):
        return self.selected_appliances
    
    @staticmethod
    def process_appliances(selected_appliances):
        # Simulate processing logic for selected appliances
        appliance_list = ", ".join(selected_appliances)
        return {"result": "Processed selected appliances: " + appliance_list}
