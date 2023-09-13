document.addEventListener("DOMContentLoaded", function () {
    // Fetch the CSRF token from the hidden input field
    const form = document.getElementById("myForm");
    //const appliancesForm = document.getElementById("appliancesForm");
    const resultDiv = document.getElementById("result");
    //const processingResultsDiv = document.getElementById("processingResults");

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
            formData.append("appliances", JSON.stringify(appliances)); // Convert appliances to JSON

            sendZipCode(formData);
        } else {
            resultDiv.innerHTML = "Please enter a valid 5-digit zip code.";
        }
    });

    function sendZipCode(formData) {
        axios.post("/application.html", formData)
            .then(function (response) {
                resultDiv.innerHTML = "Result: " + response.data.result;
                processingResultsDiv.innerHTML = "Selected Appliances: " + response.data.appliances.join(", ");
            })
            .catch(function (error) {
                resultDiv.innerHTML = "Error processing the data.";
            });
    }
});
