document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const form = document.getElementById("myForm");
    const resultDiv = document.getElementById("result");
    const selectedAppliancesDiv = document.getElementById("selectedAppliances");
    

    console.log("Form element:", form);

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const zipCodeInput = document.getElementById("zipCodeInput");
        const zipCode = zipCodeInput.value;

        console.log(zipCodeInput);
        console.log(zipCode);

        const appliances = [];
        const applianceCheckboxes = document.querySelectorAll('input[name="appliances[]"]:checked');
        applianceCheckboxes.forEach(function (checkbox) {
            appliances.push(checkbox.value);
        });
        console.log("Selected Appliances:", appliances);
        const csrfTokenInput = document.querySelector('input[name="csrf_token"]').value;

        const formData = new FormData();
        formData.append("csrf_token", csrfTokenInput);
        formData.append("zipCode", zipCode);
        appliances.forEach((appliance, index) => {
            formData.append(`appliance${index}`, appliance);
        });

        // Send the data to the server using an HTTP POST request (e.g., with Axios)
        sendZipCode(formData);
    });

    function sendZipCode(formData) {
        axios.post("/submit", formData)
            .then(function (response) {
                // Handle the response from the server
                console.log(response)
                if (response.data.result) {
                    resultDiv.innerHTML = "Result: " + response.data.result;
                } else {
                    resultDiv.innerHTML = "No result available.";
                }

                // Check if selected appliances data is available
                if (response.data.appliances) {
                    selectedAppliancesDiv.innerHTML = "Selected Appliances: " + response.data.appliances.join(", ");
                } else {
                    selectedAppliancesDiv.innerHTML = "No appliances selected.";
                }
                window.location.href = "/result";
            })
            .catch(function (error) {
                // Handle errors
                resultDiv.innerHTML = "An error occurred while processing the request.";
                selectedAppliancesDiv.innerHTML = "No appliances selected.";
            });
    }
});