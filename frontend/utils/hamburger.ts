const initApp = () => {
  const hamburgerBtn = document.getElementById(
    'hamburger-button'
  ) as HTMLElement
  const mobileMenu = document.getElementById('mobile-menu') as HTMLElement

  const toggleMenu = () => {
    mobileMenu.classList.toggle('hidden')
    mobileMenu.classList.toggle('flex')
    hamburgerBtn.classList.toggle('toggle-btn')
  }

  hamburgerBtn.addEventListener('click', toggleMenu)
  mobileMenu.addEventListener('click', toggleMenu)
}

window.addEventListener('load', () => {
  initApp()
})
