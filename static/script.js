document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const form = document.getElementById("myForm");
    const resultDiv = document.getElementById("result");
    const selectedAppliancesDiv = document.getElementById("selectedAppliances");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const zipCodeInput = document.getElementById("zipCodeInput");
        const zipCode = zipCodeInput.value;

        const appliances = [];
        const applianceCheckboxes = document.querySelectorAll('input[name="appliances[]"]:checked');
        applianceCheckboxes.forEach(function (checkbox) {
            appliances.push(checkbox.value);
        });

        var csrfTokenInput = document.querySelector('input[name="csrf_token"]').value;


        if (zipCode.length === 5 && /^\d+$/.test(zipCode)) {
            resultDiv.innerHTML = "Processing...";

            const formData = new FormData();
            formData.append("csrf_token", csrfTokenInput); // Include the CSRF token
            formData.append("zipCode", zipCode);
            appliances.forEach((appliance, index) => {
                formData.append(`appliance${index}`, appliance);
            });

            sendZipCode(formData);
        } else {
            resultDiv.innerHTML = "Please enter a valid 5-digit zip code.";
        }
    });

    function sendZipCode(formData) {
        axios.post("/index.html", formData)
            .then(function (response) {
                console.log(response.data); // Log the entire response data
                resultDiv.innerHTML = "Result: " + response.data.result;
                
                // Check if processingResultsDiv exists before setting innerHTML
                if (selectedAppliancesDiv) {
                    if (response.data.appliances) {
                        selectedAppliancesDiv.innerHTML = "Selected Appliances: " + response.data.appliances.join(", ");
                    } else {
                        selectedAppliancesDiv.innerHTML = "No appliances selected.";
                    }
                }
            })
            .catch(function (error) {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    resultDiv.innerHTML = "Server Error: " + error.response.status + " - " + error.response.statusText;
                    console.error("Server Error:", error.response.data);
                } else if (error.request) {
                    // The request was made but no response was received
                    resultDiv.innerHTML = "No response received from the server.";
                    console.error("No response received:", error.request);
                } else {
                    // Something happened in setting up the request that triggered an error
                    resultDiv.innerHTML = "Request Error: " + error.message;
                    console.error("Request Error:", error.message);
                }
            });
    }
})    
