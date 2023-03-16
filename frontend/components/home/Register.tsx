const Register = ({
  email,
  setEmail,
  password,
  setPassword,
  confirmPassword,
  setConfirmPassword,
  handleRegister,
}) => {
  return (
    <form onSubmit={handleRegister}>
      <div className="p-2">
        <input
          type="text"
          id="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          className="w-full rounded-lg border-b-2 border-red-500 p-2 outline-none text-center"
          placeholder="Email"
        />
      </div>
      <div className="p-2">
        <input
          type="password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          className="group w-full rounded-lg border-b-2 border-red-500 p-2 outline-none text-center"
          placeholder="Password"
        />
      </div>
      <div className="p-2">
        <input
          type="password"
          id="confirmPassword"
          value={confirmPassword}
          onChange={(event) => setConfirmPassword(event.target.value)}
          className="group w-full rounded-lg border-b-2 border-red-500 p-2 outline-none text-center"
          placeholder="Confirm Password"
        />
      </div>
      <div className="p-2">
        <p>
          {password == confirmPassword ? (
            <p className="text-green-500 group:bg-green-600"> :) </p>
          ) : (
            <p className="text-red-500"> incorrect password</p>
          )}
        </p>
      </div>
      <div className="p-2">
        <div className="m-3">
          <button className="w-32 bg-white tracking-wide text-gray-800 font-bold rounded-lg border-b-2 border-red-500 hover:border-red-600 hover:bg-red-500 hover:text-white shadow-md py-2 px-6 inline-flex items-center">
            <span className="mx-auto">Register</span>
          </button>
        </div>
      </div>
    </form>
  )
}

export default Register
