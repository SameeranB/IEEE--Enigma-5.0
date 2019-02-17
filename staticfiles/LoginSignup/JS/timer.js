var x;
var countDownDate = new Date("Feb 23, 2019 15:37:25").getTime();

// Update the count down every 1 second
 x = setInterval(function() {

  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with following ids as
  // day, hour, min, sec given in the html file
  document.getElementById("day").innerHTML = days + "D";
  document.getElementById("hour").innerHTML = hours + "H";
  document.getElementById("min").innerHTML = minutes + "M";
  document.getElementById("sec").innerHTML = seconds + "S";

  // If the count down is finished, write some text
  //This is the condition after the clock reaches 0
  if (distance < 0) {
    clearInterval(x);
    alert("EXPIRED");
  }

}, 1000);
