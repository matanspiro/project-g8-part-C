function hideOnLoad() {
  document.getElementById("Events").style.display="block"; //block means "Show"
  document.getElementById("EventText").style.display="none";
  document.getElementById("GoBackButton").style.display="none";
  document.getElementById("RSVP").style.display="none";
}

function getText1() {
  document.getElementById("EventText").style.display="block";
  document.getElementById("EventText1").style.display="block"; 
  document.getElementById("EventText2").style.display="none";
  document.getElementById("EventText3").style.display="none";
  document.getElementById("EventText4").style.display="none";
  document.getElementById("Events").style.display="none";
  document.getElementById("GoBackButton").style.display="block";
  document.getElementById("RSVP").style.display="block";
}

function getText2() {
  document.getElementById("EventText").style.display="block";
  document.getElementById("EventText1").style.display="none";
  document.getElementById("EventText2").style.display="block";
  document.getElementById("EventText3").style.display="none";
  document.getElementById("EventText4").style.display="none";
  document.getElementById("Events").style.display="none";
  document.getElementById("GoBackButton").style.display="block";
  document.getElementById("RSVP").style.display="block";
}

function getText3() {
  document.getElementById("EventText").style.display="block";
  document.getElementById("EventText1").style.display="none";
  document.getElementById("EventText2").style.display="none";
  document.getElementById("EventText3").style.display="block";
  document.getElementById("EventText4").style.display="none";
  document.getElementById("Events").style.display="none";
  document.getElementById("GoBackButton").style.display="block";
  document.getElementById("RSVP").style.display="block";
}

function getText4() {
  document.getElementById("EventText").style.display="block";
  document.getElementById("EventText1").style.display="none";
  document.getElementById("EventText2").style.display="none";
  document.getElementById("EventText3").style.display="none";
  document.getElementById("EventText4").style.display="block";
  document.getElementById("Events").style.display="none";
  document.getElementById("GoBackButton").style.display="block";
  document.getElementById("RSVP").style.display="block";
}


  /*FAQ*/

var acc = document.getElementsByClassName("questions");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
  var acc = document.getElementsByClassName("questions");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  }

  // registration

  // registration valid
function validUser() {
  var returnVal = true;
  let firstpassword=document.getElementById("psw").value;
  let secondpassword=document.getElementById("psw_repeat").value;
  let validEmail = document.getElementById("email").value;
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if(firstpassword==secondpassword){
      if(re.test(String(validEmail).toLowerCase())){
          returnVal = true;
      }
      else{
        alert("email is not valid");
        returnVal = false;
      }
  }
  else{
      if(re.test(String(validEmail).toLowerCase())) {
          alert("password must be same!");
          returnVal = false;
      }
      else{
           alert("wrong details!");
      }
  }

  // VALIDATE BIRTHDAY
  var today = new Date();
  var nowyear = today.getFullYear();
  var nowmonth = today.getMonth();
  var nowday = today.getDate();
  var b = document.getElementById("Bday").value;

  var birth = new Date(b);

  var birthyear = birth.getFullYear();
  var birthmonth = birth.getMonth();
  var birthday = birth.getDate();

  var age = nowyear - birthyear;
  var age_month = nowmonth - birthmonth;
  var age_day = nowday - birthday;

      if (age > 100) {
          alert("Age cannot be more than 100 Years.Please enter correct age")
          returnVal = false;
      }
      if (age_month < 0 || (age_month == 0 && age_day < 0) && age!=19) {
          age = parseInt(age) - 1;
      }
      if (((age == 18 && age_month < 0 && age_day < 0) || age < 18)) {
          alert("Age should be more than 18 years.Please enter a valid Date of Birth");
          returnVal =false;
      }

      // Phone number API 
      const phoneInput = document.getElementById("PhoneNum");
      if(!phoneInput.checkValidity()){
          alert("phone number is not in the correct format please enter a correct number");
          returnVal = false;
      }
      return returnVal;
}
function goBackToRegister(){
      window.location.href='/Register';
}
// product page

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target === document.getElementById('id01')) {
      document.getElementById('id01').style.display = "none";
  }
  else if (event.target === document.getElementById('id02')){
      document.getElementById('id02').style.display = "none";
  }
  else if(event.target === document.getElementById('id03')){
      document.getElementById('id03').style.display = "none";
  }
}
/* Pj's - id06*/
function CH_product3() {
  document.getElementById('id06').style.display='block'; // show the
  let par = mediaModal(); // check screen size
  let words ='<p>' +
                  par+ 'Pajamas' +
                  '<br>'+
                  '2 sets of pajamas ,'+
                  '<br>'+
                  '(for male or female) ' +
                  '<br>'+
                  'Donation price : 100 NIS' +
              '</p>';
  document.getElementById('modal_img6').src="../static/media/Pjs.png";
  document.getElementById('target6').innerHTML = words;
}
/* Candies - id05*/
function F_product3() {
  document.getElementById('id05').style.display='block';
  let par = mediaModal(); // check screen size
  let words ='<p>' +
                  par+ 'Candies Basket' +
                  '<br>'+
                  'chocolates and snacks packages'+
                  '<br>'+
                  'to put a big smile on thier face' +
                  '<br>'+
                  'Donation price : 60 NIS' +
              '</p>';
  document.getElementById('modal_img5').src="../static/media/candis.png";
  document.getElementById('target5').innerHTML = words;
}
/* Pots & Pans - id04*/
function CH_product2() {
  document.getElementById('id04').style.display='block';
  let par = mediaModal(); // check screen size
  let words ='<p>' +
                  par+ 'Pots & Pans set inculdes:' +
                  '<br>'+
                  'Pot x 3 sizes- S,M,L '+
                  '<br>'+
                  'Pan x 2 size M' +
                  '<br>'+
                  'Donation price : 200 NIS' +
              '</p>';
  document.getElementById('modal_img4').src="../static/media/PotsAndPans.jfif";
  document.getElementById('target4').innerHTML = words;
}

/* Pillows & Blankets- id02*/
function CH_product1() {
  document.getElementById('id02').style.display='block';
  let par = mediaModal(); // check screen size
  let words ='<p>' +
                  par+ 'Pillows and Blankets set :' +
                  '<br>'+
                  'Pillow x 2'+
                  '<br>'+
                  'Blanket x 1' +
                  '<br>'+
                  'Donation price : 250 NIS' +
              '</p>';
  document.getElementById('modal_img2').src="../static/media/PillowsAndBlankets2.jfif";
  document.getElementById('target2').innerHTML = words;
}

/* Food basket - id01*/
function F_product1() {
  document.getElementById('id01').style.display='block';
  let par = mediaModal(); // check screen size
  let words = '<p>' +
                   par+ 'Food Basket includes: ' +
                  '<br>'+
                  'wine, rice, oil, sugar, '+
                  '<br>'+
                  'flour, tuna,cans, pasta' +
                  '<br>'+
                  'Donation price : 120 NIS' +
              '</p>';
  document.getElementById('modal_img1').src='../static/media/foodbasket.jpg'
  document.getElementById('target').innerHTML = words;
}

/* Hot Food - id03*/
function F_product2() {
  document.getElementById('id03').style.display='block';
  let par = mediaModal(); // check screen size
  let words = '<p>' +
                   par+ 'Hot food from catering: ' +
                  '<br>'+
                  'Single hot meal for one person '+
                  '<br>'+
                  'Donation price : 40 NIS' +
              '</p>';
  document.getElementById('modal_img3').src="../static/media/warmfood.jpg";
  document.getElementById('target3').innerHTML = words;
}
/* 100 NIS - id07*/
function Cash1() {
  document.getElementById('id07').style.display='block';
  let par = mediaModal(); // check screen size
  let words = '<p>' +
                   par+ 'Donate to orginiztions' +
                  '<br>'+
                  '10% will be added by the organization'+
                  '<br>'+
                  '<br>'+
                  'Donation price : 100 NIS' +
              '</p>';
  document.getElementById('target7').innerHTML = words;
}
/* 200 NIS - id08*/
function Cash2() {
  document.getElementById('id08').style.display='block';
  let par = mediaModal(); // check screen size
  let words = '<p>' +
                   par+ 'Donate to orginiztions' +
                  '<br>'+
                  '10% will be added by the organization'+
                  '<br>'+
                  '<br>'+
                  'Donation price : 200 NIS' +
              '</p>';
  document.getElementById('target8').innerHTML = words;
}
/* other price - id09*/
function Cash3() {
  document.getElementById('id09').style.display='block';
  let par = mediaModal(); // check screen size
  let words = '<p>' +
                   par+ 'Donate to orginiztions' +
                  '<br>'+
                  '10% will be added by the organization'+
                  '<br>'+
                  '<br>'+
                  'Donation price : your choice' +
              '</p>';
  document.getElementById('target9').innerHTML = words;
}

function mediaModal(){  //check if it mobile screen size
  let mediaQuery = window.matchMedia('(min-width: 768px)')
  let  par = '<b style="font-size: 5vw">';
  if (mediaQuery.matches){
     par = '<b>';
  }
  return par;  // returns tag needed
}

// registration valid
function validUS() {
  let firstpassword=document.getElementById("psw").value;
  let secondpassword=document.getElementById("psw_repeat").value;
  let validEmail = document.getElementById("email").value;
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if(firstpassword==secondpassword){
      if(re.test(String(validEmail).toLowerCase())){
      return true;
      }
      else{
        alert("email is not valid");
        return false;
      }
  }
  else{
      if(re.test(String(validEmail).toLowerCase())) {
          alert("password must be same!");
          return false;
      }
      else{
           alert("wrong details!");
      }
  }
}

function goToCheckout(){
  window.location.href='/Checkout';
}

function alertResetChoices(){
    alert("Your choices were successfully reset");
}

function onChange() {
  const password = document.querySelector('input[name=psw]');
  const confirm = document.querySelector('input[name=psw-repeat]');
  if (confirm.value === password.value) {
    confirm.setCustomValidity('');
  } else {
    confirm.setCustomValidity('Passwords do not match');
  }
}