import { useState } from 'react'
import Login from './Login'
import Register from './Register'
import apiRequest from '../../utils/apiRequest'
import urls from '../../utils/apiUrls'

function MainHome() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [fetchError, setFetchError] = useState(null)

  const handleRegister = async (event) => {
    event.preventDefault()
    if (password != confirmPassword) {
      alert('Inwalid Password')
    } else {
      const options: object = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      }

      const result = await apiRequest(urls.user, options)
      if (result) setFetchError(result)
    }
  }

  return (
    <div className="min-h-screen snap-y">
      <header className="snap-start top-0 select-none scroll-margin-top-0 h-screen w-full grid grid-flow-row-dense grid-cols-2 grid-rows-1 p-8 bg-yellow-100">
        <section className="col-span-1 grid grid-flow-row-dense grid-cols-3 grid-rows-3">
          <section className="col-span-3"></section>
          <h1 className="col-span-3 lg:text-7xl md:text-5xl text-sky-900 text-4xl">
            NoFluffTutoring
          </h1>
          <p className="col-span-3">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Vero
            voluptas dolorum placeat sed, quidem impedit perferendis hic ducimus
            libero repudiandae alias facere
          </p>
          <a href="http://localhost:5173/#login">&#2193;</a> //get normal icon
        </section>
        <section className="col-span-1"></section>
      </header>
      <header className="sticky z-50 text-white top-0 p-2 space-x-8 text-center bg-pink-500">
        <section className="mx-auto flex max-w-4xl items-center justify-between p-4">
          <h1 className="text-3xl font-medium">
            <a href="#hero">NoFluffTutoring</a>
          </h1>
          <div>
            <button
              id="hamburger-button"
              className="relative h-8 w-8 cursor-pointer text-3xl md:hidden"
            >
              <div className="absolute top-4 -mt-0.5 h-1 w-8 rounded bg-white transition-all duration-500 before:absolute before:h-1 before:w-8 before:-translate-x-4 before:-translate-y-3 before:rounded before:bg-white before:transition-all before:duration-500 before:content-[''] after:absolute after:h-1 after:w-8 after:-translate-x-4 after:translate-y-3 after:rounded after:bg-white after:transition-all after:duration-500 after:content-['']"></div>
            </button>
            <nav
              className="hidden space-x-8 text-xl md:block"
              aria-label="main"
            >
              <a href="http://localhost:5173/#login">Login / Register</a>
              <a href="http://localhost:5173/#fast-search">Fast search</a>
              <a href="http://localhost:5173/#idea">Idea</a>
              <a href="http://localhost:5173/#how-it-works">How it works?</a>
              <a href="http://localhost:5173/#more">More</a>
            </nav>
          </div>
        </section>
        <section
          id="mobile-menu"
          className="hidden justify-content-center origin-top animate-open-menu flex-col bg-pink-500 text-3xl flex"
        >
          <nav
            className="flex min-h-screen flex-col items-center py-8"
            aria-label="mobile"
          >
            <a
              href="http://localhost:5173/#login"
              className="w-full py-6 text-center hover:opacity-90"
            >
              Login / Register
            </a>
            <a
              href="http://localhost:5173/#fast-search"
              className="w-full py-6 text-center hover:opacity-90"
            >
              Fast search
            </a>
            <a
              href="http://localhost:5173/#idea"
              className="w-full py-6 text-center hover:opacity-90"
            >
              Idea
            </a>
            <a
              href="http://localhost:5173/#how-it-works"
              className="w-full py-6 text-center hover:opacity-90"
            >
              How it works?
            </a>
            <a
              href="http://localhost:5173/#more"
              className="w-full py-6 text-center hover:opacity-90"
            >
              More
            </a>
          </nav>
        </section>
      </header>
      <header
        id="login"
        className="snap-start relative z-20 flex justify-center items-center h-screen p-8 bg-green-100"
      >
        <section className="w-1/3 h-1/2 text-center p-8 border-8 border-cyan-200">
          <div className="border-8 border-teal-300 h-full">
            <Login></Login>
          </div>
        </section>
        <section className="w-1/3 h-1/2 text-center p-8 border-8 border-cyan-200">
          <div className="border-8 border-teal-300 h-full">
            <Register
              email={email}
              setEmail={setEmail}
              password={password}
              setPassword={setPassword}
              confirmPassword={confirmPassword}
              setConfirmPassword={setConfirmPassword}
              handleRegister={handleRegister}
            ></Register>
          </div>
        </section>
      </header>
      <header
        id="fast-search"
        className="snap-start relative z-20 h-screen flex justify-center items-center p-8 bg-purple-100"
      >
        <section className="w-1/2 h-1/3 text-center p-8 border-8 border-cyan-200"></section>
      </header>
      <header
        id="idea"
        className="snap-start relative z-20 h-screen flex justify-center items-center p-8 bg-purple-100"
      >
        <section className="w-1/2 h-3/4 text-center border-8 border-cyan-200"></section>
        <section className="w-1/2 h-3/4 text-center p-8 border-8 border-cyan-200"></section>
      </header>
      <header
        id="how-it-works"
        className="snap-start relative z-20 h-screen flex justify-center items-center p-8 bg-purple-100"
      >
        <section className="w-1/2 h-3/4 text-center border-8 border-cyan-200"></section>
        <section className="w-1/2 h-3/4 text-center p-8 border-8 border-cyan-200"></section>
      </header>
      <header
        id="more"
        className="snap-start relative z-20 h-screen flex justify-center items-center p-8 bg-purple-100"
      >
        <section className="w-full h-3/4 text-center border-8 border-cyan-200"></section>
      </header>
    </div>
  )
}

export default MainHome
