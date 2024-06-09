document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.dropdownmenu ul');

  menuToggle.addEventListener('click', function() {
      menu.classList.toggle('active');
      if (menu.style.display === 'flex') {
          menu.style.display = 'none';
      } else {
          menu.style.display = 'flex';
      }
  });

  // Function to check the screen width and reset styles if needed
  function checkScreenWidth() {
      if (window.innerWidth >= 768) {
          menu.style.display = 'flex'; // Ensure menu is displayed on larger screens
      } else {
          menu.style.display = 'none'; // Hide menu on smaller screens by default
          menuToggle.classList.remove('active'); // Remove active class from button
      }
  }

  // Initial check
  checkScreenWidth();

  // Check on window resize
  window.addEventListener('resize', checkScreenWidth);
});
