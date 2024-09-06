function validateForm(){
    var intialDate=document.searchForm.initialdate_value.value;
    var finalDate= document.searchForm.finaldate_value.value;
    
          
         handleChooseFromMap();
         if( intialDate == "" || finalDate == "" ) {
           document.searchForm.initialdate_value.focus()
           document.getElementById("startDate").innerHTML=  "Please enter your initial date ";  
           document.getElementById("endDate").innerHTML=  "Please enter your final date";
            return false;
         }
         else if( intialDate == "" ) {
           document.searchForm.initialdate_value.focus()
           document.getElementById("startDate").innerHTML=  "Please enter your initial date "; 
          
            return false;
         }
         else if( finalDate == "" ) {
           document.searchForm.finaldate_value.focus()
           document.getElementById("endDate").innerHTML=  "Please enter your final date";
            return false;
         }
         else if(isNaN(input_lat)||input_lat=='' ){
          document.searchForm.Latitude.focus()
          document.getElementById("Lat").innerHTML=  "Please enter your Latitude value or choose from map ";
          return false;
          }
         
         else if(isNaN(input_long)||input_long =='' ){
          document.searchForm.Longitude.focus()
          document.getElementById("Long").innerHTML=  "Please enter your Langitude value or choose from map ";
          return false;
          }
        else {     
          return( true );              
         }
   }
