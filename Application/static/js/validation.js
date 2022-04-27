// const emailinput = document.querySelector("#emailinput");
// const emailFeedBackArea = document.querySelector(".emailFeedBackArea")

// emailinput.addEventListener('keyup', (e)=>{
//    const emailVal = e.target.value;

//    emailinput.classList.remove("is-valid");
//    emailFeedBackArea.style.display = "none";

//    if (emailVal.length > 0) {
//        fetch('index.html', {
//            body: JSON.stringify({ email: emailVal }),
//            method: "POST",
//        })
//            .then((res) => res.json())
//            .then((data) => {
//                console.log("data",data);
//                if (data.email_error) {
//                    emailinput.classList.add("is-valid");
//                    feedBackArea.style.display = "block";
//                    feedBackArea.innerHTML = `<p>${data.email_error}</p>`;
//                }
//            })
//    }
// })












//let emailerror = true
//
//function emailValidation() {
//    let email = $("#email").val();
//    let mailformat = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
//    if (email == "") {
//        $("#error-email").text("Please Enter Your Email.");
//        emailerror = false;
//    }
//    else if(mailformat.test(email) == false) {
//        $("#error-email").text("Please Enter Valid email")
//        emailerror = false;
//    }
//    else {
//        $("#error-email").text("");
//        emailerror = true;
//    }
//
//}
//
//$('#submit').click(function(e){
//    e.preventDefault();
//    emailValidation();
//    if(emailerror == true) {
//        return true;
//    }
//    else{
//        return false;
//    }
//});