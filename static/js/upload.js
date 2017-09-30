var uploader = document.getElementById("uploader");
var submit = document.getElementById("submit");
// accounts for user hitting back button
uploader.files.length > 0 ? submit.disabled = false : submit.disabled = true;
console.log("hi");
uploader.addEventListener("change", function() {
  if(this.files) {
    if(this.files[0].type == "image/gif") {
      submit.disabled = false;
    } else {
      submit.disabled = true;
    }
  } else {
    submit.disabled = true;
  }
}, false);

// submit.addEventListener("click", function() {
//   //prevent click spam
//   submit.disabled = true;
// });