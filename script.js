document.addEventListener("DOMContentLoaded", function(){
    
    // checking if form was submitted
    document.querySelector("form").onsubmit = function() {

        // show success message
        alert("Successfully submitted!");

        // saving all form inputs to seperate variables
        let subject = document.querySelector("#subject").value;
        let firstName = document.querySelector("#first-name").value;
        let phoneNumber = document.querySelector("#phone-number").value;
        let emailAddress = document.querySelector("#email-address").value;
        let nationality = document.querySelector("#nationality").value;
        let message = document.querySelector("#message").value;
        
        // create an array with user data
        let userData = [subject, firstName, phoneNumber, emailAddress, nationality, message];
        
        // validate user input
        if (subject.length == 0 || firstName.length == 0 || phoneNumber.length == 0 || emailAddress.length == 0 || nationality.length == 0 || message.length == 0) {
            alert("Error, cannot submit form!");
        }
        else {
            // populate div with user's data
            userData.forEach(item => {
                document.querySelector("#form-success").insertAdjacentText(item);
            });
        }

        return false;
    }
});
