tailwind.config = {
    darkMode: 'class',
  }
    
    
  // grab everything we need
  const btn = document.querySelector("button.mobile-menu-button");
  const menu = document.querySelector(".mobile-menu");
  
  // add event listeners
  btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
  
  function darkModeListener() {
    document.querySelector("html").classList.toggle("dark");
  }
  
  document.querySelector("input[type='checkbox']#dark-toggle").addEventListener("click", darkModeListener);
  
  