import MainHome from '../components/home/MainHome'
import MainCourse from '../components/course/MainCourse'
import MainUser from '../components/user/MainUser'
import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from '../components/context/AuthContext'

function App() {
  return (
    <div>
      <Routes>
        <Route
          path="/"
          element={
            <AuthProvider>
              <MainHome />
            </AuthProvider>
          }
        />
        <Route
          path="courses"
          element={
            <AuthProvider>
              <MainCourse />
            </AuthProvider>
          }
        />
        <Route
          path="profile"
          element={
            <AuthProvider>
              <MainUser />
            </AuthProvider>
          }
        />
      </Routes>
    </div>
  )
}

export default App
