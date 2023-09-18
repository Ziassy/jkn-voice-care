const toggleSwitchChange = () => {
  const toggleSwitch = document.getElementById('toggleSwitch');
  const select = document.getElementById('languageSelect');
  let isToggleOn = toggleSwitch.checked;

  isToggleOn = toggleSwitch.checked;
  localStorage.setItem('isToggleOn', isToggleOn ? 'true' : 'false');

  select.disabled = !isToggleOn;

  if (isToggleOn) {
    showPlayButtons();
    select.style.backgroundColor = '#06B6D4';
  } else {
    hidePlayButtons();
    select.selectedIndex = 0;
    select.style.backgroundColor = 'gray';
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
    select.style.backgroundColor = '#06B6D4';
  } else {
    toggleSwitch.checked = false;
    select.selectedIndex = 0;
    hidePlayButtons();
    select.style.backgroundColor = 'gray';
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
  const translationContent = document.getElementById('translationContent');
  const audioPlayer = document.getElementById('audioPlayer');

  const isButtonMenu = e.target.getAttribute('data-isbuttonmenu');

  // Set the translation content
  translationContent.textContent = translation;

  // Replace spaces with underscores in menuName
  const menuNameWithoutSpaces = replaceSpacesWithUnderscores(menuName);

  if (isButtonMenu === 'true') {
    // Construct the audio file URL based on the menuName
    const audioURL = `/media/audio-detail-${menuNameWithoutSpaces}.mp3`; // Adjust the file format as needed

    // Set the audio source and display the audio player
    audioPlayer.src = audioURL;
    audioPlayer.play();
  } else {

    // Construct the audio file URL based on the menuName
    const audioURL = `/media/audio-${menuNameWithoutSpaces}.mp3`; // Adjust the file format as needed

    // Set the audio source and display the audio player
    audioPlayer.src = audioURL;
    audioPlayer.play();
  }
  console.log(isButtonMenu)


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
        console.log("run this")
      });

      // saat openSubmenuButtons di klik Tampilkan submenu yang sesuai
      submenu.style.display = 'block';
      console.log(submenu)
    });
  });
};

const goBack = () => {
  window.history.back();
}

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

// Tambahkan event listener untuk body atau elemen lain yang sesuai
document.body.addEventListener('click', function (event) {
  // Loop melalui setiap popover yang ada
  popoverList.forEach(popover => {
    // Periksa apakah popover aktif
    if (popover._activeTrigger.click) {
      // Tutup popover jika di-klik di luar popover atau di button popover lain
      if (!popover._element.contains(event.target)) {
        popover.hide();
      }
    }
  });
});

// Anda juga bisa menambahkan event listener untuk menghilangkan popover saat mengklik halaman lain
window.addEventListener('beforeunload', function () {
  // Tutup semua popover sebelum meninggalkan halaman
  popoverList.forEach(popover => {
    popover.hide();
  });
});


document.querySelectorAll('.play').forEach(button => {
  button.addEventListener('click', playButtonClick);
});
document.getElementById('languageSelect').addEventListener('change', languageSelectChange);
document.addEventListener('DOMContentLoaded', initializeSubmenus);

document.getElementById('toggleSwitch').addEventListener('change', toggleSwitchChange);
loadToggleStatus();
