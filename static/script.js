document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const form = document.getElementById("myForm");
    //const zipCodeDiv = document.getElementById("zipCode");
    //const selectedAppliancesDiv = document.getElementById("selectedAppliances");
    

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const zipCodeInput = document.getElementById("zipCodeInput");
        const zipCode = zipCodeInput.value;

        // Check if the zipCode is a 5-digit number using a regular expression
        const zipCodePattern = /^\d{5}$/;
        if (!zipCodePattern.test(zipCode)) {
            // Display an error message or take appropriate action
            alert("Please enter a valid 5-digit zip code.");
            return; // Exit the function to prevent further processing
        }

        const appliances = [];
        const applianceCheckboxes = document.querySelectorAll('input[name="appliances[]"]:checked');
        applianceCheckboxes.forEach(function (checkbox) {
            appliances.push(checkbox.value);
        });
        
        // Check if at least one appliance is selected
        if (appliances.length === 0) {
            // Display an error message or take appropriate action
            alert("Please select at least one Appliance.");
            return; // Exit the function to prevent further processing
        }

        const csrfTokenInput = document.querySelector('input[name="csrf_token"]').value;

        const formData = new FormData();
        console.log(formData)
        formData.append("csrf_token", csrfTokenInput);
        formData.append("zipCode", zipCode);
        appliances.forEach((appliance) => {
            formData.append("appliances[]", appliance);
        });
        console.log("Selected Appliances:", appliances);
        // Send the data to the server using an HTTP POST request (e.g., with Axios)
        sendZipCode(formData);
    });

    function sendZipCode(formData) {
        axios.post("/submit", formData)
        .then(function (response) {
            const data = response.data;
            if (data.redirect) {
                // Redirect to the /result route
                window.location.href = data.redirect;
            } else {
                // Handle other data or errors
                console.error("Unexpected response:", data);
            }
        })
        .catch(function (error) {
            // Handle errors
            console.error("An error occurred:", error);
        });
    }
});