import { useContext } from 'react'
import AuthContext from '../context/AuthContext'

const Login = () => {
  const { loginUser } = useContext(AuthContext)
  return (
    <div>
      <form onSubmit={loginUser}>
        <div className="p-2">
          <input
            className="w-full rounded-lg border-b-2 border-blue-500 p-2 outline-none text-center"
            type="email"
            name="email"
            placeholder="Enter Username"
          />
        </div>
        <div className="p-2">
          <input
            className="w-full rounded-lg border-b-2 border-blue-500 p-2 outline-none text-center"
            type="password"
            name="password"
            placeholder="Enter Password"
          />
        </div>
        <div className="p-2">
          <div className="m-3">
            <input
              className="w-32 bg-white tracking-wide text-gray-800 font-bold rounded-lg border-b-2 border-blue-500 hover:border-blue-600 hover:bg-blue-500 hover:text-white shadow-md py-2 px-6 inline-flex items-center"
              type="submit"
            />
          </div>
        </div>
      </form>
    </div>
  )
}

export default Login
