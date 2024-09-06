const newpasswordField=document.querySelector('#newpasswordField')
const newpasswordfeedbackarea=document.querySelector('.newpasswordfeedbackarea')

const newconfirmpasswordField=document.querySelector('#newconfirmpasswordField');
const newconfirmpasswordfeedbackarea=document.querySelector('.newconfirmpasswordfeedbackarea')


const submitBtn=document.querySelector('.submit-btn')
const showPasswordToggle=document.querySelector('.showPasswordToggle')


newpasswordField.addEventListener('keyup', (e) => {
    const newPasswordVal=e.target.value;
    if (newPasswordVal.length > 0){
        newpasswordfeedbackarea.style.display="block";
        fetch('/authenticate/validate-newpassword',
        
        {
            body:JSON.stringify({newpassword:newPasswordVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.new_password_error){
                submitBtn.disabled=true;
                newpasswordfeedbackarea.innerHTML=`<p>${data.new_password_error}</p>`
                newpasswordfeedbackarea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
                newpasswordfeedbackarea.style.display="none"
            }
            
        });
    }
});
  
newconfirmpasswordField.addEventListener('keyup',(e)=>{
    const newConfirmPassVal = e.target.value;
    const newPasswordVal=newpasswordField.value;
    console.log(newPasswordVal);
    
    if(newConfirmPassVal.length>0){
        newconfirmpasswordfeedbackarea.style.display="block";
        fetch('/authenticate/validate-newconfirmpassword',
        
        {
            body: JSON.stringify({
                newpassword: newPasswordVal,
                newconfirmpassword: newConfirmPassVal
            }),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.new_confirm_password_error){
                submitBtn.disabled=true;
                newconfirmpasswordfeedbackarea.innerHTML=`<p>${data.new_confirm_password_error}</p>`
                newconfirmpasswordfeedbackarea.style.display="block"
            }
            else{
                submitBtn.removeAttribute("disabled")
                newconfirmpasswordfeedbackarea.style.display="none"
            }
            
        });
    }
})
// const csrfToken = getCookie('csrftoken');

// submitBtn.addEventListener('click', (e) => {
//     // e.preventDefault(); // Prevent form submission
    
//     const newConfirmPassVal = newconfirmpasswordField.value;
//     const newPasswordVal = newpasswordField.value;

//     // Perform any additional validation or checks before submitting the form

//     fetch('/authenticate/newpassowrdset', {
//         body: JSON.stringify({
//             newpassword: newPasswordVal,
//             newconfirmpassword: newConfirmPassVal
//         }),
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken
//         },
//         method: "POST",
//     })
//     .then(res => res.json())
//     .then(data => {
//         // Handle the response from the API
//         console.log(data);
//         if(data.new_update_password_error){
//             submitBtn.disabled=true;
//         }
//         else{
            
//             submitBtn.removeAttribute("disabled")
//         }
//     })
    
// });


// function getCookie(name) {
//     const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
//     return cookieValue ? cookieValue.pop() : '';
//   }
  
const handleToggleInput=(e)=>{
    if(showPasswordToggle.textContent==='SHOW'){
        showPasswordToggle.textContent="HIDE"
        newpasswordField.setAttribute("type","text")
    }
    else{
        showPasswordToggle.textContent="SHOW"
        newpasswordField.setAttribute("type","password")
    }
}

showPasswordToggle.addEventListener('click',handleToggleInput);
