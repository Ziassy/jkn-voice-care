const toggleSwitchChange = () => {
  const toggleSwitch = document.getElementById('toggleSwitch');
  const select = document.getElementById('languageSelect');
  let isToggleOn = toggleSwitch.checked;

  isToggleOn = toggleSwitch.checked;
  localStorage.setItem('isToggleOn', isToggleOn ? 'true' : 'false');

  select.disabled = !isToggleOn;

  if (isToggleOn) {
    showPlayButtons();
  } else {
    hidePlayButtons();
    select.selectedIndex = 0;
  }
}

const showPlayButtons = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'block';
  });
}

const hidePlayButtons = () => {
  const playButtons = document.querySelectorAll('.play');
  playButtons.forEach(button => {
    button.style.display = 'none';
  });
}

const loadToggleStatus = () => {
  const toggleSwitch = document.getElementById('toggleSwitch');
  const select = document.getElementById('languageSelect');

  const storedToggleStatus = localStorage.getItem('isToggleOn');
  if (storedToggleStatus === 'true') {
    toggleSwitch.checked = true;
    select.disabled = false;
    showPlayButtons();
  } else {
    toggleSwitch.checked = false;
    select.selectedIndex = 0;
    hidePlayButtons();
  }
}

const languageSelectChange = () => {
  const translationForm = document.querySelector('form[method="get"]');
  translationForm.submit();
}

// Function to replace spaces with underscores
const replaceSpacesWithUnderscores = (str) => {
  return str.replace(/\s+/g, ' ');
};

const playButtonClick = (e) => {
  const translation = e.target.getAttribute('data-translation');
  const menuId = e.target.getAttribute('data-menu-id');
  const menuName = e.target.getAttribute('data-menu-name');
  const detailURL = `/menu/${menuId}/`;
  const translationContent = document.getElementById('translationContent');
  const audioPlayer = document.getElementById('audioPlayer');

  // Set the translation content
  translationContent.textContent = translation;

  // Replace spaces with underscores in menuName
  const menuNameWithoutSpaces = replaceSpacesWithUnderscores(menuName);

  // Construct the audio file URL based on the menuName
  const audioURL = `/media/audio-${menuNameWithoutSpaces}.mp3`; // Adjust the file format as needed

  // Set the audio source and display the audio player
  audioPlayer.src = audioURL;
  audioPlayer.play();


  const menuDetailLink = document.querySelector('.buka-menu-button');

  if (menuDetailLink) {
    menuDetailLink.href = detailURL;
  }
};

const initializeSubmenus = () => {
  // Sembunyikan semua submenu saat halaman dimuat pertama kali
  const allSubmenus = document.querySelectorAll('.submenu');
  allSubmenus.forEach(s => {
    s.style.display = 'none';
  });

  const openSubmenuButtons = document.querySelectorAll('.open-submenu');

  openSubmenuButtons.forEach(button => {
    button.addEventListener('click', e => {
      e.preventDefault();
      const menuId = button.getAttribute('data-submenu-id');
      const submenu = document.getElementById(`submenu-${menuId}`);

      // hide semua submenu terlebih dahulu
      allSubmenus.forEach(s => {
        s.style.display = 'none';
      });

      // saat openSubmenuButtons di klik Tampilkan submenu yang sesuai
      submenu.style.display = 'block';
    });
  });
};



document.getElementById('toggleSwitch').addEventListener('change', toggleSwitchChange);
document.getElementById('languageSelect').addEventListener('change', languageSelectChange);
document.querySelectorAll('.play').forEach(button => {
  button.addEventListener('click', playButtonClick);
});
document.addEventListener('DOMContentLoaded', initializeSubmenus);

loadToggleStatus();
