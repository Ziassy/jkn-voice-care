const customButtons = document.getElementsByClassName("custom-button");
const toggleCheckbox = document.getElementById("toogleCheckbox");
const popupantrean = document.getElementById('popupantrean');
const buttonPelayanan = document.getElementById('button-pelayanan');
// const body = document.body;

function showCustomButton() {
const isActive = toggleCheckbox.checked;

for (let i = 0; i < customButtons.length; i++) {
  customButtons[i].style.display = isActive ? 'block' : 'none';
}

const menuIcons = document.querySelectorAll(".menu-icon");

menuIcons.forEach((menuIcon) => {
  if (isActive) {
    menuIcon.style.display = 'block';
    buttonPelayanan.addEventListener('click', showPopup);
  } else {
    menuIcon.style.display = 'none';
  }
});
}

  toggleCheckbox.addEventListener('change', showCustomButton);
  showCustomButton();



  // Function to show the popup
  function showPopup() {
    popupantrean.style.display = 'block';
    body.style.backgroundColor = 'rgb(46, 43, 43)';
  }


  /* When the user clicks on the button, 
  toggle between hiding and showing the dropdown content */
  function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }