class ZipCodeModel:
    @staticmethod
    def zip_code_data(zip_code):
        print("Received zip_code:", zip_code)
        zipCode = "Processed data for zip code: " + zip_code
        return {"zipCode": zipCode}
    @staticmethod
    def selected_appliances_data(selected_appliances):
        print("Received selected_appliances:", selected_appliances)
        appliances = selected_appliances
        return{"appliances": appliances}
