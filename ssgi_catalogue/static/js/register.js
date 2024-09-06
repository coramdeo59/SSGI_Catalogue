const usernameField=document.querySelector('#usernameField');//input space
const usernamefeedBackArea=document.querySelector('.invalid_feedback_username')//invalid username
const emailField=document.querySelector('#emailField')
const emailFeedBackArea=document.querySelector('.emailFeedBackArea')
const usernameSuccessOutput=document.querySelector('.usernameSuccessOutput')//valid username
const emailSuccessOutput=document.querySelector('.emailSuccessOutput')
const showPasswordToggle=document.querySelector('.showPasswordToggle')
const showConfirmPasswordToggle=document.querySelector('.showConfirmPasswordToggle')
const submitBtn=document.querySelector('.submit-btn')

const firstnameField = document.getElementById("firstnameField");
const firstnameSuccessOutput = document.querySelector(".firstnameSuccessOutput");
const firstnamefeedBackArea=document.querySelector('.invalid_feedback_firstname')

const middlenameField = document.getElementById("middlenameField");
const middlenameSuccessOutput = document.querySelector(".middlenameSuccessOutput");
const middlenamefeedBackArea=document.querySelector('.invalid_feedback_middlename')

const lastnameField = document.getElementById("lastnameField");
const lastnameSuccessOutput = document.querySelector(".lastnameSuccessOutput");
const lastnamefeedBackArea=document.querySelector('.invalid_feedback_lastname')

const passwordField = document.getElementById("passwordField");
const passwordfeedbackarea=document.querySelector('.passwordfeedbackarea')

const confirmpasswordField=document.querySelector('#confirmpasswordField')
const confirmpasswordfeedbackarea=document.querySelector('.confirmpasswordfeedbackarea')

const countryField=document.querySelector('#countryField')

const sectorField=document.querySelector('#sectorField')

const instituteField=document.querySelector('#instituteField')


firstnameField.addEventListener('keyup', (e) => {
    const firstnameVal = e.target.value;
    firstnameSuccessOutput.textContent = `Checking if ${firstnameVal} is valid`;

    firstnameField.classList.remove("is-invalid");
    firstnamefeedBackArea.style.display = "none";

    if (firstnameVal.length > 0) {
        firstnameSuccessOutput.style.display = "block";
        fetch('/authenticate/validate-firstname',
        
        {
            body:JSON.stringify({firstname:firstnameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            firstnameSuccessOutput.style.display="none"
            if(data.firstname_error){
                submitBtn.disabled=true;
                firstnameField.classList.add("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
                firstnamefeedBackArea.innerHTML=`<p>${data.firstname_error}</p>`
                firstnamefeedBackArea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
            
        });
    }
});
middlenameField.addEventListener('keyup', (e) => {
    const middlenameVal = e.target.value;
    middlenameSuccessOutput.textContent = `Checking if ${middlenameVal} is valid`;

    middlenameField.classList.remove("is-invalid");
    middlenamefeedBackArea.style.display = "none";

    if (middlenameVal.length > 0) {
        middlenameSuccessOutput.style.display = "block";
        fetch('/authenticate/validate-middlename',
        
        {
            body:JSON.stringify({middlename:middlenameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            middlenameSuccessOutput.style.display="none"
            if(data.middlename_error){
                submitBtn.disabled=true;
                middlenameField.classList.add("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
                middlenamefeedBackArea.innerHTML=`<p>${data.middlename_error}</p>`
                middlenamefeedBackArea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
            
        });
    }
});



lastnameField.addEventListener('keyup', (e) => {
    const lastnameVal = e.target.value;
    lastnameSuccessOutput.textContent = `Checking if ${lastnameVal} is valid`;

    lastnameField.classList.remove("is-invalid");
    lastnamefeedBackArea.style.display = "none";

    if (lastnameVal.length > 0) {
        lastnameSuccessOutput.style.display = "block";
        fetch('/authenticate/validate-lastname',
        
        {
            body:JSON.stringify({lastname:lastnameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            lastnameSuccessOutput.style.display="none"
            if(data.lastname_error){
                submitBtn.disabled=true;
                lastnameField.classList.add("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
                lastnamefeedBackArea.innerHTML=`<p>${data.lastname_error}</p>`
                lastnamefeedBackArea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
            
        });
    }
});


usernameField.addEventListener('keyup', (e)=>{
    
    const usernameVal=e.target.value;
    usernameSuccessOutput.textContent=`Checking if ${usernameVal} is valid`
    
    usernameField.classList.remove("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
    usernamefeedBackArea.style.display="none"
    if (usernameVal.length>0){
        usernameSuccessOutput.style.display="block"
        // make an api call to the server
        fetch('/authenticate/validate-username',
        
        {
            body:JSON.stringify({username:usernameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            usernameSuccessOutput.style.display="none"
            if(data.username_error){
                submitBtn.disabled=true;
                usernameField.classList.add("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
                usernamefeedBackArea.innerHTML=`<p>${data.username_error}</p>`
                usernamefeedBackArea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
            
        });
    }
    
})

emailField.addEventListener('keyup',(e)=>{
    const emailVal=e.target.value;
    emailSuccessOutput.textContent=`Checking if ${emailVal} is valid`
    
    emailField.classList.remove("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
    emailFeedBackArea.style.display="none"
    emailSuccessOutput.style.display="block"
    if (emailVal.length>0){
        // make an api call to the server
        fetch('/authenticate/validate-email',
        
        {
            body:JSON.stringify({email:emailVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            emailSuccessOutput.style.display="none";
            if(data.email_error){
                submitBtn.disabled=true;
                emailField.classList.add("is-invalid");//is-invalid is a bootstrap class that makes the box red when invalid input is entered
                emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`
                emailFeedBackArea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
        });
    }
})

passwordField.addEventListener('keyup', (e) => {
    const passwordVal=e.target.value;
    if (passwordVal.length > 0){
        passwordfeedbackarea.style.display="block";
        fetch('/authenticate/validate-password',
        
        {
            body:JSON.stringify({password:passwordVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.password_error){
                submitBtn.disabled=true;
                passwordfeedbackarea.innerHTML=`<p>${data.password_error}</p>`
                passwordfeedbackarea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
                passwordfeedbackarea.style.display="none"
            }
            
        });
    }
});

confirmpasswordField.addEventListener('keyup',(e)=>{
    const confirmPassVal = e.target.value;
    const passwordVal=passwordField.value;
    console.log(passwordVal);
    

    if(confirmPassVal.length>0){
        confirmpasswordfeedbackarea.style.display="block";
        fetch('/authenticate/validate-confirmpassword',
        
        {
            body: JSON.stringify({
                password: passwordVal,
                confirmpassword: confirmPassVal
            }),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.confirm_password_error){
                submitBtn.disabled=true;
                confirmpasswordfeedbackarea.innerHTML=`<p>${data.confirm_password_error}</p>`
                confirmpasswordfeedbackarea.style.display="block"


            }
            else{
                submitBtn.removeAttribute("disabled")
                confirmpasswordfeedbackarea.style.display="none"
            }
            
        });
    }
})

countryField.addEventListener('change', (e) => {
  const selectedCountry = e.target.value;
  
  if (selectedCountry) {
    // Perform your validation or further processing here
    console.log('Selected country is:', selectedCountry);
    fetch('/authenticate/validate-country',
        
        {
            body:JSON.stringify({country:selectedCountry}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.country_error){
                submitBtn.disabled=true;
            }
            else{
                submitBtn.removeAttribute("disabled")
            }
            
        });
  } 
});

sectorField.addEventListener('change', (e) => {
    const selectedSector = e.target.value;
    
    if (selectedSector) {
      // Perform your validation or further processing here
      console.log('Selected sector is:', selectedSector);
      fetch('/authenticate/validate-sector',
          
          {
              body:JSON.stringify({sector:selectedSector}),
              method:"POST",
          }).then(res=>res.json()).then(data=>{
              console.log("data",data);
              if(data.sector_error){
                  submitBtn.disabled=true;
              }
              else{
                  submitBtn.removeAttribute("disabled")
              }
              
          });
    } 
  });

  instituteField.addEventListener('change', (e) => {
    const selectedInstitute = e.target.value;
    
    if (selectedInstitute) {
      // Perform your validation or further processing here
      console.log('Selected institute is:', selectedInstitute);
      fetch('/authenticate/validate-institute',
          
          {
              body:JSON.stringify({institute:selectedInstitute}),
              method:"POST",
          }).then(res=>res.json()).then(data=>{
              console.log("data",data);
              if(data.institute_error){
                  submitBtn.disabled=true;
              }
              else{
                  submitBtn.removeAttribute("disabled")
              }
              
          });
    } 
  });


  
  
  

  
const handleToggleInput=(e)=>{
    if(showPasswordToggle.textContent==='SHOW'){
        showPasswordToggle.textContent="HIDE"
        passwordField.setAttribute("type","text")
    }
    else{
        showPasswordToggle.textContent="SHOW"
        passwordField.setAttribute("type","password")
    }
}

showPasswordToggle.addEventListener('click',handleToggleInput);
