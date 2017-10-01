var uploader = document.getElementById("uploader");
var submit = document.getElementsByClassName("submit")[0];
// accounts for user hitting back button
uploader.files.length > 0 ? submit.disabled = false : submit.disabled = true;
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

submit.addEventListener("click", function() {
  //prevent click spam
  var processing = document.createElement("p");
  var processing_text = document.createTextNode("Processing...");
  processing.className = "processing";
  processing.appendChild(processing_text);

  this.parentElement.replaceChild(processing, this);
  document.getElementById("form").submit();
});