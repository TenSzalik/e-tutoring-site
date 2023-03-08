const Login = ({ email, setEmail, password, setPassword, handleSubmit }) => {

  return (
    <form onSubmit={handleSubmit}>
      <div className="p-2">
        <input
          type="text"
          id="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          className="w-full rounded-lg border-b-2 border-blue-500 p-2 outline-none text-center"
          placeholder="Email"
        />
      </div>
      <div className="p-2">
        <input
          type="password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          className="w-full rounded-lg border-b-2 border-blue-500 p-2 outline-none text-center"
          placeholder="Password"
        />
      </div>
      <div className="p-2">
        <div className="m-3">
            <button
              className="w-32 bg-white tracking-wide text-gray-800 font-bold rounded-lg border-b-2 border-blue-500 hover:border-blue-600 hover:bg-blue-500 hover:text-white shadow-md py-2 px-6 inline-flex items-center">
              <span className="mx-auto">Login</span>
            </button>
          </div>
      </div>
    </form>
  )
}

export default Login
